def solve():
    T = lambda n: n * (n + 1)
    H = lambda n: T(n * n * (n + 1))
    U = lambda n: T(H(n))
    
    n = U(1)
    value = U(n)
    ans = value % 1000000000
    return str(ans)

if __name__ == "__main__":
    print(solve())
