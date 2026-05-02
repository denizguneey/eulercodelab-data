import math

def solve():
    MOD = 1000000007
    N = 100000000000000
    INV2 = 500000004

    limit = int(math.isqrt(N))
    # Sieve Mobius function
    mu = [0] * (limit + 1)
    mu[1] = 1
    is_prime = bytearray(b'\x01') * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > limit: break
            is_prime[i * p] = 0
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]

    def calc_T(x):
        total = 0
        l = 1
        while l <= x:
            r = x // (x // l)
            count = r - l + 1
            sum_lr = l + r
            sum_seq = (count * sum_lr % (2 * MOD) // 2) % MOD
            total = (total + sum_seq * (x // l)) % MOD
            l = r + 1
        return total

    S_N = 0
    for d in range(1, limit + 1):
        if mu[d] == 0: continue
        inner = calc_T(N // (d * d))
        term = d * inner % MOD
        if mu[d] == 1:
            S_N = (S_N + term) % MOD
        else:
            S_N = (S_N - term) % MOD

    n_sum = N % MOD * ((N + 1) % MOD) % MOD * INV2 % MOD
    return str((S_N - n_sum) % MOD)

if __name__ == '__main__':
    print(solve())
