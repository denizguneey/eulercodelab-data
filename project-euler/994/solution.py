import sys
from array import array

TARGET_M = 1234 * 100_000_000
TARGET_N = 2345 * 100_000_000
MOD = 1_000_000_007
SIEVE_LIMIT = 5_000_000
INV2 = 500_000_004
INV3 = 333_333_336
INV6 = 166_666_668


def add_mod(a, b):
    s = a + b
    return s - MOD if s >= MOD else s


def sub_mod(a, b):
    return a - b if a >= b else a + MOD - b


def mul_mod(a, b):
    return (a % MOD) * (b % MOD) % MOD


def sum_power(power, n):
    a = n % MOD
    b = (n + 1) % MOD
    if power == 0:
        return a
    if power == 1:
        return a * b % MOD * INV2 % MOD
    if power == 2:
        c = (2 * (n % MOD) + 1) % MOD
        return a * b % MOD * c % MOD * INV6 % MOD
    t = a * b % MOD * INV2 % MOD
    return t * t % MOD


def range_power(power, lo, hi):
    return sub_mod(sum_power(power, hi), sum_power(power, lo - 1))


def choose2(n):
    return n % MOD * ((n - 1) % MOD) % MOD * INV2 % MOD


def choose3(n):
    if n < 3:
        return 0
    return n % MOD * ((n - 1) % MOD) % MOD * ((n - 2) % MOD) % MOD * INV6 % MOD


def triangle_number(n):
    return n % MOD * ((n + 1) % MOD) % MOD * INV2 % MOD


class TotientSummatory:
    def __init__(self, limit):
        self.limit = limit
        self.sums = [array("I", [0]) * (limit + 1) for _ in range(3)]
        self.memo = [{} for _ in range(3)]
        self._build()

    def prefix(self, power, n):
        if n <= self.limit:
            return self.sums[power][n]

        table = self.memo[power]
        cached = table.get(n)
        if cached is not None:
            return cached

        result = sum_power(power + 1, n)
        lo = 2
        while lo <= n:
            q = n // lo
            hi = n // q
            block = range_power(power, lo, hi)
            result = (result - block * self.prefix(power, q)) % MOD
            lo = hi + 1

        table[n] = result
        return result

    def _build(self):
        limit = self.limit
        phi = array("I", range(limit + 1))
        phi[1] = 1

        for i in range(2, limit + 1):
            if phi[i] == i:
                for j in range(i, limit + 1, i):
                    phi[j] -= phi[j] // i

        s0, s1, s2 = self.sums
        for i in range(1, limit + 1):
            im = i % MOD
            ph = phi[i] % MOD
            s0[i] = (s0[i - 1] + ph) % MOD
            s1[i] = (s1[i - 1] + im * ph) % MOD
            s2[i] = (s2[i - 1] + im * im % MOD * ph) % MOD


def pairwise_triangle_candidates(m, n):
    total = mul_mod(choose3(m), choose3(n))
    total = add_mod(total, mul_mod(mul_mod(choose3(m), n % MOD), (n - 1) % MOD))
    total = add_mod(total, mul_mod(mul_mod(m % MOD, (m - 1) % MOD), choose3(n)))
    corner = mul_mod(mul_mod(m % MOD, (m - 1) % MOD), mul_mod(n % MOD, (n - 1) % MOD))
    total = add_mod(total, mul_mod(corner, INV2))
    return total


def concurrent_triples(m, n, totient):
    limit = min(m, n) - 1
    total = 0
    lo = 2

    while lo <= limit:
        qm = (m - 1) // lo
        qn = (n - 1) // lo
        hi = min((m - 1) // qm, (n - 1) // qn)

        s0 = sub_mod(totient.prefix(0, hi), totient.prefix(0, lo - 1))
        s1 = sub_mod(totient.prefix(1, hi), totient.prefix(1, lo - 1))
        s2 = sub_mod(totient.prefix(2, hi), totient.prefix(2, lo - 1))

        am0 = mul_mod(qm, m)
        an0 = mul_mod(qn, n)
        am1 = triangle_number(qm)
        an1 = triangle_number(qn)

        term = mul_mod(mul_mod(am0, an0), s0)
        term = sub_mod(term, mul_mod(add_mod(mul_mod(am0, an1), mul_mod(am1, an0)), s1))
        term = add_mod(term, mul_mod(mul_mod(am1, an1), s2))
        total = add_mod(total, term)

        lo = hi + 1

    return total


def solve_mod(m, n, totient):
    return sub_mod(pairwise_triangle_candidates(m, n), concurrent_triples(m, n, totient))


def pair_intersects(a, b):
    return a[0] == b[0] or a[1] == b[1] or (a[0] - b[0]) * (a[1] - b[1]) < 0


def collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (b[1] - a[1]) * (c[0] - a[0])


def brute_count(m, n):
    segments = [(i, j) for i in range(1, m + 1) for j in range(1, n + 1)]
    total = 0

    for a in range(len(segments)):
        for b in range(a + 1, len(segments)):
            for c in range(b + 1, len(segments)):
                sa = segments[a]
                sb = segments[b]
                sc = segments[c]
                if (
                    pair_intersects(sa, sb)
                    and pair_intersects(sa, sc)
                    and pair_intersects(sb, sc)
                    and not collinear(sa, sb, sc)
                ):
                    total += 1

    return total


def run_checkpoints(totient):
    for m in range(1, 6):
        for n in range(1, 6):
            assert solve_mod(m, n, totient) == brute_count(m, n)

    assert solve_mod(2, 3, totient) == 8
    assert solve_mod(3, 5, totient) == 146
    assert solve_mod(12, 23, totient) == 756_716


def main(argv=None):
    argv = sys.argv if argv is None else argv
    should_run_checkpoints = True

    for arg in argv[1:]:
        if arg == "--skip-checkpoints":
            should_run_checkpoints = False
            continue
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return 1

    totient = TotientSummatory(SIEVE_LIMIT)
    if should_run_checkpoints:
        run_checkpoints(totient)

    print(solve_mod(TARGET_M, TARGET_N, totient))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
