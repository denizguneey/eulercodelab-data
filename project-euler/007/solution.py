import math

def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
    return [p for p in range(2, limit + 1) if is_prime[p]]

def solve(index=10001):
    if index == 1:
        return 2
    upper = 64
    if index >= 6:
        n = float(index)
        upper = int(n * (math.log(n) + math.log(math.log(n)))) + 16
    while True:
        primes = sieve_primes(upper)
        if len(primes) >= index:
            return primes[index - 1]
        upper *= 2

if __name__ == "__main__":
    assert solve(6) == 13, "Checkpoint failed for index=6"
    print(solve())
