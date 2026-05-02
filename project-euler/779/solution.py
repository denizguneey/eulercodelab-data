import decimal

def sieve_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]

def solve():
    decimal.getcontext().prec = 50
    primes = sieve_primes(2000000)
    
    prefix = decimal.Decimal(1)
    f1 = decimal.Decimal(0)
    total = decimal.Decimal(0)
    
    for p_int in primes:
        p = decimal.Decimal(p_int)
        pm1 = p - 1
        
        f1 += prefix / (p * p * pm1)
        total += prefix / (p * pm1 * pm1)
        prefix *= pm1 / p
        
    return f"{total:.12f}"

if __name__ == "__main__":
    print(solve())
