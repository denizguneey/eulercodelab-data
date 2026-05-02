MOD = 1000000007
XOR_SIZE = 64

def fwt_xor(a, invert):
    length = 1
    while length < XOR_SIZE:
        for i in range(0, XOR_SIZE, length * 2):
            for j in range(length):
                u = a[i + j]
                v = a[i + j + length]
                x = (u + v) % MOD
                y = (u - v) % MOD
                a[i + j] = x
                a[i + j + length] = y
        length *= 2
    
    if invert:
        inv2 = (MOD + 1) // 2
        length = 1
        while length < XOR_SIZE:
            for i in range(0, XOR_SIZE, length * 2):
                for j in range(length):
                    a[i + j] = (a[i + j] * inv2) % MOD
                    a[i + j + length] = (a[i + j + length] * inv2) % MOD
            length *= 2

def compute_R(m, w):
    maxD = w - 2
    D = 2 * maxD + 1
    S = 2 * maxD * m + 1
    offset = maxD * m

    f = [[0] * XOR_SIZE for _ in range(D)]

    for a in range(1, w - 1):
        for b in range(1, w - a):
            maxk = w - a - b
            d_idx = b - a + maxD
            for g in range(maxk):
                f[d_idx][g] = (f[d_idx][g] + 1) % MOD

    for d in range(D):
        fwt_xor(f[d], False)

    dp = [[0] * XOR_SIZE for _ in range(S)]
    dp[offset][0] = 1

    delta = [d - maxD for d in range(D)]

    for step in range(m):
        dp_hat = [row[:] for row in dp]
        for s in range(S):
            fwt_xor(dp_hat[s], False)

        new_hat = [[0] * XOR_SIZE for _ in range(S)]

        for freq in range(XOR_SIZE):
            for sd in range(S):
                acc = 0
                for d in range(D):
                    sd_prev = sd - delta[d]
                    if 0 <= sd_prev < S:
                        acc = (acc + dp_hat[sd_prev][freq] * f[d][freq]) % MOD
                new_hat[sd][freq] = acc

        new_dp = new_hat
        for s in range(S):
            fwt_xor(new_dp[s], True)
        dp = new_dp

    ans = 0
    for sd in range(S):
        sum_d = sd - offset
        row_sum = sum(dp[sd]) % MOD
        if sum_d > 0:
            ans = (ans + row_sum) % MOD
        elif sum_d == 0:
            zero = dp[sd][0]
            add = (row_sum - zero) % MOD
            ans = (ans + add) % MOD

    return ans % MOD

def solve():
    return str(compute_R(8, 64))

if __name__ == "__main__":
    print(solve())
