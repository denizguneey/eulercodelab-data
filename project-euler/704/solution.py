def S_fast(N):
    if N == 0:
        return 0

    K = N.bit_length() - 1
    ans = 0

    for k in range(1, K):
        p2 = 1 << k
        ans += (k - 1) * p2 + 1

    block_start = 1 << K
    M = N - block_start + 1
    A = block_start + 1
    B = N + 1

    sum_min = 0
    for t in range(1, K + 1):
        p2 = 1 << t
        count = (B // p2) - ((A - 1) // p2)
        sum_min += count

    ans += K * M - sum_min
    return ans

def solve():
    N = 10000000000000000
    ans = S_fast(N)
    return str(ans)

if __name__ == '__main__':
    print(solve())
