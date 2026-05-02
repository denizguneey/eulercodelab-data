import math

def modinv_u64(a, mod):
    a %= mod
    if a == 0: raise ValueError("modinv: a=0")
    try:
        return pow(a, -1, mod)
    except ValueError:
        raise ValueError("modinv: not invertible")

def pow_mod_u64(a, e, mod):
    return pow(a, e, mod)

def is_prime_trial(p):
    if p < 2: return False
    if p % 2 == 0: return p == 2
    for d in range(3, math.isqrt(p) + 1, 2):
        if p % d == 0: return False
    return True

def pow_table(p, S):
    pp = [1] * (S + 1)
    for i in range(1, S + 1):
        pp[i] = pp[i - 1] * p
    return pp

def compute_coeff_C(p, S):
    pPow = pow_table(p, S)
    mod = pPow[S]
    N = (S - 1) // 2
    if N <= 0: return []

    sample_n = []
    n = 1
    while len(sample_n) < N:
        if n % p != 0:
            sample_n.append(n)
        n += 1

    b = [0] * N
    for i in range(N):
        n = sample_n[i]
        sum_val = 0
        up = p * n
        for m in range(1, up + 1):
            if m % p == 0: continue
            sum_val = (sum_val + modinv_u64(m, mod)) % mod
        b[i] = sum_val

    M = [[0] * (N + 1) for _ in range(N)]
    for i in range(N):
        n = sample_n[i]
        for k in range(N):
            M[i][k] = pow_mod_u64(n, 2 * (k + 1), mod)
        M[i][N] = b[i]

    for col in range(N):
        pivot = -1
        for r in range(col, N):
            if math.gcd(M[r][col], mod) == 1:
                pivot = r
                break
        if pivot == -1:
            raise ValueError("Coefficient solve failed")
        if pivot != col:
            M[pivot], M[col] = M[col], M[pivot]

        invPivot = modinv_u64(M[col][col], mod)
        for c in range(col, N + 1):
            M[col][c] = (M[col][c] * invPivot) % mod

        for r in range(N):
            if r == col: continue
            factor = M[r][col]
            if factor == 0: continue
            for c in range(col, N + 1):
                sub = (factor * M[col][c]) % mod
                M[r][c] = (M[r][c] - sub + mod) % mod

    C = [0] * N
    for i in range(N):
        C[i] = M[i][N] % mod

    return C

def max_Jp(p, S):
    if p < 3 or p % 2 == 0: raise ValueError("p must be odd prime")
    if not is_prime_trial(p): raise ValueError("p is not prime")

    pPow = pow_table(p, S)
    modS = pPow[S]
    C = compute_coeff_C(p, S)

    Hsmall = [0] * p
    for n in range(1, p):
        Hsmall[n] = (Hsmall[n - 1] + modinv_u64(n, modS)) % modS

    cur = []
    maxn = 0
    for n in range(1, p):
        if Hsmall[n] % p == 0:
            cur.append((n, Hsmall[n]))
            maxn = max(maxn, n)

    r = S
    while cur and r >= 2:
        mod_r = pPow[r]
        mod_next = pPow[r - 1]
        
        nxt = []
        for node in cur:
            n, hn = node
            hn_mod = hn % mod_r
            hn_div_p = (hn_mod // p) % mod_next

            poly = 0
            nmod = n % mod_next
            n2 = (nmod * nmod) % mod_next
            pow_n2k = n2
            
            for k in range(len(C)):
                ck = C[k] % mod_next
                if ck:
                    poly = (poly + ck * pow_n2k) % mod_next
                pow_n2k = (pow_n2k * n2) % mod_next

            hp_n = (hn_div_p + poly) % mod_next
            
            if hp_n % p == 0:
                nxt.append((p * n, hp_n))
                maxn = max(maxn, p * n)

            h = hp_n
            for k in range(1, p):
                denom = p * n + k
                invd = modinv_u64(denom, mod_next)
                h = (h + invd) % mod_next
                if h % p == 0:
                    nxt.append((p * n + k, h))
                    maxn = max(maxn, p * n + k)
                    
        cur = nxt
        r -= 1

    if cur and r < 2:
        raise ValueError("Precision S too low: increase S.")
    
    return maxn

def compute_M(p, S):
    maxJ = max_Jp(p, S)
    return p * maxJ + (p - 1)

def solve():
    return str(compute_M(137, 8))

if __name__ == '__main__':
    print(solve())
