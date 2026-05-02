def solve(limit=2000000):
    if limit <= 2:
        return 0
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p < limit:
        if is_prime[p]:
            for q in range(p * p, limit, p):
                is_prime[q] = False
        p += 1
    return sum(p for p in range(2, limit) if is_prime[p])

if __name__ == "__main__":
    assert solve(10) == 17, "Checkpoint failed for limit=10"
    print(solve())
