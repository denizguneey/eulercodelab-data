MOD = 987654319

def mod_inv(a):
    return pow(a, MOD - 2, MOD)

def solve():
    N = 100
    g = [0] * (N + 1)
    g[0] = 1

    for n in range(1, N + 1):
        s = 0
        for i in range(1, n + 1):
            s = (s + g[i - 1] * g[n - i]) % MOD

        H = (n * (2 * n - 1)) % MOD
        invn = mod_inv(n % MOD)
        g[n] = (H * s % MOD) * invn % MOD

    return str(g[N])

if __name__ == "__main__":
    print(solve())
