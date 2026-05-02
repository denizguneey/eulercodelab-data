MOD = 1000000007

def mod_pow(a, e):
    return pow(a, e, MOD)

def mod_inv(a):
    return pow(a % MOD, MOD - 2, MOD)

def P_formula(n):
    two_n = 2 * n

    fact_n = 1
    fact_2n = 1
    for i in range(1, two_n + 1):
        fact_2n = (fact_2n * i) % MOD
        if i == n:
            fact_n = fact_2n

    inv_fact_n = mod_inv(fact_n)
    c2n_n = (fact_2n * inv_fact_n % MOD * inv_fact_n) % MOD

    inv_n1 = mod_inv(n + 1)
    inv_n2 = mod_inv(n + 2)

    f1 = (c2n_n * inv_n1) % MOD
    c2n_n1 = (c2n_n * (n % MOD) % MOD * inv_n1) % MOD
    f2 = (3 * c2n_n1 % MOD * inv_n2) % MOD

    ans = (f1 * f1) % MOD
    ans = (ans + f2 * f2) % MOD
    return ans

def solve():
    return str(P_formula(100000000))

if __name__ == "__main__":
    print(solve())
