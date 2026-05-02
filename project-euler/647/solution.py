import math

def isqrt_floor(n):
    if n < 0: return 0
    return math.isqrt(n)

def floor_sqrt(n):
    if n < 0: return 0
    r = math.isqrt(n)
    while (r + 1)**2 <= n: r += 1
    while r**2 > n: r -= 1
    return r

def Fk(k, N):
    if (k & 1) == 0 or k < 3: return 0
    d = k - 2
    c = (k - 4) * (k - 4)
    
    sqrtN = isqrt_floor(N)
    if sqrtN <= 1: return 0
    
    tA = (sqrtN - 1) // (2 * d)
    
    M = (2 * N) // c
    disc = 1 + 4 * d * M
    s = floor_sqrt(disc)
    tB = (s - 1) // (2 * d) if s > 0 else 0
    
    T = min(tA, tB)
    if T == 0: return 0
    
    TT = T
    S1 = TT * (TT + 1) // 2
    S2 = TT * (TT + 1) * (2 * TT + 1) // 6
    
    sumA = TT + 4 * d * S1 + 4 * d * d * S2
    sum_dt2_t = d * S2 + S1
    sumB = c * (sum_dt2_t // 2)
    return sumA + sumB

def sum_all(N):
    ans = 0
    k = 3
    while True:
        d = k - 2
        c = (k - 4) * (k - 4)
        A1 = (2 * k - 3) * (2 * k - 3)
        B1 = c * (k - 1) // 2
        if A1 > N or B1 > N: break
        ans += Fk(k, N)
        k += 2
    return ans

def solve():
    N = 1000000000000
    ans = sum_all(N)
    return str(ans)

if __name__ == '__main__':
    print(solve())
