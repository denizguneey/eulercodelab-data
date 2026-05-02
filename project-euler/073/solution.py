import sys


def count_between(a, b, c, d, limit):
    # Iterative Stern-Brocot traversal to avoid Python recursion depth limits.
    stack = [(a, b, c, d)]
    total = 0
    while stack:
        left_n, left_d, right_n, right_d = stack.pop()
        num = left_n + right_n
        den = left_d + right_d
        if den > limit:
            continue
        total += 1
        stack.append((left_n, left_d, num, den))
        stack.append((num, den, right_n, right_d))
    return total

def solve(limit):
    return count_between(1, 3, 1, 2, limit)

def run_checkpoints():
    if solve(8) != 3:
        sys.stderr.write("Checkpoint failed for limit=8\n")
        return False
    if solve(12) != 7:
        sys.stderr.write("Checkpoint failed for limit=12\n")
        return False
    return True

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=12000)
    parser.add_argument('--skip-checkpoints', action='store_true')
    args = parser.parse_args()

    if args.limit < 2:
        sys.stderr.write("Limit must be at least 2\n")
        return 1

    if not args.skip_checkpoints and not run_checkpoints():
        return 2

    print(solve(args.limit))
    return 0

if __name__ == "__main__":
    sys.exit(main())
