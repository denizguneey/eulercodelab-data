import math

def F(n, m):
    binom = [[0.0] * (m + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        binom[i][0] = 1.0
        binom[i][i] = 1.0
        for j in range(1, i):
            binom[i][j] = binom[i-1][j-1] + binom[i-1][j]
            
    two_pi = 2.0 * math.pi
    cosine = [math.cos(two_pi * r / n) for r in range(n)]
    
    total = 0.0
    def dfs(idx, rem, mod_sum, count_zero, cos_sum, ways):
        nonlocal total
        if idx == n - 1:
            x = rem
            if (mod_sum + idx * x) % n != 0:
                return
            if count_zero == m:
                return
            
            final_cos = cos_sum + x * cosine[idx]
            denom = 1.0 - final_cos / m
            if denom > 0.0:
                total += ways / denom
            return
            
        for x in range(rem + 1):
            next_count_zero = count_zero
            if idx == 0:
                next_count_zero = x
            dfs(idx + 1, rem - x, (mod_sum + idx * x) % n, next_count_zero,
                cos_sum + x * cosine[idx], ways * binom[rem][x])
                
    dfs(0, m, 0, 0, 0.0, 1.0)
    return total

def G(N, M):
    total = 0.0
    for n in range(2, N + 1):
        for m in range(2, M + 1):
            total += F(n, m)
    return total

def solve():
    answer = G(12, 12)
    return "{:.12e}".format(answer).replace("e+", "e")

if __name__ == "__main__":
    print(solve())
