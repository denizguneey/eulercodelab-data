import math

def solve():
    LIMIT = 10**12
    MASK32 = 0xFFFFFFFF

    def mod_mul(a, b, mod):
        return a * b % mod

    def mod_pow(base, exp, mod):
        result = 1 % mod
        cur = base % mod
        while exp > 0:
            if exp & 1: result = mod_mul(result, cur, mod)
            cur = mod_mul(cur, cur, mod)
            exp >>= 1
        return result

    def is_prime(n):
        if n < 2: return False
        for p in [2, 3, 5, 7, 11, 13]:
            if n == p: return True
            if n % p == 0: return False
        d = n - 1
        s = 0
        while d % 2 == 0: d >>= 1; s += 1
        for a in [2, 3, 5, 7, 11, 13]:
            if a >= n: continue
            x = mod_pow(a, d, n)
            if x == 1 or x == n - 1: continue
            witness = True
            for _ in range(1, s):
                x = mod_mul(x, x, n)
                if x == n - 1: witness = False; break
            if witness: return False
        return True

    def gen_hamming(limit):
        out = []
        a = 1
        while a <= limit:
            b = a
            while b <= limit:
                c = b
                while c <= limit:
                    out.append(c)
                    if c > limit // 5: break
                    c *= 5
                if b > limit // 3: break
                b *= 3
            if a > limit // 2: break
            a *= 2
        out = sorted(set(out))
        return out

    hamming = gen_hamming(LIMIT)
    prefix_mod = [0] * (len(hamming) + 1)
    for i in range(len(hamming)):
        prefix_mod[i+1] = (prefix_mod[i] + (hamming[i] & MASK32)) & MASK32

    admissible = sorted(p for h in hamming if (p := h + 1) > 5 and p <= LIMIT and is_prime(p))

    import bisect
    def sum_hamming_mod(x):
        cnt = bisect.bisect_right(hamming, x)
        return prefix_mod[cnt]

    total_mod = 0
    def dfs(idx, prod):
        nonlocal total_mod
        h_sum = sum_hamming_mod(LIMIT // prod)
        total_mod = (total_mod + ((prod & MASK32) * h_sum & MASK32)) & MASK32
        for i in range(idx, len(admissible)):
            p = admissible[i]
            if prod > LIMIT // p: break
            dfs(i + 1, prod * p)

    dfs(0, 1)
    return str(total_mod)

if __name__ == '__main__':
    print(solve())
