def solve():
    MOD = 1020340567; N = 10000000
    # Linear sieve for Mobius
    lp = [0]*(N+1); primes = []; mu = [0]*(N+1); mu[1] = 1
    for i in range(2, N+1):
        if lp[i] == 0: lp[i] = i; primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > N: break
            lp[i*p] = p
            if p == lp[i]: mu[i*p] = 0; break
            mu[i*p] = -mu[i]
    pmu = [0]*(N+1)
    for i in range(1, N+1): pmu[i] = pmu[i-1] + mu[i]
    pw2 = [1]*(N+1)
    for i in range(1, N+1): pw2[i] = pw2[i-1]*2 % MOD
    ans = 0; i = 1
    while i <= N:
        q = N//i; j = N//q
        bm = (pmu[j] - pmu[i-1]) % MOD
        ans = (ans + bm * pw2[q]) % MOD; i = j+1
    return str(ans % MOD)

if __name__ == '__main__':
    print(solve())
