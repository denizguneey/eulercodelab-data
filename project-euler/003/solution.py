def solve(n=600851475143):
    largest = 0
    while n % 2 == 0:
        largest = 2
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            largest = d
            n //= d
        d += 2
    if n > 1:
        largest = n
    return largest

if __name__ == "__main__":
    assert solve(13195) == 29, "Checkpoint failed for n=13195"
    print(solve())
