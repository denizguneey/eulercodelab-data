import math

def solve():
    n = 10000000; K = 100000
    MOD_S = 10007; PHI = MOD_S - 1; VMAX = 20013

    def powmod(a, e, m):
        r = 1; a %= m
        while e > 0:
            if e & 1: r = r * a % m
            a = a * a % m; e >>= 1
        return r

    # Sieve primes up to nth_prime upper bound
    bound = int(n * (math.log(n) + math.log(math.log(n)))) + 200
    sieve = bytearray(b'\x01') * ((bound >> 1) + 1)
    for p in range(3, int(bound**0.5)+1, 2):
        if sieve[p >> 1]:
            for x in range(p*p, bound+1, 2*p): sieve[x >> 1] = 0

    # Fenwick tree for order statistics
    bit = [0] * (VMAX + 1)
    def fw_add(idx, d):
        idx += 1
        while idx <= VMAX: bit[idx] += d; idx += idx & (-idx)
    def fw_kth(k):
        idx = 0; step = 1
        while step * 2 <= VMAX: step *= 2
        while step:
            nxt = idx + step
            if nxt <= VMAX and bit[nxt] < k:
                idx = nxt; k -= bit[nxt]
            step >>= 1
        return idx

    Sfirst = [0] * 1002
    ring = [0] * K; ptr = 0; k = 0
    sum2 = 0

    def add_median():
        nonlocal sum2
        if K & 1:
            sum2 += 2 * fw_kth((K+1)//2)
        else:
            sum2 += fw_kth(K//2) + fw_kth(K//2+1)

    def handle_prime(p):
        nonlocal k, ptr
        k += 1
        base = p % MOD_S
        s = powmod(base, k % PHI, MOD_S) if base else 0
        if k <= 1001: Sfirst[k] = s
        idx = k // 10000 + 1; v = s + Sfirst[idx]
        if k <= K:
            ring[ptr] = v; ptr += 1; fw_add(v, 1)
            if k == K: ptr = 0; add_median()
        else:
            out = ring[ptr]; fw_add(out, -1)
            ring[ptr] = v; fw_add(v, 1)
            ptr += 1
            if ptr == K: ptr = 0
            add_median()

    handle_prime(2)
    for x in range(3, bound+1, 2):
        if k >= n: break
        if sieve[x >> 1]: handle_prime(x)

    whole = sum2 // 2; frac = sum2 & 1
    return f"{whole}.{'5' if frac else '0'}"

if __name__ == '__main__':
    print(solve())
