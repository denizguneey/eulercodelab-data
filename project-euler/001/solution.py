def sum_of_multiples_below(limit, divisor):
    n = (limit - 1) // divisor
    return divisor * n * (n + 1) // 2

def solve(limit=1000):
    if limit == 0:
        return 0
    return (sum_of_multiples_below(limit, 3)
            + sum_of_multiples_below(limit, 5)
            - sum_of_multiples_below(limit, 15))

if __name__ == "__main__":
    assert solve(10) == 23, "Checkpoint failed for limit=10"
    print(solve())
