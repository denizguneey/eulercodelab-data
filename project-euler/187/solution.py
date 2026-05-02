# Problem 187: Semiprimes
# Count composites below 10^8 that are the product of exactly two primes.

def solve():
    limit = 10**8
    max_q = (limit-1)//2
    # Sieve of Eratosthenes
    sieve = bytearray(b'\x01') * (max_q+1)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, int(max_q**0.5)+1):
        if sieve[i]:
            for j in range(i*i, max_q+1, i):
                sieve[j] = 0
    primes = [i for i in range(2, max_q+1) if sieve[i]]

    import bisect
    count = 0
    for i, p in enumerate(primes):
        if p*p >= limit: break
        qmax = (limit-1)//p
        j = bisect.bisect_right(primes, qmax)
        count += j - i
    print(count)

solve()
