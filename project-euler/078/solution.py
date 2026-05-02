# Problem 78: Coin partitions
# Find the least value of n for which the number of ways to partition n
# is divisible by one million.

def solve():
    MOD = 1000000
    p = [1]
    for n in range(1, 100000):
        val = 0
        for k in range(1, n + 1):
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > n:
                break
            sign = 1 if k % 2 == 1 else -1
            val += sign * p[n - g1]
            if g2 <= n:
                val += sign * p[n - g2]
        p.append(val % MOD)
        if p[-1] == 0:
            print(n)
            return

solve()
