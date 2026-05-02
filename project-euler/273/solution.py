def solve():
    PRIMES = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109, 113, 137, 149]
    LIMIT = 150

    reps = [None] * LIMIT
    for i in range(1, LIMIT, 2):
        for j in range(2, LIMIT, 2):
            s = i*i + j*j
            if s < LIMIT:
                reps[s] = (i, j)

    def cmul(a, b):
        return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

    def conj(a):
        return (a[0], -a[1])

    def dfs(idx, value):
        if idx == len(PRIMES):
            a = abs(value[0])
            b = abs(value[1])
            return min(a, b)
        p = PRIMES[idx]
        return (dfs(idx + 1, value) +
                dfs(idx + 1, cmul(value, reps[p])) +
                dfs(idx + 1, cmul(value, conj(reps[p]))))

    total = 0
    for k in range(len(PRIMES)):
        total += dfs(k + 1, reps[PRIMES[k]])
    return str(total)

if __name__ == '__main__':
    print(solve())
