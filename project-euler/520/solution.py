MOD = 1000000123

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def mod_inverse(x):
    return pow(x % MOD, MOD - 2, MOD)

def geom_sum_from_one(lam, n):
    if n == 0:
        return 0
    if lam == 1:
        return n % MOD
    if lam == 0:
        return 0
    lm = lam % MOD
    if lm < 0:
        lm += MOD
    num = (lm * ((mod_pow(lm, n) + MOD - 1) % MOD)) % MOD
    den = (lm + MOD - 1) % MOD
    return (num * mod_inverse(den)) % MOD

def geom_sum_from_zero(lam, n):
    if n == 0:
        return 0
    if lam == 1:
        return n % MOD
    if lam == 0:
        return 1
    lm = lam % MOD
    if lm < 0:
        lm += MOD
    num = (mod_pow(lm, n) + MOD - 1) % MOD
    den = (lm + MOD - 1) % MOD
    return (num * mod_inverse(den)) % MOD

def expand_coeffs_F():
    poly1 = {(0, 0): 1}
    base1 = [(0, 0, 2), (1, 0, 1), (0, 1, -1)]
    for _ in range(5):
        nxt = {}
        for (a, b), val in poly1.items():
            for da, db, dc in base1:
                nxt[(a+da, b+db)] = nxt.get((a+da, b+db), 0) + val * dc
        poly1 = nxt

    poly2 = {(0, 0): 1}
    base2 = [(1, 0, 1), (0, 1, 1)]
    for _ in range(5):
        nxt = {}
        for (a, b), val in poly2.items():
            for da, db, dc in base2:
                nxt[(a+da, b+db)] = nxt.get((a+da, b+db), 0) + val * dc
        poly2 = nxt

    both = {}
    for (a1, b1), v1 in poly1.items():
        for (a2, b2), v2 in poly2.items():
            both[(a1+a2, b1+b2)] = both.get((a1+a2, b1+b2), 0) + v1 * v2

    by_lambda = {}
    for (a, b), val in both.items():
        by_lambda[a - b] = by_lambda.get(a - b, 0) + val
    return by_lambda

def expand_coeffs_G():
    poly1 = {(0, 0): 1}
    base1 = [(0, 0, 2), (1, 0, 1), (0, 1, -1)]
    for _ in range(5):
        nxt = {}
        for (a, b), val in poly1.items():
            for da, db, dc in base1:
                nxt[(a+da, b+db)] = nxt.get((a+da, b+db), 0) + val * dc
        poly1 = nxt

    poly2 = {(0, 0): 1}
    base2 = [(1, 0, 1), (0, 1, 1)]
    for _ in range(4):
        nxt = {}
        for (a, b), val in poly2.items():
            for da, db, dc in base2:
                nxt[(a+da, b+db)] = nxt.get((a+da, b+db), 0) + val * dc
        poly2 = nxt

    diff = {(1, 0): 1, (0, 1): -1}

    tmp = {}
    for (a1, b1), v1 in poly1.items():
        for (a2, b2), v2 in poly2.items():
            tmp[(a1+a2, b1+b2)] = tmp.get((a1+a2, b1+b2), 0) + v1 * v2

    both = {}
    for (a1, b1), v1 in tmp.items():
        for (a2, b2), v2 in diff.items():
            both[(a1+a2, b1+b2)] = both.get((a1+a2, b1+b2), 0) + v1 * v2

    by_lambda = {}
    for (a, b), val in both.items():
        by_lambda[a - b] = by_lambda.get(a - b, 0) + val
    return by_lambda

def Q(n, cf, cg, inv_two_pow_10):
    sum_A = 0
    for lam, coeff in cf.items():
        geom = geom_sum_from_one(lam, n)
        coeff_mod = coeff % MOD
        if coeff_mod < 0:
            coeff_mod += MOD
        sum_A = (sum_A + coeff_mod * geom) % MOD

    sum_B = 0
    for lam, coeff in cg.items():
        geom = geom_sum_from_zero(lam, n)
        coeff_mod = coeff % MOD
        if coeff_mod < 0:
            coeff_mod += MOD
        sum_B = (sum_B + coeff_mod * geom) % MOD

    return (((sum_A + MOD - sum_B) % MOD) * inv_two_pow_10) % MOD

def solve():
    max_power = 39
    cf = expand_coeffs_F()
    cg = expand_coeffs_G()
    inv_two_pow_10 = mod_inverse(1024)

    ans = 0
    for u in range(1, max_power + 1):
        n = 1 << u
        ans += Q(n, cf, cg, inv_two_pow_10)
        if ans >= MOD:
            ans -= MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
