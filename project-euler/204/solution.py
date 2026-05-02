# Problem 204: Generalised Hamming Numbers
# Count 100-smooth numbers (Hamming) up to 10^9.

def solve():
    limit = 10**9
    type_n = 100
    # Sieve primes up to type_n
    sieve = [True] * (type_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(type_n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, type_n+1, i):
                sieve[j] = False
    primes = [i for i in range(2, type_n+1) if sieve[i]]

    count = 0
    def dfs(idx, val):
        nonlocal count
        if idx == len(primes):
            count += 1
            return
        p = primes[idx]
        x = val
        while True:
            dfs(idx + 1, x)
            if x > limit // p:
                break
            x *= p
    dfs(0, 1)
    print(count)

solve()
