import math

def solve():
    L = 1000000000000
    root = math.isqrt(1 + 4 * L)
    max_b = (root - 1) // 2

    # Mobius sieve
    mu = [0] * (max_b + 1)
    mu[1] = 1
    is_comp = bytearray(max_b + 1)
    primes = []
    for i in range(2, max_b + 1):
        if not is_comp[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            v = i * p
            if v > max_b: break
            is_comp[v] = 1
            if i % p == 0:
                mu[v] = 0
                break
            mu[v] = -mu[i]

    # For each b, store signed divisors d with mu[d] != 0
    div_lists = [[] for _ in range(max_b + 1)]
    for d in range(1, max_b + 1):
        if mu[d] == 0: continue
        sd = mu[d] * d
        for b in range(d, max_b + 1, d):
            div_lists[b].append(sd)

    answer = 0
    for b in range(1, max_b + 1):
        M = L // b
        upper = min(2 * b - 1, M)
        if upper <= b: continue
        c = b + 1
        while c <= upper:
            q = M // c
            c2 = min(upper, M // q)
            left_m1 = c - 1
            coprime_count = 0
            for sd in div_lists[b]:
                d = abs(sd)
                term = c2 // d - left_m1 // d
                coprime_count += term if sd > 0 else -term
            answer += q * coprime_count
            c = c2 + 1

    return str(answer)

if __name__ == '__main__':
    print(solve())
