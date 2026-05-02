MOD = 1000000007

def mod_pow(a, e):
    return pow(a, e, MOD)

def words_mod(p, q, r):
    if p > q:
        p, q = q, p
    m = p + q

    inv = [0] * (m + 1)
    if m >= 1:
        inv[1] = 1
    for i in range(2, m + 1):
        inv[i] = MOD - ((MOD // i) * inv[MOD % i]) % MOD

    comb0 = 1
    for i in range(1, m + 1):
        comb0 = (comb0 * ((r + i) % MOD)) % MOD
        comb0 = (comb0 * inv[i]) % MOD

    if p == 0 or q == 0:
        return comb0

    max_trans = (2 * p - 1) if p == q else (2 * p)
    tmax = min(m - 1, r // 2, max_trans)
    if tmax <= 0:
        return 0

    umax = tmax // 2
    cp = [0] * (umax + 1)
    cq = [0] * (umax + 1)
    cp[0] = 1
    cq[0] = 1

    for u in range(1, umax + 1):
        if u <= p - 1:
            cp[u] = cp[u - 1] * ((p - u) % MOD) % MOD * inv[u] % MOD
        if u <= q - 1:
            cq[u] = cq[u - 1] * ((q - u) % MOD) % MOD * inv[u] % MOD

    n0 = r + m
    n_end = n0 - 2 * tmax
    low = n_end + 1
    high = n0
    length = high - low + 1

    pref = [1] * (length + 1)
    for i in range(length):
        pref[i + 1] = pref[i] * ((low + i) % MOD) % MOD

    inv_total = mod_pow(pref[length], MOD - 2)
    inv_range = [0] * length
    for i in range(length - 1, -1, -1):
        x = low + i
        inv_range[i] = pref[i] * inv_total % MOD
        inv_total = inv_total * (x % MOD) % MOD

    def inv_large(x):
        return inv_range[x - low]

    ans = 0
    comb_t = comb0
    n_cur = n0

    for t in range(1, tmax + 1):
        n_prev = n_cur
        comb_t = comb_t * ((n_prev - m) % MOD) % MOD
        comb_t = comb_t * ((n_prev - m - 1) % MOD) % MOD
        comb_t = comb_t * inv_large(n_prev) % MOD
        comb_t = comb_t * inv_large(n_prev - 1) % MOD
        n_cur = n_prev - 2

        ways_ab = 0
        if (t & 1) == 1:
            u = t // 2
            ways_ab = (2 * cp[u] * cq[u]) % MOD
        else:
            u = t // 2
            ways_ab = (cp[u] * cq[u - 1] + cp[u - 1] * cq[u]) % MOD

        ans = (ans + ways_ab * comb_t) % MOD

    return ans

def solve():
    return str(words_mod(1000000, 10000000, 100000000))

if __name__ == "__main__":
    print(solve())
