#!/usr/bin/env python3
import sys
import math

def build_primes(n):
    spf = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = i * p
            if v > n or p > spf[i]:
                break
            spf[v] = p
    return primes

def squarefree_and_square_part(n, primes):
    s = 1
    q = 1
    x = n
    for p in primes:
        pp = p
        if pp * pp > x:
            break
        if x % pp != 0:
            continue
        e = 0
        while x % pp == 0:
            x //= pp
            e += 1
        if e % 2 != 0:
            s *= pp
        for _ in range(e // 2):
            q *= pp
    if x > 1:
        s *= x
    return s, q

def floor_sqrt_u64(x):
    r = int(math.sqrt(float(x)))
    while (r + 1) * (r + 1) <= x:
        r += 1
    while r * r > x:
        r -= 1
    return r

def find_fundamental_pell_limited(s, x_limit):
    a0 = floor_sqrt_u64(s)
    if a0 * a0 == s:
        return None
    m = 0
    d = 1
    a = a0
    p_prev2 = 0
    p_prev1 = 1
    q_prev2 = 1
    q_prev1 = 0
    for _ in range(2_000_000):
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        diff = p * p - s * q * q
        if diff == 1 and p > 1 and p <= x_limit:
            return p, q
        if p > x_limit:
            return None
        p_prev2 = p_prev1
        p_prev1 = p
        q_prev2 = q_prev1
        q_prev1 = q
        m = d * a - m
        d = (s - m * m) // d
        a = (a0 + m) // d
    return None

def pell_solutions_up_to(s, x_limit):
    res = find_fundamental_pell_limited(s, x_limit)
    if res is None:
        return []
    x1, y1 = res
    solutions = []
    x = x1
    y = y1
    while x <= x_limit:
        solutions.append((x, y))
        nx = x1 * x + s * y1 * y
        ny = x1 * y + y1 * x
        if nx > x_limit:
            break
        x = nx
        y = ny
    return solutions

def generate_square_pivots(limit):
    m_max = int((math.sqrt(2.0 * float(limit) + 1.0) - 1.0) / 2.0)
    primes = build_primes(m_max + 2)
    grouped = {}
    for m in range(1, m_max + 1):
        n = m * (m + 1)
        s, q = squarefree_and_square_part(n, primes)
        x_max = (2 * limit - m) // m
        if s not in grouped:
            grouped[s] = []
        grouped[s].append((m, q, x_max))
    pivots = []
    for s, entries in grouped.items():
        x_max = max(e[2] for e in entries)
        sols = pell_solutions_up_to(s, x_max)
        if not sols:
            continue
        for m, q, _ in entries:
            min_d = 2 * m + 1
            m128 = m
            qs128 = q * s
            for x, y in sols:
                if x < min_d:
                    continue
                if x % 2 == 0:
                    continue
                numerator = m128 * x + qs128 * y + m128
                if numerator % 2 != 0:
                    continue
                k = numerator // 2
                if k > limit:
                    continue
                if k > 0:
                    pivots.append(k)
    pivots.sort()
    return list(dict.fromkeys(pivots))

def solve(limit):
    pivots = generate_square_pivots(limit)
    return sum(pivots)

def brute_pivots(limit):
    pivots = []
    for k in range(1, limit + 1):
        ok = False
        for m in range(1, k):
            lhs = (m + 1) * k * (k - m)
            if lhs % m != 0:
                continue
            c = lhs // m
            d = (m + 1) * (m + 1) + 4 * c
            s = int(math.sqrt(float(d)))
            root = s
            while (root + 1) * (root + 1) <= d:
                root += 1
            while root * root > d:
                root -= 1
            if root * root != d:
                continue
            numer = -(m + 1) + root
            if numer % 2 != 0:
                continue
            n = numer // 2
            if n >= k:
                ok = True
                break
        if ok:
            pivots.append(k)
    return pivots

def run_checkpoints():
    fast_small = generate_square_pivots(5000)
    brute_small = brute_pivots(5000)
    if fast_small != brute_small:
        print("Checkpoint failed for limit=5000", file=sys.stderr)
        return False
    sample = generate_square_pivots(120)
    required = [4, 21, 24, 110]
    for x in required:
        if x not in sample:
            print(f"Checkpoint failed: missing sample pivot {x}", file=sys.stderr)
            return False
    return True

def parse_arguments(args):
    options = {
        "limit": 10_000_000_000,
        "run_checkpoints": True
    }
    for arg in args:
        if arg == "--skip-checkpoints":
            options["run_checkpoints"] = False
        elif arg.startswith("--limit="):
            try:
                options["limit"] = int(arg[8:])
            except ValueError:
                print(f"Unknown argument: {arg}", file=sys.stderr)
                return None
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            return None
    if options["limit"] < 1:
        return None
    return options

def main():
    args = sys.argv[1:]
    options = parse_arguments(args)
    if options is None:
        return 1
    if options["run_checkpoints"] and not run_checkpoints():
        return 2
    print(solve(options["limit"]))
    return 0

if __name__ == "__main__":
    sys.exit(main())
