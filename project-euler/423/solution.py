def solve():
    MOD = 1000000007
    limit = 50000000

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD
            exp >>= 1
        return r

    # Sieve primes
    is_prime = bytearray(b'\x01') * (limit + 2)
    is_prime[0] = is_prime[1] = 0
    for p in range(2, int((limit+1)**0.5) + 1):
        if is_prime[p]:
            for q in range(p*p, limit+2, p): is_prime[q] = 0

    # Modular inverses
    inv = [0] * (limit + 3)
    inv[1] = 1
    for i in range(2, limit + 3):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD

    inv5 = mod_pow(5, MOD - 2)
    t = 0; p = 1; bt = 1; bt1 = 0
    answer = 0
    for n in range(1, limit + 1):
        c_n = 6 * p % MOD
        answer = (answer + c_n) % MOD
        if n == limit: break
        next_prime = is_prime[n + 1]
        if not next_prime:
            p_next = (6 * p + MOD - bt) % MOD
            bt_m1 = 0
            if t > 0:
                bt_m1 = bt * (5 * t % MOD) % MOD * inv[n - t] % MOD
            bt_next = (5 * bt + bt_m1) % MOD
            bt1_next = (5 * bt1 + bt) % MOD
        else:
            p_next = (6 * p + 5 * bt1) % MOD
            bt2 = 0
            if t + 2 <= n - 1:
                bt2 = bt1 * (n - t - 2) % MOD * inv5 % MOD * inv[t + 2] % MOD
            bt_next = (5 * bt1 + bt) % MOD
            bt1_next = (5 * bt2 + bt1) % MOD
            t += 1
        p, bt, bt1 = p_next, bt_next, bt1_next

    return str(answer)

if __name__ == '__main__':
    print(solve())
