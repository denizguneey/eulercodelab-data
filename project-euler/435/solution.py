def solve():
    MOD = 1307674368000
    n = 1000000000000000
    x_max = 100

    def mat_mul(a, b):
        c = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for k in range(3):
                if a[i][k] == 0:
                    continue
                aik = a[i][k]
                for j in range(3):
                    if b[k][j] == 0:
                        continue
                    c[i][j] = (c[i][j] + aik * b[k][j]) % MOD
        return c

    def mat_vec_mul(a, v):
        out = [0] * 3
        for i in range(3):
            val = 0
            for j in range(3):
                if a[i][j] != 0 and v[j] != 0:
                    val = (val + a[i][j] * v[j]) % MOD
            out[i] = val
        return out

    def mat_pow(base, exp):
        result = [[0] * 3 for _ in range(3)]
        for i in range(3):
            result[i][i] = 1
        e = exp
        while e > 0:
            if e & 1:
                result = mat_mul(base, result)
            e >>= 1
            if e > 0:
                base = mat_mul(base, base)
        return result

    def f_value(x_raw):
        if n == 0:
            return 0
        x = x_raw % MOD
        x2 = (x * x) % MOD
        t = [
            [x, x2, 0],
            [1, 0, 0],
            [x, x2, 1]
        ]
        v1 = [x, 0, x]
        p = mat_pow(t, n - 1)
        vn = mat_vec_mul(p, v1)
        return vn[2]

    ans = 0
    for x in range(x_max + 1):
        ans = (ans + f_value(x)) % MOD

    return str(ans)

if __name__ == '__main__':
    print(solve())
