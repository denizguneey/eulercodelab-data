import math

def solve():
    MOD = 1000000007
    n = 10000000

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD
            exp >>= 1
        return r

    # SPF sieve
    spf = list(range(n + 1))
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p:
            for q in range(p*p, n+1, p):
                if spf[q] == q: spf[q] = p

    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD

    exponent = [0] * (n + 1)
    power_mod = [1] * (n + 1)

    # Product of (p^e + 1) tracker
    product = 1; zeros = 0
    inv_cache = {}

    def get_inv(x):
        if x not in inv_cache: inv_cache[x] = mod_pow(x, MOD - 2)
        return inv_cache[x]

    def adjust(p, delta):
        nonlocal product, zeros
        old_exp = exponent[p]; pp = power_mod[p]
        if old_exp > 0:
            v = (pp + 1) % MOD
            if v == 0: zeros -= 1
            else: product = product * get_inv(v) % MOD
        if delta > 0:
            for _ in range(delta): pp = pp * p % MOD
        else:
            ip = inv[p]
            for _ in range(-delta): pp = pp * ip % MOD
        exponent[p] = old_exp + delta
        power_mod[p] = pp
        if old_exp + delta > 0:
            v = (pp + 1) % MOD
            if v == 0: zeros += 1
            else: product = product * v % MOD

    def apply_fact(x, sign):
        while x > 1:
            p = spf[x]; cnt = 0
            while x % p == 0: x //= p; cnt += 1
            adjust(p, sign * cnt)

    binom_mod = 1; answer = 0; half = n // 2
    for k in range(1, half + 1):
        apply_fact(n - k + 1, 1)
        apply_fact(k, -1)
        binom_mod = binom_mod * (n - k + 1) % MOD * inv[k] % MOD
        q_mod = 0 if zeros > 0 else product
        r_mod = (q_mod + MOD - binom_mod) % MOD
        weight = 1 if k == n - k else 2
        answer = (answer + weight * r_mod) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
