def solve():
    MOD = 1000000007
    INV2 = (MOD + 1) // 2
    N = 10000000000000000

    ans = 0
    k = 1
    while True:
        c = k * (k - 1) // 2
        if c >= N: break
        M = N - c; q = M // k; r = M % k
        t1 = k % MOD * (q % MOD) % MOD * ((q - 1) % MOD) % MOD * INV2 % MOD
        t2 = q % MOD * ((r + 1) % MOD) % MOD
        ans = (ans + t1 + t2) % MOD
        k += 1

    return str(ans)

if __name__ == '__main__':
    print(solve())
