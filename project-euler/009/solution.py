def solve(target_sum=1000):
    for a in range(1, target_sum):
        for b in range(a + 1, target_sum):
            c = target_sum - a - b
            if c <= b:
                continue
            if a * a + b * b == c * c:
                return a * b * c
    return 0

if __name__ == "__main__":
    assert solve(12) == 60, "Checkpoint failed for sum=12"
    print(solve())
