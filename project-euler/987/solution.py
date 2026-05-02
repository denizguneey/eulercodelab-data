import os
from concurrent.futures import ProcessPoolExecutor


STARTS = 10
RANKS = 13
MAX_STRAIGHTS = 8
FREE_STATE = 4

COVER = (
    (0, 1, 2, 3, 12),
    (0, 1, 2, 3, 4),
    (1, 2, 3, 4, 5),
    (2, 3, 4, 5, 6),
    (3, 4, 5, 6, 7),
    (4, 5, 6, 7, 8),
    (5, 6, 7, 8, 9),
    (6, 7, 8, 9, 10),
    (7, 8, 9, 10, 11),
    (8, 9, 10, 11, 12),
)

FACT = (1, 1, 2, 6, 24, 120, 720, 5040, 40320)
POW5 = (1, 5, 25, 125, 625, 3125, 15625, 78125, 390625)


def build_suit_perms():
    perms = [[] for _ in range(5)]
    perms[0].append((0, 0, 0, 0))
    for a in range(4):
        perms[1].append((a, 0, 0, 0))
        for b in range(4):
            if b == a:
                continue
            perms[2].append((a, b, 0, 0))
            for c in range(4):
                if c == a or c == b:
                    continue
                perms[3].append((a, b, c, 0))
                for d in range(4):
                    if d == a or d == b or d == c:
                        continue
                    perms[4].append((a, b, c, d))
    return tuple(tuple(group) for group in perms)


SUIT_PERMS = build_suit_perms()


def build_pattern_data(pattern):
    straight_count = 0
    first_rank = [0] * MAX_STRAIGHTS
    last_rank = [0] * MAX_STRAIGHTS
    active_mask = [0] * MAX_STRAIGHTS
    divisor = 1

    for start_idx, copies in enumerate(pattern):
        divisor *= FACT[copies]
        ranks = COVER[start_idx]
        mask = 0
        for rank in ranks:
            mask |= 1 << rank
        for _ in range(copies):
            label = straight_count
            straight_count += 1
            first_rank[label] = ranks[0]
            last_rank[label] = ranks[4]
            active_mask[label] = mask

    entry_pos = [[-1] * MAX_STRAIGHTS for _ in range(RANKS)]
    next_pos = [[-1] * MAX_STRAIGHTS for _ in range(RANKS)]
    current_labels = [[0] * MAX_STRAIGHTS for _ in range(RANKS)]
    next_labels = [[0] * MAX_STRAIGHTS for _ in range(RANKS)]
    current_count = [0] * RANKS
    next_count = [0] * RANKS

    for rank in range(RANKS):
        current_idx = 0
        next_idx = 0
        for label in range(straight_count):
            if (active_mask[label] >> rank) & 1:
                current_labels[rank][current_idx] = label
                current_idx += 1
            if first_rank[label] <= rank < last_rank[label]:
                next_pos[rank][label] = next_idx
                next_labels[rank][next_idx] = label
                next_idx += 1
        current_count[rank] = current_idx
        next_count[rank] = next_idx

        entry_idx = 0
        for label in range(straight_count):
            if first_rank[label] < rank <= last_rank[label]:
                entry_pos[rank][label] = entry_idx
                entry_idx += 1

    return (
        straight_count,
        last_rank,
        active_mask,
        entry_pos,
        next_pos,
        current_labels,
        next_labels,
        current_count,
        next_count,
        divisor,
    )


def count_pattern(pattern):
    (
        _straight_count,
        last_rank,
        active_mask,
        entry_pos,
        next_pos,
        current_labels,
        next_labels,
        current_count,
        next_count,
        divisor,
    ) = build_pattern_data(pattern)

    current = {0: 1}
    for rank in range(RANKS):
        next_map = {}
        current_row = current_labels[rank]
        next_row = next_labels[rank]
        entry_row = entry_pos[rank]
        next_pos_row = next_pos[rank]
        rank_last = last_rank
        rank_active = active_mask
        curr_count = current_count[rank]
        nxt_count = next_count[rank]

        for state_code, ways in current.items():
            state_digits = [0] * MAX_STRAIGHTS
            tmp = state_code
            for i in range(MAX_STRAIGHTS):
                state_digits[i] = tmp % 5
                tmp //= 5

            carried_code = 0
            for idx in range(nxt_count):
                label = next_row[idx]
                if ((rank_active[label] >> rank) & 1) == 0:
                    old_pos = entry_row[label]
                    carried_code += state_digits[old_pos] * POW5[idx]

            for suits in SUIT_PERMS[curr_count]:
                ok = True
                next_code = carried_code

                for idx in range(curr_count):
                    label = current_row[idx]
                    suit = suits[idx]
                    old_pos = entry_row[label]

                    new_state = suit
                    if old_pos != -1:
                        old_state = state_digits[old_pos]
                        if old_state == FREE_STATE or old_state != suit:
                            new_state = FREE_STATE
                        else:
                            new_state = old_state

                    if rank == rank_last[label]:
                        if new_state != FREE_STATE:
                            ok = False
                            break
                    else:
                        out_pos = next_pos_row[label]
                        next_code += new_state * POW5[out_pos]

                if not ok:
                    continue

                next_map[next_code] = next_map.get(next_code, 0) + ways

        current = next_map

    return current[0] // divisor


def generate_patterns_rec(start_idx, remaining, pattern, occupancy, out):
    if start_idx == STARTS:
        if remaining == 0:
            out.append(tuple(pattern))
        return

    ranks = COVER[start_idx]
    limit = min(4, remaining)
    for copies in range(limit + 1):
        ok = True
        for rank in ranks:
            if occupancy[rank] + copies > 4:
                ok = False
                break
        if not ok:
            break

        pattern[start_idx] = copies
        for rank in ranks:
            occupancy[rank] += copies
        generate_patterns_rec(start_idx + 1, remaining - copies, pattern, occupancy, out)
        for rank in ranks:
            occupancy[rank] -= copies

    pattern[start_idx] = 0


def generate_patterns(straight_count):
    out = []
    generate_patterns_rec(0, straight_count, [0] * STARTS, [0] * RANKS, out)
    return out


def count_total_single_thread(straight_count):
    total = 0
    for pattern in generate_patterns(straight_count):
        total += count_pattern(pattern)
    return total


def count_total_parallel(straight_count):
    patterns = generate_patterns(straight_count)
    worker_count = min(32, max(1, os.cpu_count() or 1))
    if worker_count == 1 or len(patterns) < 8:
        return sum(count_pattern(pattern) for pattern in patterns)

    try:
        with ProcessPoolExecutor(max_workers=worker_count) as executor:
            return sum(executor.map(count_pattern, patterns, chunksize=8))
    except Exception:
        return sum(count_pattern(pattern) for pattern in patterns)


def solve():
    assert count_total_single_thread(1) == 10200
    assert count_total_single_thread(2) == 31832952
    return str(count_total_parallel(8))


if __name__ == "__main__":
    print(solve())
