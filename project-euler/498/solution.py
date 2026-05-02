def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def binom_mod_small_prime_digit(n, k, prime):
    if k > n:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1

    numerator = 1
    denominator = 1
    for i in range(1, k + 1):
        numerator = (numerator * (n - k + i)) % prime
        denominator = (denominator * i) % prime
        
    inv_denominator = mod_pow(denominator, prime - 2, prime)
    return (numerator * inv_denominator) % prime

def binom_mod_prime_lucas(n, k, prime):
    if k > n:
        return 0
    result = 1
    nn = n
    kk = k
    while nn > 0 or kk > 0:
        ni = nn % prime
        ki = kk % prime
        if ki > ni:
            return 0
        digit = binom_mod_small_prime_digit(ni, ki, prime)
        result = (result * digit) % prime
        nn //= prime
        kk //= prime
    return result

def coefficient_mod(n, m, d, prime):
    if d >= m or m > n:
        return 0
    first = binom_mod_prime_lucas(n, d, prime)
    second = binom_mod_prime_lucas(n - d - 1, m - d - 1, prime)
    return (first * second) % prime

def solve():
    kPrime = 999999937
    n = 10000000000000
    m = 1000000000000
    d = 10000
    ans = coefficient_mod(n, m, d, kPrime)
    return str(ans)

if __name__ == '__main__':
    print(solve())
