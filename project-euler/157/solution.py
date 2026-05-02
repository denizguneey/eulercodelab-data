import sys

def ipow(base, exp):
    out = 1
    while exp > 0:
        out *= base
        exp -= 1
    return out

def divisor_count(x):
    count = 1
    p = 2
    while p * p <= x:
        e = 1
        while x % p == 0:
            x //= p
            e += 1
        count *= e
        p += 1
    if x != 1:
        count *= 2
    return count

def count_for_n(n):
    total = 0
    for a2 in range(0, 1):  # a2 <= 0 means only a2=0
        for b2 in range(0, n - a2 + 1):
            if a2 != 0 and b2 != 0:
                continue
            for a5 in range(0, (n if b2 else 0) + 1):
                for b5 in range(0, n - a5 + 1):
                    if a5 != 0 and b5 != 0:
                        continue

                    left = ipow(2, a2) * ipow(5, a5)
                    right = ipow(2, b2) * ipow(5, b5)
                    scale = ipow(2, n - a2 - b2) * ipow(5, n - a5 - b5)
                    total += divisor_count((left + right) * scale)
    return total

def solve(max_n):
    total = 0
    for n in range(1, max_n + 1):
        total += count_for_n(n)
    return total

def main():
    max_n = 9
    run_checkpoints = True

    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--max-n="):
            try:
                max_n = int(arg[8:])
                if max_n < 1:
                    sys.exit(1)
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)

    if run_checkpoints:
        if count_for_n(1) != 20:
            sys.stderr.write("Checkpoint failed for n=1\n")
            sys.exit(2)

    print(solve(max_n))

if __name__ == "__main__":
    main()
