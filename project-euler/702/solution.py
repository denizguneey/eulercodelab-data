import sys

sys.setrecursionlimit(20000)

cache = {}

def f(x, m):
    x %= m
    if x <= 1:
        return 0
    key = (x, m)
    if key in cache:
        return cache[key]
    
    t = m // x
    y = m % x
    
    term = (t * (t + 1) * x * (x - 1)) // 4
    res = term + (t + 1) * f(x, y) - t * f(x, x - y)
    
    cache[key] = res
    return res

def g(x, m):
    return (m - 1) * (m - 2) - f(x, m)

def solve():
    cache.clear()
    n = 123456789
    
    D = n.bit_length()
    ans = (n * (3 * n + 1) // 2) * (D + 1)
    
    for d in range(2, D + 1):
        ans -= g(n, 1 << d)
        
    ans += 2 * g(n, (1 << D) - n)
    return str(ans)

if __name__ == '__main__':
    print(solve())
