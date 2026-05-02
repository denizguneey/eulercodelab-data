# Problem 160: Factorial trailing digits
# Find the last 5 non-zero digits of 10^12!

def solve():
    MOD = 100000
    M2 = 3125
    PHI_M2 = 2500
    
    def power(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result
    
    # Build P_table: product of integers 1..M2 coprime to 5, mod 3125
    P_table = [0] * (M2 + 1)
    P_table[0] = 1
    for i in range(1, M2 + 1):
        if i % 5 != 0:
            P_table[i] = (P_table[i-1] * i) % M2
        else:
            P_table[i] = P_table[i-1]
    
    def get_P_mod_3125(n):
        q = n // M2
        r = n % M2
        res = 1 if q % 2 == 0 else (M2 - 1)
        return (res * P_table[r]) % M2
    
    def factorial_no_5_mod_3125(n):
        if n == 0: return 1
        return (get_P_mod_3125(n) * factorial_no_5_mod_3125(n // 5)) % M2
    
    def count_factors_5(n):
        count = 0
        while n > 0:
            count += n // 5
            n //= 5
        return count
    
    def solve_crt(res3125):
        inv21 = 29  # 21^(-1) mod 32
        target = (32 - (res3125 % 32)) % 32
        k = (target * inv21) % 32
        return res3125 + k * M2
    
    def f(n):
        if n < 10:
            res = 1
            for i in range(1, n + 1):
                res *= i
            while res % 10 == 0:
                res //= 10
            return res % MOD
        
        fact_no_5 = factorial_no_5_mod_3125(n)
        num_5s = count_factors_5(n)
        two_exp = num_5s % PHI_M2
        inv_2 = power(2, PHI_M2 - two_exp, M2)
        res3125 = (fact_no_5 * inv_2) % M2
        return solve_crt(res3125)
    
    N = 10**12
    result = f(N)
    print(f"{result:05d}")

solve()
