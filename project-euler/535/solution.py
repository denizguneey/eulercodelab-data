import math
import sys

sys.setrecursionlimit(20000)

kMod = 1000000000

def isqrt(x):
    r = int(math.sqrt(x))
    while (r + 1) * (r + 1) <= x:
        r += 1
    while r * r > x:
        r -= 1
    return r

def sum_floor_sqrt(n):
    s = isqrt(n)
    nn1 = n + 1
    sumsq = s * (s + 1) * (2 * s + 1) // 6
    return s * nn1 - sumsq

def tri_mod(n):
    t = n * (n + 1) // 2
    return t % kMod

memoA = {0: 0}
memoU = {0: 0}
memoTmod = {0: 0}

def U(k):
    if k in memoU:
        return memoU[k]
    a = A(k)
    c = k - a
    res = U(a) + sum_floor_sqrt(c)
    memoU[k] = res
    return res

def A(n):
    if n in memoA:
        return memoA[n]
    if n <= 1:
        memoA[n] = 0
        return 0
        
    def f(k):
        return k + U(k)
        
    hi_max = n - 1
    lo = 0
    hi = 1
    
    while hi < hi_max and f(hi) <= n:
        lo = hi
        hi = min(hi * 2, hi_max)
        
    if f(hi) <= n:
        memoA[n] = hi
        return hi
        
    while lo + 1 < hi:
        mid = lo + (hi - lo) // 2
        if f(mid) <= n:
            lo = mid
        else:
            hi = mid
            
    memoA[n] = lo
    return lo

def T_mod(n):
    if n in memoTmod:
        return memoTmod[n]
    a = A(n)
    c = n - a
    res = (T_mod(a) + tri_mod(c)) % kMod
    memoTmod[n] = res
    return res

def solve():
    n = 1000000000000000000
    ans = T_mod(n)
    return f"{ans:09d}"

if __name__ == '__main__':
    print(solve())
