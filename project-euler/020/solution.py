from math import factorial

def solve(n=100):
    return sum(int(d) for d in str(factorial(n)))

if __name__ == "__main__":
    assert solve(10) == 27, "Checkpoint failed for n=10"
    print(solve())
