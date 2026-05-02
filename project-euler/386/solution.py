def solve():
    N = 100_000_000

    # Build min divisor (SPF) sieve
    spf = [0] * (N + 1)
    spf[1] = 1
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            if i <= N // i:
                for j in range(i*i, N+1, i):
                    if spf[j] == 0:
                        spf[j] = i

    # Compute Omega(n) for each n and group by degree
    degs = [0] * (N + 1)
    by_degs = [[1]]  # degree 0 has {1}
    for i in range(2, N + 1):
        reduced = i // spf[i]
        d = degs[reduced] + 1
        degs[i] = d
        while len(by_degs) <= d:
            by_degs.append([])
        by_degs[d].append(i)

    ans = 0
    for i in range(len(by_degs) - 1):
        cur = by_degs[i]

        # Count pairs within same degree
        low = 0
        high = len(cur) - 1
        while low < len(cur):
            while high >= 0 and cur[high] * cur[low] > N:
                high -= 1
            ans += high + 1
            low += 1

        # Count pairs between consecutive degrees
        nxt = by_degs[i + 1]
        low = 0
        high = len(nxt) - 1
        while low < len(cur):
            while high >= 0 and nxt[high] * cur[low] > N:
                high -= 1
            ans += high + 1
            low += 1

    return str(ans)

if __name__ == '__main__':
    print(solve())
