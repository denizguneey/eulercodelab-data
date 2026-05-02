import math
import heapq

def solve():
    POWER = 500500
    MOD = 500500507

    # Generate first POWER primes
    def first_n_primes(n):
        limit = max(20, int(n * (math.log(n) + math.log(math.log(n)))) + 100)
        while True:
            sieve = bytearray([1]) * (limit + 1)
            sieve[0] = sieve[1] = 0
            for p in range(2, int(limit**0.5) + 1):
                if sieve[p]:
                    for q in range(p*p, limit+1, p):
                        sieve[q] = 0
            primes = [i for i in range(2, limit+1) if sieve[i]]
            if len(primes) >= n:
                return primes[:n]
            limit *= 2

    primes = first_n_primes(POWER)
    # Min-heap: (log_value, mod_value)
    heap = [(math.log(p), p % MOD) for p in primes]
    heapq.heapify(heap)

    ans = 1
    for _ in range(POWER):
        log_val, mod_val = heapq.heappop(heap)
        ans = ans * mod_val % MOD
        heapq.heappush(heap, (log_val * 2.0, mod_val * mod_val % MOD))

    return str(ans)

if __name__ == '__main__':
    print(solve())
