def solve():
    MOD = 1_000_000_033
    N = 100

    def add_mod(a, b): return (a + b) % MOD
    def sub_mod(a, b): return (a - b) % MOD
    def mul_mod(a, b): return a * b % MOD

    # Build binomials
    binom = [[0]*(N+1) for _ in range(N+1)]
    binom[0][0] = 1
    for n in range(1, N+1):
        binom[n][0] = 1
        binom[n][n] = 1
        for k in range(1, n):
            binom[n][k] = add_mod(binom[n-1][k-1], binom[n-1][k])

    # Build powers of 2
    pow2 = [0] * (N*N + 1)
    pow2[0] = 1
    for e in range(1, N*N+1):
        pow2[e] = add_mod(pow2[e-1], pow2[e-1])

    r = [[0]*(N+1) for _ in range(N+1)]
    r[1][0] = 1

    for m in range(1, N+1):
        # Compute base from previous rows
        base = [0] * (N + 1)
        for i in range(1, m):
            choose_rows = binom[m-1][i-1]
            delta = m - i
            for n in range(1, N+1):
                inner = 0
                for j in range(n+1):
                    term = mul_mod(mul_mod(binom[n][j], r[i][j]), pow2[delta*(n-j)])
                    inner = add_mod(inner, term)
                base[n] = add_mod(base[n], mul_mod(choose_rows, inner))

        for n in range(1, N+1):
            same_row = 0
            for j in range(n):
                same_row = add_mod(same_row, mul_mod(binom[n][j], r[m][j]))
            value = pow2[m * n]
            value = sub_mod(value, base[n])
            value = sub_mod(value, same_row)
            r[m][n] = value

    total = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            total = add_mod(total, r[i][j])

    return str(total)

if __name__ == '__main__':
    print(solve())
