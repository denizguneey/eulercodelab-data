def solve(n=100):
    sum_n = n * (n + 1) // 2
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    return sum_n * sum_n - sum_sq

if __name__ == "__main__":
    assert solve(10) == 2640, "Checkpoint failed for n=10"
    print(solve())
