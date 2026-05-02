def solve():
    N = 1000000000000000000; B = 120

    is_prime = [True]*(B+1); is_prime[0] = is_prime[1] = False
    for i in range(2, int(B**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, B+1, i): is_prime[j] = False
    primes = [p for p in range(2, B+1) if is_prime[p] and p != 3]

    max_a = sum(1 for p in primes if p%3 == 1)
    max_b = sum(1 for p in primes if p%3 == 2)

    # Build binomial
    dim = max(max_a, max_b)
    c = [[0]*(dim+1) for _ in range(dim+1)]
    for i in range(dim+1):
        c[i][0] = 1
        for j in range(1, i+1): c[i][j] = c[i-1][j-1] + c[i-1][j]

    w = [[0]*(max_b+1) for _ in range(max_a+1)]
    for a in range(max_a+1):
        for b in range(max_b+1):
            v = 0
            for i in range(a+1):
                for j in range(b+1):
                    if (i + 2*j) % 3 != 0: continue
                    term = c[a][i] * c[b][j]
                    if (i+j) & 1: term = -term
                    v += term
            if (a+b) & 1: v = -v
            w[a][b] = v

    answer = 0
    def dfs(idx, prod, ca, cb):
        nonlocal answer
        if idx == len(primes):
            wt = w[ca][cb]
            if wt >= 0: answer += wt * (N // prod)
            else: answer -= (-wt) * (N // prod)
            return
        dfs(idx+1, prod, ca, cb)
        p = primes[idx]
        if prod <= N // p:
            if p % 3 == 1: dfs(idx+1, prod*p, ca+1, cb)
            else: dfs(idx+1, prod*p, ca, cb+1)

    dfs(0, 1, 0, 0)
    return str(answer)

if __name__ == '__main__':
    print(solve())
