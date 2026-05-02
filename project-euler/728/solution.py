import math

def solve():
    MOD = 1000000007
    N = 10000000

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    phi = list(range(N + 1))
    primes = []
    for i in range(2, N + 1):
        if phi[i] == i: phi[i] = i - 1; primes.append(i)
        for p in primes:
            if i * p > N: break
            if i % p == 0: phi[i * p] = phi[i] * p; break
            phi[i * p] = phi[i] * (p - 1)

    pow2 = [1] * (N + 1)
    for i in range(1, N + 1): pow2[i] = pow2[i-1] * 2 % MOD

    ans = 2 * N % MOD  # h=1

    def v2(x):
        c = 0
        while x & 1 == 0: x >>= 1; c += 1
        return c

    for h in range(2, N + 1):
        if h & 1:
            coeff = 3 * (phi[h] // 2) % MOD
        else:
            coeff = 2 * phi[h] % MOD
        step = h - 1; count = N // h
        exp = step
        for i in range(count):
            ans = (ans + coeff * pow2[exp]) % MOD
            exp += step

    return str(ans)

if __name__ == '__main__':
    print(solve())
