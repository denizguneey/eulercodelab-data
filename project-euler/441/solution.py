import math

def solve():
    n = 10000000

    # Linear sieve for SPF and phi
    spf = [0]*(n+1); phi = [0]*(n+1); phi[1] = 1
    primes = []
    for i in range(2, n+1):
        if spf[i] == 0:
            spf[i] = i; phi[i] = i-1; primes.append(i)
        for p in primes:
            if i*p > n: break
            spf[i*p] = p
            if p == spf[i]: phi[i*p] = phi[i]*p; break
            phi[i*p] = phi[i]*(p-1)

    # Harmonic prefix
    H = [0.0]*(n+1)
    for i in range(1, n+1): H[i] = H[i-1] + 1.0/i

    half = n // 2
    total = 0.0
    for q in range(2, n+1):
        # Get distinct prime factors
        pf = []; x = q
        while x > 1:
            p = spf[x]; pf.append(p)
            while x % p == 0: x //= p

        # Generate squarefree divisors with signs
        divs = [1]; signs = [1]
        for p in pf:
            m = len(divs)
            for j in range(m):
                divs.append(divs[j]*p); signs.append(-signs[j])

        qm1 = q - 1
        if q <= half:
            a_full = 0.0
            for i in range(len(divs)):
                a_full += signs[i] / divs[i] * H[qm1 // divs[i]]
            total += (phi[q] + a_full) / q
        else:
            a = n - q
            a_a = b = 0.0; c = 0
            for i in range(len(divs)):
                d = divs[i]; s = signs[i]; inv_d = s / d
                ad = a // d; c += s * ad
                a_a += inv_d * H[ad]; b += inv_d * (H[qm1 // d] - H[ad])
            total += (c + a_a + (a+1)*b) / q

    return f'{total:.4f}'

if __name__ == '__main__':
    print(solve())
