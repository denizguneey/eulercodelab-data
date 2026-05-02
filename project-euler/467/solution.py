import math

def solve():
    MOD = 1000000007
    n = 10000

    def digital_root(x): return 1 + (x - 1) % 9

    limit = max(64, int(n * (math.log(n) + math.log(math.log(n))))) + 64
    sieve = bytearray(b'\x01') * (limit + 1); sieve[0] = sieve[1] = 0
    for p in range(2, int(limit**0.5)+1):
        if sieve[p]:
            for j in range(p*p, limit+1, p): sieve[j] = 0

    pd, cd = [], []
    for x in range(2, limit + 1):
        if sieve[x]:
            if len(pd) < n: pd.append(digital_root(x))
        else:
            if len(cd) < n: cd.append(digital_root(x))
        if len(pd) == n and len(cd) == n: break

    # SCS DP
    w = n + 1
    dp = [[0]*w for _ in range(w)]
    for i in range(n, -1, -1):
        for j in range(n, -1, -1):
            if i == n: dp[i][j] = n - j
            elif j == n: dp[i][j] = n - i
            elif pd[i] == cd[j]: dp[i][j] = 1 + dp[i+1][j+1]
            else: dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])

    i, j, result = 0, 0, 0
    while i < n or j < n:
        if i == n: d = cd[j]; j += 1
        elif j == n: d = pd[i]; i += 1
        elif pd[i] == cd[j]: d = pd[i]; i += 1; j += 1
        else:
            da, db = dp[i+1][j], dp[i][j+1]
            if da < db or (da == db and pd[i] < cd[j]):
                d = pd[i]; i += 1
            else: d = cd[j]; j += 1
        result = (result * 10 + d) % MOD

    return str(result)

if __name__ == '__main__':
    print(solve())
