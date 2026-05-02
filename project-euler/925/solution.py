def solve():
    MOD = 1000000007
    INV6 = 166666668
    k = 16

    def mul_mod(a, b): return a * b % MOD
    def add_mod(a, b): return (a + b) % MOD
    def sub_mod(a, b): return (a - b) % MOD

    def next_perm(digits):
        n = len(digits); i = n - 2
        while i >= 0 and digits[i] >= digits[i+1]: i -= 1
        if i < 0: return None
        j = n - 1
        while digits[j] <= digits[i]: j -= 1
        d = list(digits); d[i], d[j] = d[j], d[i]
        d[i+1:] = d[i+1:][::-1]
        return d

    def parse_mod(digits):
        v = 0
        for d in digits: v = (v * 10 + d) % MOD
        return v

    def b_diff_mod(n):
        if n == 0: return 0
        digits = []; x = n
        while x > 0: digits.append(x % 10); x //= 10
        digits.reverse()
        nm = n % MOD
        nxt = next_perm(digits)
        if nxt is None: return (MOD - nm) % MOD if nm else 0
        return sub_mod(parse_mod(nxt), nm)

    pow10 = [1]*(k+1)
    for i in range(1, k+1): pow10[i] = pow10[i-1]*10
    pow10_mod = [1]*(k+1)
    for i in range(1, k+1): pow10_mod[i] = pow10_mod[i-1]*10 % MOD

    def monotone_diff(root, length, trailing):
        if length + trailing >= k:
            return b_diff_mod(root * pow10[trailing] * root * pow10[trailing])
        p10a = pow10[length]; p10b = 10*p10a
        p10t = pow10[trailing]; p10t2 = p10t*p10t
        p10c = pow10[k - length - trailing - 1]
        p10d = p10b * p10t2
        msb1 = (root*root % p10a) // (p10a//10)
        total = 0
        for d in range(10):
            cand = p10a*d + root
            cs = cand*cand; sq = cs % p10b
            sq_t = sq * p10t2; msb2 = sq // p10a
            if msb2 < msb1:
                dh = b_diff_mod(p10d + sq_t)
                if cs == sq:
                    dl = b_diff_mod(sq_t)
                    m = (p10c - 1) % MOD
                    total = add_mod(total, dl)
                    total = add_mod(total, mul_mod(m, dh))
                else:
                    m = p10c % MOD
                    total = add_mod(total, mul_mod(m, dh))
            else:
                total = add_mod(total, monotone_diff(cand, length+1, trailing))
        return total

    nm = pow10_mod[k]; n1m = (nm + MOD - 1) % MOD; tn1m = (2*nm + MOD - 1) % MOD
    total = mul_mod(mul_mod(mul_mod(nm, n1m), tn1m), INV6)
    for d in range(1, 10):
        for t in range(k):
            total = add_mod(total, monotone_diff(d, 1, t))
    return str(total)

if __name__ == '__main__':
    print(solve())
