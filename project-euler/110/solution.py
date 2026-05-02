# Problem 110: Diophantine reciprocals II
# Find the least n such that 1/x + 1/y = 1/n has more than 4 million solutions.

def solve():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    target = 2 * 4000000 + 1
    best = float('inf')
    
    def dfs(idx, max_exp, n, divisor_count):
        nonlocal best
        if divisor_count >= target:
            best = min(best, n)
            return
        if idx >= len(primes):
            return
        val = n
        for e in range(1, max_exp + 1):
            val *= primes[idx]
            if val >= best:
                break
            dfs(idx + 1, e, val, divisor_count * (2 * e + 1))
    
    dfs(0, 63, 1, 1)
    print(best)

solve()
