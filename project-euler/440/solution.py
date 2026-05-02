import math

def solve():
    MOD = 987898789
    l = 2000

    def mod_pow_int(base, exp, mod=MOD):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    def mat_mul(x, y):
        return [
            (x[0]*y[0] + x[1]*y[2]) % MOD, (x[0]*y[1] + x[1]*y[3]) % MOD,
            (x[2]*y[0] + x[3]*y[2]) % MOD, (x[2]*y[1] + x[3]*y[3]) % MOD
        ]

    def mat_pow(base, exp):
        r = [1,0,0,1]
        while exp > 0:
            if exp & 1: r = mat_mul(r, base)
            exp >>= 1
            if exp > 0: base = mat_mul(base, base)
        return r

    # Sequence period
    A = [10,1,1,0]
    leg = mod_pow_int(104 % MOD, (MOD-1)//2)
    cand = MOD - 1 if leg == 1 else MOD + 1

    def factorize(n):
        fac = []; x = n
        p = 2
        while p*p <= x:
            if x % p == 0:
                e = 0
                while x % p == 0: x //= p; e += 1
                fac.append((p, e))
            p += 1
        if x > 1: fac.append((x, 1))
        return fac

    period = cand
    for q, _ in factorize(cand):
        while period % q == 0:
            trial = period // q
            p = mat_pow(A, trial)
            if p == [1,0,0,1]: period = trial
            else: break

    # Powers of matrix for fast T computation
    pw = [A[:]]
    for _ in range(63): pw.append(mat_mul(pw[-1], pw[-1]))

    def T_mod(n):
        if n == 0: return 1
        v0, v1 = 10, 1; e = n - 1; bit = 0
        while e > 0:
            if e & 1:
                m = pw[bit]
                v0, v1 = (m[0]*v0 + m[1]*v1) % MOD, (m[2]*v0 + m[3]*v1) % MOD
            e >>= 1; bit += 1
        return v0

    # Counts of pairs (a,b) with same v2 and gcd=d
    v2 = [0]*(l+1)
    for x in range(1, l+1):
        v2[x] = (x & -x).bit_length() - 1
    cnt = [0]*(l+1)
    for a in range(1, l+1):
        ta = v2[a]
        for b in range(1, l+1):
            if v2[b] != ta: continue
            cnt[math.gcd(a, b)] += 1

    same_total = sum(cnt[1:l+1])
    total_pairs = l * l
    count_diff = total_pairs - same_total

    ans = 0
    for c in range(1, l+1):
        base = 10 if c & 1 else 1
        sum_c = count_diff % MOD * base % MOD
        p = 1
        for d in range(1, l+1):
            p = p * c % period
            tv = T_mod(p)
            sum_c = (sum_c + cnt[d] % MOD * tv) % MOD
        ans = (ans + sum_c) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
