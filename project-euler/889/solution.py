def solve():
    MOD = 1000062031
    k = 1000000000000000031; t = 100000000000031; r = 62

    def mm(a, b): return a*b%MOD
    def mp(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp&1: r=r*base%MOD
            base=base*base%MOD; exp >>= 1
        return r
    def ma(a, b):
        v = a+b; return v-MOD if v>=MOD else v
    def ms(a, b):
        v = a-b; return v+MOD if v<0 else v

    binom = [0]*(r+1); binom[0] = 1
    for i in range(1, r+1): binom[i] = binom[i-1]*(r-i+1)//i
    binom_mod = [b%MOD for b in binom]

    pow2_t = mp(2, t)
    pow2_ti = [0]*(r+1); pow2_ti[0] = 1
    for i in range(1, r+1): pow2_ti[i] = mm(pow2_ti[i-1], pow2_t)
    pow2_k = mp(2, k); pow2_k_inv = mp(pow2_k, MOD-2); b_mod = ma(pow2_k, 1)

    term = [mm(binom_mod[i], pow2_ti[i]) for i in range(r+1)]
    term_k = [mm(term[i], pow2_k) for i in range(r+1)]
    prefix_k = [0]*(r+2); suffix = [0]*(r+2)
    for i in range(r+1): prefix_k[i+1] = ma(prefix_k[i], term_k[i])
    for i in range(r, -1, -1): suffix[i] = ma(suffix[i+1], term[i])

    def exc_contrib(n, s):
        p2n = mp(2, n); S = 0
        for i in range(r+1):
            base = mm(binom_mod[i], mm(p2n, pow2_ti[i]))
            if i < s: S = ma(S, base)
            else: S = ms(S, mm(base, pow2_k_inv))
        idx = min(s-1, r) if s <= r+1 else r
        e_max = n + t*idx; shift = k - e_max
        Q = 0
        if 0 <= shift < 63: Q = binom[idx] >> shift
        r_mod = ms(S, mm(Q%MOD, b_mod))
        greater = False
        if shift < 63:
            low_mask = (1<<shift)-1; low = binom[idx] & low_mask; half = 1<<(shift-1)
            if low < half: greater = False
            elif low > half: greater = True
            else: greater = s >= 2
        d_mod = ms(b_mod, r_mod) if greater else r_mod
        return mm(d_mod, mp(2, k-n))

    total = 0
    for s in range(1, r+1):
        start_raw = k - s*t; end_raw = k - (s-1)*t - 1
        if end_raw < 0: continue
        start = max(0, start_raw); end = min(end_raw, k-1)
        if start > end: continue
        length = end - start + 1
        exc_start = max(start, end-61); exc_count = end-exc_start+1 if exc_start<=end else 0
        bulk = length - exc_count
        if bulk > 0:
            constant = ms(prefix_k[s], suffix[s])
            total = ma(total, mm(bulk%MOD, constant))
        for n in range(exc_start, end+1): total = ma(total, exc_contrib(n, s))

    # s = r+1
    end_raw = k - r*t - 1
    if end_raw >= 0:
        start = 0; end = min(end_raw, k-1)
        if start <= end:
            length = end-start+1
            exc_start = max(start, end-61); exc_count = end-exc_start+1 if exc_start<=end else 0
            bulk = length - exc_count
            if bulk > 0: total = ma(total, mm(bulk%MOD, prefix_k[r+1]))
            for n in range(exc_start, end+1): total = ma(total, exc_contrib(n, r+1))

    return str(total%MOD)

if __name__ == '__main__':
    print(solve())
