MOD = 1000000007
X = 256

def partitions_mod(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for s in range(1, n + 1):
        for sum_val in range(s, n + 1):
            dp[sum_val] = (dp[sum_val] + dp[sum_val - s]) % MOD
    return dp

def losing_partitions_xor0(n, sg):
    dp = [[0] * X for _ in range(n + 1)]
    dp[0][0] = 1
    for s in range(1, n + 1):
        g = sg[s]
        for sum_val in range(s, n + 1):
            cur = dp[sum_val]
            prev = dp[sum_val - s]
            for x in range(X):
                cur[x ^ g] = (cur[x ^ g] + prev[x]) % MOD
    return dp[n][0]

def sg_k2(n):
    sg = [0] * (n + 1)
    for s in range(2, n + 1):
        sg[s] = 1 if s % 2 == 0 else 0
    return sg

def sg_k3(n):
    sg = [0] * (n + 1)
    for s in range(2, n + 1):
        seen = [False] * X
        for a in range(1, s):
            seen[sg[a] ^ sg[s - a]] = True
        for a in range(1, s - 1):
            for b in range(1, s - a):
                c = s - a - b
                seen[sg[a] ^ sg[b] ^ sg[c]] = True
        g = 0
        while g < X and seen[g]:
            g += 1
        sg[s] = g
    return sg

def sg_k4(n):
    sg = [0] * (n + 1)
    for s in range(2, n + 1):
        sg[s] = s - 1
    return sg

def f(n, sg, partitions_n):
    losing = losing_partitions_xor0(n, sg)
    return (partitions_n - losing + MOD) % MOD

def g(n):
    if n < 2: return 0
    part = partitions_mod(n)
    Pn = part[n]
    
    sg2 = sg_k2(n)
    sg3 = sg_k3(n)
    sg4 = sg_k4(n)
    
    f2 = f(n, sg2, Pn)
    ans = f2
    if n >= 3:
        ans = (ans + f(n, sg3, Pn)) % MOD
    if n >= 4:
        ans = (ans + (n - 3) * f(n, sg4, Pn)) % MOD
    return ans

def solve():
    return str(g(200))

if __name__ == '__main__':
    print(solve())
