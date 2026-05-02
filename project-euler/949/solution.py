import sys
from collections import defaultdict

sys.setrecursionlimit(2000)

def solve():
    MOD = 1001001011

    def ma(a, b): return (a+b)%MOD
    def mm(a, b): return a*b%MOD

    def fdp2(x, s):
        if s == 0: return x
        if x >= 0: return x >> s
        return -((-x + (1<<s)-1)>>s)

    def cdp2(x, s):
        if s == 0: return x
        if x >= 0: return (x + (1<<s)-1) >> s
        return -((-x)>>s)

    def simplest_between(u, d, e):
        for m in range(e+1):
            s = e - m
            p_min = fdp2(u, s) + 1; p_max = cdp2(d, s) - 1
            if p_min > p_max: continue
            if p_min > 0: p = p_min
            elif p_max < 0: p = p_max
            else: p = 0
            if m > 0 and p != 0 and p%2 == 0:
                if p+1 <= p_max and (p+1)%2 == 1: p += 1
                elif p-1 >= p_min and (p-1)%2 == 1: p -= 1
            return p << s
        return 0

    def compute_u_hot(n):
        e = n; scale = 1 << e; total = (1 << (n+1)) - 1
        dp_u = [0]*total; dp_d = [0]*total
        dp_u[1] = scale; dp_d[1] = scale
        dp_u[2] = -scale; dp_d[2] = -scale
        hot = [0]*(1<<n)
        INF = float('inf')
        for length in range(2, n+1):
            size = 1 << length; start = size - 1
            final = (length == n)
            for bits in range(size):
                u_raw = -INF
                for s_len in range(1, length):
                    suf = bits & ((1<<s_len)-1); idx = (1<<s_len)-1+suf
                    if dp_d[idx] > u_raw: u_raw = dp_d[idx]
                d_raw = INF
                for p_len in range(1, length):
                    pre = bits >> (length-p_len); idx = (1<<p_len)-1+pre
                    if dp_u[idx] < d_raw: d_raw = dp_u[idx]
                idx2 = start + bits
                if u_raw < d_raw:
                    x = simplest_between(u_raw, d_raw, e)
                    dp_u[idx2] = x; dp_d[idx2] = x
                    if final: hot[bits] = 0
                else:
                    dp_u[idx2] = u_raw; dp_d[idx2] = d_raw
                    if final: hot[bits] = 1
        start_n = (1<<n)-1
        u_full = dp_u[start_n:start_n+(1<<n)]
        return u_full, hot

    def conv(a, b):
        out = defaultdict(int)
        for xa, ca in a.items():
            for xb, cb in b.items():
                out[xa+xb] = ma(out[xa+xb], mm(ca, cb))
        return out

    def pow_small(hist, t):
        if t == 0: return {0: 1}
        d = dict(hist)
        for _ in range(1, t): d = conv(d, hist)
        return d

    def count_sum_lt_zero(a, b):
        items = sorted(b.items()); keys = [k for k,_ in items]; vals = [v for _,v in items]
        pref = [0]*(len(vals)+1)
        for i in range(len(vals)): pref[i+1] = ma(pref[i], vals[i])
        from bisect import bisect_left
        ans = 0
        for sa, ca in a.items():
            target = -sa; idx = bisect_left(keys, target)
            ans = ma(ans, mm(ca, pref[idx]))
        return ans

    def count_sum_eq_zero(a, b):
        ans = 0
        if len(a) > len(b): a, b = b, a
        for s, ca in a.items():
            if -s in b: ans = ma(ans, mm(ca, b[-s]))
        return ans

    n = 20; k = 7
    u_full, is_hot = compute_u_hot(n)
    hist_all = defaultdict(int); hist_cold = defaultdict(int)
    for i in range(len(u_full)):
        v = u_full[i]; hist_all[v] = ma(hist_all[v], 1)
        if is_hot[i] == 0: hist_cold[v] = ma(hist_cold[v], 1)

    a2 = k//2; b2 = k - a2
    dist_a = pow_small(hist_all, a2); dist_b = pow_small(hist_all, b2)
    neg = count_sum_lt_zero(dist_a, dist_b)
    cold_a = pow_small(hist_cold, a2); cold_b = pow_small(hist_cold, b2)
    zero_cold = count_sum_eq_zero(cold_a, cold_b)
    return str(ma(neg, zero_cold))

if __name__ == '__main__':
    print(solve())
