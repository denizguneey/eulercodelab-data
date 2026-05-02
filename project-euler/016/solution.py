def solve(exponent=1000):
    return sum(int(d) for d in str(2 ** exponent))

if __name__ == "__main__":
    assert solve(15) == 26, "Checkpoint failed for exponent=15"
    print(solve())
