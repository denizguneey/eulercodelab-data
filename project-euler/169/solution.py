# Problem 169: Exploring the number of different ways a number can be expressed
# as a sum of powers of 2, each power used at most twice.

def solve():
    n = 10**25
    memo = {0: 1, -1: 0}
    def f(n):
        if n in memo: return memo[n]
        if n & 1:
            ans = f((n - 1) >> 1)
        else:
            half = n >> 1
            ans = f(half) + f(half - 1)
        memo[n] = ans
        return ans
    print(f(n))

solve()
