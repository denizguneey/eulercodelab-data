import math
import sys

DEFAULT_LIMIT = 10_000_000


def parse_arguments(argv):
    limit = DEFAULT_LIMIT
    run_checkpoints = True

    for arg in argv[1:]:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            continue
        if arg.startswith("--limit="):
            tail = arg[len("--limit="):]
            if not tail.isdigit():
                raise ValueError(f"Invalid limit: {arg}")
            limit = int(tail)
            continue
        raise ValueError(f"Unknown argument: {arg}")

    return limit, run_checkpoints


def arithmetic_series_sum(count):
    return count * (count + 1) // 2


def contribution(limit, base_sum):
    copies = limit // base_sum
    return base_sum * arithmetic_series_sum(copies)


def solve(limit=DEFAULT_LIMIT):
    if limit <= 0:
        return 0

    gcd = math.gcd
    total = 0
    max_n = math.isqrt(limit) + 2

    for n in range(1, max_n + 1):
        for m in range(n + 1, 5 * n + 1, 2):
            if gcd(m, n) != 1:
                continue

            b = 5 * m * n - m * m - n * n
            c = m * m - 4 * m * n + n * n
            if b <= 0 or c <= 0:
                continue

            sum_plus = n * (5 * m - n)
            if sum_plus <= limit:
                total += contribution(limit, sum_plus)

            a_minus = 4 * m * n - m * m
            if a_minus > 0:
                sum_minus = m * (5 * n - m)
                if sum_minus <= limit:
                    total += contribution(limit, sum_minus)

        for m in range(n + 1, 2 * n + 1, 2):
            if gcd(m, n) != 1:
                continue

            b = 3 * m * m - 7 * n * n
            c = 2 * (3 * n * n - m * m)
            if b <= 0 or c <= 0:
                continue

            sum_plus = 4 * m * m + 2 * m * n - 6 * n * n
            if sum_plus > 0 and sum_plus <= limit:
                total += contribution(limit, sum_plus)

            a_minus = 3 * m * m - 2 * m * n - 5 * n * n
            if a_minus > 0:
                sum_minus = 4 * m * m - 2 * m * n - 6 * n * n
                if sum_minus > 0 and sum_minus <= limit:
                    total += contribution(limit, sum_minus)

    return total


def brute_force(limit):
    total = 0
    for a in range(1, limit + 1):
        for b in range(1, limit - a + 1):
            max_c = limit - a - b
            for c in range(1, max_c + 1):
                if a * (a + c) + (b + c) * (b + c) == 4 * (b + c) * (a + c):
                    total += a + b + c
    return total


def run_checkpoints():
    if solve(50) != brute_force(50):
        raise AssertionError("Checkpoint failed for limit=50")
    if solve(200) != brute_force(200):
        raise AssertionError("Checkpoint failed for limit=200")


def main(argv=None):
    argv = sys.argv if argv is None else argv
    try:
        limit, should_run_checkpoints = parse_arguments(argv)
        if should_run_checkpoints:
            run_checkpoints()
        print(solve(limit))
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1
    except AssertionError as exc:
        print(exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
