import math

MOD = 1000000007

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def is_prime_small(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

def sum_powers_mod(n, k):
    if n == 0:
        return 0

    d = k + 2
    y = [0] * d
    for i in range(1, d):
        y[i] = (y[i - 1] + mod_pow(i, k)) % MOD

    x = n % MOD
    if x < d:
        return y[x]

    fact = [1] * d
    inv_fact = [1] * d
    for i in range(1, d):
        fact[i] = (fact[i - 1] * i) % MOD
        
    inv_fact[d - 1] = pow(fact[d - 1], MOD - 2, MOD)
    for i in range(d - 1, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % MOD

    prefix = [1] * (d + 1)
    suffix = [1] * (d + 1)

    for i in range(d):
        term = (x - i) % MOD
        prefix[i + 1] = (prefix[i] * term) % MOD
        
    for i in range(d - 1, -1, -1):
        term = (x - i) % MOD
        suffix[i] = (suffix[i + 1] * term) % MOD

    answer = 0
    for i in range(d):
        numerator = (prefix[i] * suffix[i + 1]) % MOD
        denominator = (inv_fact[i] * inv_fact[d - 1 - i]) % MOD
        if (d - 1 - i) % 2 == 1:
            denominator = (MOD - denominator) % MOD

        add = (y[i] * numerator % MOD) * denominator % MOD
        answer = (answer + add) % MOD

    return answer

def solve_prefix(n):
    if n == 0:
        return 0

    answer = 0
    primorial = 1
    primorial_mod = 1
    factorial_mod = 1

    m = 0
    while True:
        if m >= 2 and is_prime_small(m):
            primorial *= m
            primorial_mod = (primorial_mod * m) % MOD

        if m > 0:
            factorial_mod = (factorial_mod * m) % MOD

        if m > n:
            break
            
        remaining = n - m
        if primorial > remaining:
            break

        count = remaining // primorial

        coefficient = (mod_pow(primorial_mod, m) * pow(factorial_mod, MOD - 2, MOD)) % MOD
        if m % 2 == 1:
            coefficient = (MOD - coefficient) % MOD

        power_sum = sum_powers_mod(count, m)
        add = (coefficient * power_sum) % MOD

        answer = (answer + add) % MOD
        m += 1

    return answer

def direct_s(n):
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i

    total = 0
    for t in range(1, n + 1):
        m = n - t
        numerator = 1
        for _ in range(m):
            numerator *= t
        if m % 2 == 1:
            numerator = -numerator

        denominator = factorial[m]
        if numerator % denominator == 0:
            total += numerator // denominator

    return total

def run_checkpoints():
    assert direct_s(1) == 1
    assert direct_s(3) == -1

    prefix = 0
    for n in range(1, 11):
        prefix += direct_s(n)
    assert prefix == 43
    assert solve_prefix(10) == 43

    for limit in [20, 30, 40]:
        direct_prefix = 0
        for n in range(1, limit + 1):
            direct_prefix += direct_s(n)

        fast = solve_prefix(limit)
        slow = direct_prefix % MOD
        assert fast == slow

def solve():
    target = 1000000000000000000
    return str(solve_prefix(target))

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
