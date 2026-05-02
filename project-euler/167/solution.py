def solve():
    target_k = 100000000000

    def brute_ulam(a, b, min_last):
        seq = [a, b]
        reps = {a + b: 1}
        cand = b + 1
        while seq[-1] < min_last:
            while True:
                w = reps.get(cand, 0)
                if w == 1: break
                cand += 1
            nxt = cand
            for x in seq:
                if x == nxt: continue
                s = x + nxt
                reps[s] = min(reps.get(s, 0) + 1, 2)
            seq.append(nxt)
            cand = nxt + 1
        return seq

    def kth_term(v, k):
        gap = v + 1
        second_even = 2 * (v + 1)
        seed_limit = 2 * gap + 1
        seed = brute_ulam(2, v, seed_limit)
        members = set(seed)

        bits = [1 if (2*t+1) in members else 0 for t in range(gap)]
        prefix = [0] * (gap + 1)
        for i in range(gap): prefix[i+1] = prefix[i] + bits[i]
        odd_lt_se = prefix[gap]
        se_idx = 2 + odd_lt_se

        state_count = 1 << gap
        seen = [-1] * state_count
        state = 0
        for i in range(gap): state = (state << 1) | bits[i]
        seen[state] = 0
        lower_mask = (1 << (gap-1)) - 1 if gap > 1 else 0
        bit_list = list(bits)
        po_list = list(prefix)
        step = 0
        while True:
            oldest = (state >> (gap-1)) & 1
            newest = state & 1
            nb = oldest ^ newest
            bit_list.append(nb)
            po_list.append(po_list[-1] + nb)
            state = ((state & lower_mask) << 1) | nb
            step += 1
            prev = seen[state]
            if prev >= 0:
                cycle_start = prev; cycle_end = step; break
            seen[state] = step

        cT_start = gap - 1 + cycle_start
        cT_end = gap - 1 + cycle_end
        cycle_len = cT_end - cT_start
        ones_before = po_list[cT_start + 1]
        ones_per_cycle = po_list[cT_end + 1] - ones_before
        cpf = [0] * (cycle_len + 1)
        for i in range(cycle_len):
            cpf[i+1] = cpf[i] + bit_list[cT_start + 1 + i]

        if k == 1: return 2
        if k == se_idx: return second_even
        odd_rank = k - 1 if k < se_idx else k - 2

        if odd_rank <= ones_before:
            lo, hi = 0, cT_start + 1
            while lo < hi:
                mid = (lo + hi) // 2
                if po_list[mid + 1] >= odd_rank: hi = mid
                else: lo = mid + 1
            return 2 * lo + 1
        else:
            rem = odd_rank - ones_before
            full_cycles = (rem - 1) // ones_per_cycle
            rem_inside = rem - full_cycles * ones_per_cycle
            lo, hi = 0, cycle_len
            while lo < hi:
                mid = (lo + hi) // 2
                if cpf[mid + 1] >= rem_inside: hi = mid
                else: lo = mid + 1
            t = cT_start + full_cycles * cycle_len + lo + 1
            return 2 * t + 1

    total = 0
    for n in range(2, 11):
        v = 2 * n + 1
        total += kth_term(v, target_k)
    return str(total)

if __name__ == '__main__':
    print(solve())
