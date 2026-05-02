import heapq

def solve():
    LIMIT = 10_000_000

    # Sieve of Eratosthenes
    is_prime = bytearray([1]) * (LIMIT + 1)
    is_prime[0] = is_prime[1] = 0
    for p in range(2, int(LIMIT**0.5) + 1):
        if is_prime[p]:
            for q in range(p*p, LIMIT+1, p):
                is_prime[q] = 0

    pow10 = [1]
    while pow10[-1] <= LIMIT // 10:
        pow10.append(pow10[-1] * 10)

    INF = float('inf')
    best = [INF] * (LIMIT + 1)
    best[2] = 2
    pq = [(2, 2)]

    while pq:
        cost, p = heapq.heappop(pq)
        if cost != best[p]: continue

        ln = 1
        while ln < len(pow10) and p >= pow10[ln]:
            ln += 1

        # Change one digit
        for pos in range(ln):
            place = pow10[pos]
            old_d = (p // place) % 10
            for d in range(10):
                if d == old_d: continue
                if pos == ln - 1 and d == 0: continue
                v = p + (d - old_d) * place
                if 2 <= v <= LIMIT and is_prime[v]:
                    cand = max(cost, v)
                    if cand < best[v]:
                        best[v] = cand
                        heapq.heappush(pq, (cand, v))

        # Remove leading digit
        if ln > 1:
            v = p % pow10[ln - 1]
            if 2 <= v <= LIMIT and is_prime[v]:
                cand = max(cost, v)
                if cand < best[v]:
                    best[v] = cand
                    heapq.heappush(pq, (cand, v))

        # Prepend digit
        if ln < len(pow10):
            base = pow10[ln]
            for d in range(1, 10):
                v = d * base + p
                if v > LIMIT: break
                if is_prime[v]:
                    cand = max(cost, v)
                    if cand < best[v]:
                        best[v] = cand
                        heapq.heappush(pq, (cand, v))

    ans = sum(p for p in range(2, LIMIT+1) if is_prime[p] and best[p] > p)
    return str(ans)

if __name__ == '__main__':
    print(solve())
