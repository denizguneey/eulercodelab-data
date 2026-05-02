def solve():
    n = 20000
    N = n - 1
    inv = [0.0]*(N+1)
    for i in range(1, N+1): inv[i] = 1.0/i

    G = [0.0]*(N+1); G[0] = 1.0
    for m in range(1, N+1):
        term = 1.0; s = 1.0
        for c in range(1, m+1):
            term *= (m-c+1)*inv[N-c+1]; s += term
        G[m] = s

    total = 0.0
    for a in range(N+1):
        f = 1.0; mb = N - a
        for b in range(mb+1):
            m = N - a - b; total += f * G[m]
            if b < mb: f *= (N-a-b)*inv[N-b]

    return f'{total / (n*n):.10f}'

if __name__ == '__main__':
    print(solve())
