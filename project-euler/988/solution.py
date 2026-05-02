import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_representable(n, a, b):
    x = 0
    while x * a <= n:
        if (n - x * a) % b == 0:
            return True
        x += 1
    return False


def brute_force(a, b):
    gaps = []
    for n in range(1, a * b):
        if not is_representable(n, a, b):
            gaps.append(n)

    assert len(gaps) <= 20

    n = len(gaps)
    attack = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            bad = is_representable(gaps[j] - gaps[i], a, b)
            attack[i][j] = bad
            attack[j][i] = bad

    total = 0
    for mask in range(1 << n):
        ok = True
        subtotal = 0
        for i in range(n):
            if ((mask >> i) & 1) == 0:
                continue
            subtotal += gaps[i]
            rest = mask & (~0 << (i + 1))
            while rest != 0:
                j = (rest & -rest).bit_length() - 1
                if attack[i][j]:
                    ok = False
                    break
                rest &= rest - 1
            if not ok:
                break
        if ok:
            total += subtotal

    return total


def solve(a, b):
    if a > b:
        a, b = b, a

    ab = a * b
    counts = [0] * (a + 1)
    sums = [0] * (a + 1)
    counts[a] = 1

    for x in range(1, b):
        h = (ab - 1 - a * x) // b
        next_counts = counts[:]
        next_sums = sums[:]

        for limit in range(1, a + 1):
            count = counts[limit]
            if count == 0:
                continue

            prefix_sum = sums[limit]
            ymax = min(h, limit - 1)
            for y in range(1, ymax + 1):
                gap = ab - a * x - b * y
                next_counts[y] += count
                next_sums[y] += prefix_sum + count * gap

        counts, sums = next_counts, next_sums

    return sum(sums)


def run_checkpoints():
    for a in range(2, 8):
        for b in range(a + 1, 9):
            if gcd(a, b) != 1 or a * b > 35:
                continue
            assert solve(a, b) == brute_force(a, b)
            assert solve(a, b) == solve(b, a)

    assert solve(3, 5) == 23
    assert solve(5, 13) == 16336


if __name__ == "__main__":
    should_run_checkpoints = "--skip-checkpoints" not in sys.argv[1:]
    if should_run_checkpoints:
        run_checkpoints()
    print(solve(19, 53))
