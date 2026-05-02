MOD = 998244353

def mod_pow(a, e):
    r = 1
    while e > 0:
        if e & 1:
            r = (r * a) % MOD
        a = (a * a) % MOD
        e >>= 1
    return r

def T_mod(N):
    U = [0] * (N + 1)
    V = [0] * (N + 1)
    E = [0] * (N + 1)
    E[0] = 1

    for n in range(1, N + 1):
        sum_uv = 0
        sum_uu = 0
        for i in range(n):
            sum_uv = (sum_uv + U[i] * V[n - 1 - i]) % MOD
            sum_uu = (sum_uu + U[i] * U[n - 1 - i]) % MOD

        vn = 1 if n == 1 else 0
        vn = (vn + 9 * sum_uv) % MOD
        V[n] = vn

        un = (V[n - 1] + 9 * sum_uu) % MOD
        U[n] = un

    for n in range(1, N + 1):
        sum_ue = 0
        for i in range(n):
            sum_ue = (sum_ue + U[i] * E[n - 1 - i]) % MOD
        E[n] = (10 * sum_ue) % MOD

    sumE = sum(E[1:]) % MOD

    inv10 = mod_pow(10, MOD - 2)
    return (9 * inv10 % MOD * sumE) % MOD

def solve():
    return str(T_mod(10000))

if __name__ == "__main__":
    print(solve())
