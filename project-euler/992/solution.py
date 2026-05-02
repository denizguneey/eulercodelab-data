from functools import lru_cache
import sys

MOD = 987_898_789
TARGET_N = 500
K_VALUES = (1, 10, 100, 1000, 10000)


def mod_add(a, b):
    total = a + b
    return total - MOD if total >= MOD else total


def mod_mul(a, b):
    return (a * b) % MOD


def build_needed_binomials(n, k_values):
    max_row = 0
    for k in k_values:
        max_row = max(max_row, k + n - 2)

    needed = [False] * (max_row + 1)
    for k in k_values:
        for row in range(k, k + n - 1):
            needed[row] = True

    rows = [None] * (max_row + 1)
    current = [1]

    for row in range(1, max_row + 1):
        current.append(1)
        for col in range(row - 1, 0, -1):
            current[col] = mod_add(current[col], current[col - 1])
        if needed[row]:
            rows[row] = current.copy()

    return rows


def solve_endpoint(n, k, endpoint, binomials):
    right_crossings = k - (1 if endpoint == 0 else 0)
    ways = 1

    for stone in range(1, n):
        row = k + stone - 1
        if right_crossings <= 0 or right_crossings > row + 1:
            return 0
        ways = mod_mul(ways, binomials[row][right_crossings - 1])
        right_crossings = k + stone - right_crossings + (1 if endpoint > stone else 0)

    return ways


def solve(n, k, binomials):
    total = 0
    for endpoint in range(n + 1):
        total = mod_add(total, solve_endpoint(n, k, endpoint, binomials))
    return total


def brute_force(n, k):
    target = tuple(k + i for i in range(n))

    @lru_cache(maxsize=None)
    def dfs(position, counts):
        complete = True
        for i, count in enumerate(counts):
            if count > target[i]:
                return 0
            if count != target[i]:
                complete = False

        if complete:
            return 1 + (1 if position == n - 1 else 0)

        total = 0
        for nxt in (position - 1, position + 1):
            if nxt < 0 or nxt > n:
                continue
            if nxt < n:
                next_counts = list(counts)
                next_counts[nxt] += 1
                if next_counts[nxt] <= target[nxt]:
                    total += dfs(nxt, tuple(next_counts))
            else:
                total += dfs(nxt, counts)
        return total

    counts = [0] * n
    counts[0] = 1
    return dfs(0, tuple(counts))


def run_checkpoints(binomials):
    for n in range(1, 7):
        for k in range(1, 4):
            assert solve(n, k, binomials) == brute_force(n, k)

    assert solve(3, 2, binomials) == 17
    assert solve(6, 1, binomials) == 1320
    assert solve(6, 5, binomials) == 16_793_280


def solve_target(binomials):
    total = 0
    for k in K_VALUES:
        total = mod_add(total, solve(TARGET_N, k, binomials))
    return total


def main(argv=None):
    argv = sys.argv if argv is None else argv
    should_run_checkpoints = True

    for arg in argv[1:]:
        if arg == "--skip-checkpoints":
            should_run_checkpoints = False
            continue
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return 1

    binomials = build_needed_binomials(TARGET_N, K_VALUES)

    if should_run_checkpoints:
        run_checkpoints(binomials)

    print(solve_target(binomials))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
