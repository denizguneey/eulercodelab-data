def solve():
    n = 12345678; m = 12345
    # Euler totient sieve
    phi = list(range(n+1))
    for p in range(2, n+1):
        if phi[p] == p:
            for j in range(p, n+1, p): phi[j] -= phi[j]//p
    # Expected error
    p = (n-m)/n; total = phi[1]*p
    for k in range(1, n-m):
        p *= (n-k-m)/(n-k)
        total += phi[k+1]*p
    return f"{total:.6f}"

if __name__ == '__main__':
    print(solve())
