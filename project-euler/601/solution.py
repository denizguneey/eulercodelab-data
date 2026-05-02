import math

def solve():
    S_MAX = 32
    L = [0] * (S_MAX + 1)
    L[0] = 1
    for i in range(1, S_MAX + 1):
        L[i] = L[i-1] * i // math.gcd(L[i-1], i)

    def count_cong1(N, Lv):
        if N <= 2 or Lv == 0: return 0
        x = N - 2
        return x // Lv if Lv <= x else 0

    def P(s, N):
        return count_cong1(N, L[s]) - count_cong1(N, L[s+1])

    ans = 0
    N = 1
    for i in range(1, 32):
        N *= 4
        ans += P(i, N)

    return str(ans)

if __name__ == '__main__':
    print(solve())
