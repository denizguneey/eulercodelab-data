def solve():
    MOD = 1000000000
    n = 20000

    def mod_norm(v):
        return v % MOD

    def series_divide(num, den, degree):
        out = [0] * (degree + 1)
        out[0] = num[0] % MOD
        for i in range(1, degree + 1):
            acc = num[i] if i < len(num) else 0
            for j in range(1, i + 1):
                if j < len(den): acc -= den[j] * out[i-j]
            out[i] = mod_norm(acc)
        return out

    def compute_F2(degree):
        den = [0] * (degree + 1)
        num = [0] * (degree + 1)
        invprod = [0] * (degree + 1)
        invprod[0] = 1
        for nn in range(10000):
            eD = nn * (nn + 1); eN = nn * (nn + 2)
            if eD > degree and eN > degree: break
            neg = nn & 1
            if eD <= degree:
                for i in range(degree - eD + 1):
                    v = invprod[i]
                    if not neg: den[i+eD] = (den[i+eD] + v) % MOD
                    else: den[i+eD] = (den[i+eD] - v) % MOD
            if eN <= degree:
                for i in range(degree - eN + 1):
                    v = invprod[i]
                    if not neg: num[i+eN] = (num[i+eN] + v) % MOD
                    else: num[i+eN] = (num[i+eN] - v) % MOD
            nxt = nn + 1
            for t in range(nxt, degree + 1):
                invprod[t] = (invprod[t] + invprod[t-nxt]) % MOD
        return series_divide(num, den, degree)

    def compute_t(f2, degree):
        A = [(2 * f2[i]) % MOD for i in range(degree + 1)]
        A[0] = (A[0] - 1) % MOD
        den = [0] * (degree + 1); num = [0] * (degree + 1)
        den[0] = 1
        for i in range(1, degree + 1):
            den[i] = (-2 * A[i-1]) % MOD
            num[i] = A[i-1]
        return series_divide(num, den, degree)

    f2 = compute_F2(n)
    t = compute_t(f2, n)
    return str(3 * t[n] % MOD).zfill(9)

if __name__ == '__main__':
    print(solve())
