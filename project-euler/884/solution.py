import sys

sys.setrecursionlimit(2000000)

def floor_cuberoot(x):
    y = int(x ** (1.0/3.0))
    k = y
    while (k + 1) ** 3 <= x:
        k += 1
    while k ** 3 > x:
        k -= 1
    return k

def S_fast(N):
    if N <= 1:
        return 0

    K = floor_cuberoot(N - 1)
    A = [0] * (K + 1)
    
    memo = {}
    memo[0] = 0
    memo[1] = 0

    def solve(x, ready_k):
        if x <= 1:
            return 0
        if x in memo:
            return memo[x]

        k = floor_cuberoot(x - 1)
        c = k ** 3
        t = x - c

        ans = A[k] + t + solve(t, ready_k)
        memo[x] = ans
        return ans

    for k in range(1, K):
        delta = 3 * k * k + 3 * k + 1
        sdelta = solve(delta, k)
        A[k + 1] = A[k] + delta + sdelta
        memo[(k + 1) ** 3] = A[k + 1]

    return solve(N, K)

def solve():
    return str(S_fast(10**17))

if __name__ == "__main__":
    print(solve())
