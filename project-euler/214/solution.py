# Problem 214: Totient Chains
# Sum of primes p < 40,000,000 where the totient chain length is exactly 25.
# Chain: n -> phi(n) -> phi(phi(n)) -> ... -> 1

def solve():
    limit = 40000000
    target = 25

    # Linear sieve to compute phi and find primes
    is_composite = bytearray(limit + 1)
    phi = [0] * (limit + 1)
    primes = []
    phi[1] = 1

    for i in range(2, limit + 1):
        if not is_composite[i]:
            primes.append(i)
            phi[i] = i - 1
        for p in primes:
            if i * p > limit:
                break
            is_composite[i * p] = 1
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            phi[i * p] = phi[i] * (p - 1)

    # Compute chain lengths
    chain = bytearray(limit + 1)
    chain[1] = 1
    for n in range(2, limit + 1):
        chain[n] = chain[phi[n]] + 1

    total = sum(p for p in primes if chain[p] == target)
    print(total)

solve()
