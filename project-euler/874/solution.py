import math
import heapq

def first_primes(count):
    if count <= 0:
        return []
    if count < 6:
        limit = 15
    else:
        n = float(count)
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 32

    while True:
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(math.isqrt(limit)) + 1):
            if is_prime[i]:
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        
        primes = []
        for x in range(2, limit + 1):
            if is_prime[x]:
                primes.append(x)
                if len(primes) >= count:
                    return primes
        limit *= 2

def maximal_score_fast(k, n, primes):
    top = primes[k - 1]
    loss = [0] * k
    for d in range(1, k):
        loss[d] = top - primes[k - 1 - d]

    residue = (k - (n % k)) % k

    INF = float('inf')
    dist = [INF] * k
    pq = []

    dist[0] = 0
    heapq.heappush(pq, (0, 0))

    while pq:
        du, u = heapq.heappop(pq)
        if du != dist[u]:
            continue

        for d in range(1, k):
            v = u + d
            if v >= k:
                v -= k
            nd = du + loss[d]
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return n * top - dist[residue]

def solve():
    k = 7000
    primes = first_primes(k + 1)
    n = primes[k]
    return str(maximal_score_fast(k, n, primes))

if __name__ == "__main__":
    print(solve())
