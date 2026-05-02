def solve(limit=4000000):
    a, b = 1, 2
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

if __name__ == "__main__":
    assert solve(100) == 44, "Checkpoint failed for limit=100"
    print(solve())
