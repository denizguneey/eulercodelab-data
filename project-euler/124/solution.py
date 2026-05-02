# Problem 124: Ordered radicals
# Sort 1..100000 by rad(n), then by n. Find E(10000).

def solve():
    limit = 100000
    rad = [1] * (limit + 1)
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if not is_prime[p]: continue
        for m in range(p, limit + 1, p):
            rad[m] *= p
            if m > p: is_prime[m] = False
    
    values = sorted(range(1, limit + 1), key=lambda n: (rad[n], n))
    print(values[9999])  # E(10000), 0-indexed

solve()
