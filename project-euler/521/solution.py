import math

def solve():
    N = 10**12
    MOD = 10**9

    v = math.isqrt(N)

    s_cnt = list(range(v + 1))  # s_cnt[i] = i-1 for i>=1
    for i in range(v + 1):
        s_cnt[i] = i - 1 if i >= 1 else 0
    tri = lambda x: x * (x + 1) // 2 - 1 if x >= 1 else 0
    s_sum = [tri(i) for i in range(v + 1)]
    l_cnt = [0] * (v + 1)
    l_sum = [0] * (v + 1)
    for i in range(1, v + 1):
        q = N // i
        l_cnt[i] = q - 1
        l_sum[i] = q * (q + 1) // 2 - 1

    used = bytearray(v + 1)
    ret = 0

    for p in range(2, v + 1):
        if s_cnt[p] == s_cnt[p - 1]: continue
        p_cnt = s_cnt[p - 1]
        p_sum = s_sum[p - 1]
        q = p * p

        ret += p * (l_cnt[p] - p_cnt)
        l_cnt[1] -= (l_cnt[p] - p_cnt)
        l_sum[1] -= (l_sum[p] - p_sum) * p

        interval = (p & 1) + 1
        end = min(v, N // q)
        i = p + interval
        while i <= end:
            if not used[i]:
                d = i * p
                if d <= v:
                    l_cnt[i] -= (l_cnt[d] - p_cnt)
                    l_sum[i] -= (l_sum[d] - p_sum) * p
                else:
                    t = N // d
                    l_cnt[i] -= (s_cnt[t] - p_cnt)
                    l_sum[i] -= (s_sum[t] - p_sum) * p
            i += interval

        if q <= v:
            step = p * interval
            ii = q
            while ii < end:
                used[ii] = 1
                ii += step

        i = v
        while i >= q:
            t = i // p
            s_cnt[i] -= (s_cnt[t] - p_cnt)
            s_sum[i] -= (s_sum[t] - p_sum) * p
            i -= 1

    ans = (l_sum[1] + ret) % MOD
    return f"{ans:09d}"

if __name__ == '__main__':
    print(solve())
