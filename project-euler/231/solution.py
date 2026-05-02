def primes_up_to(n):
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = 0
                
    return [i for i in range(2, n + 1) if is_prime[i]]

def exponent_in_factorial(n, p):
    exp = 0
    x = n
    while x > 0:
        x //= p
        exp += x
    return exp

def solve(n=20000000, k=15000000):
    r = n - k
    primes = primes_up_to(n)
    
    total_sum = 0
    for p in primes:
        exp = exponent_in_factorial(n, p) - exponent_in_factorial(k, p) - exponent_in_factorial(r, p)
        total_sum += p * exp
        
    return str(total_sum)

if __name__ == '__main__':
    print(solve())
