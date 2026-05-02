def solve():
    MAX_K = 24; SCALE = 1 << 20
    limit = 100000

    def val_zero_frac(n3):
        star = 0; up = [0]*(MAX_K+1)
        zeros_right = 0; x = n3
        while x > 0:
            d = x % 3
            if d == 0: zeros_right += 1
            else:
                star ^= 1
                if zeros_right <= MAX_K: up[zeros_right] += 1
            x //= 3
        return (0, star, tuple(up))

    def build_values(lim):
        vals = [None]*(lim+1)
        vals[0] = (0, 0, tuple([0]*(MAX_K+1)))
        for n in range(1, lim+1):
            q, r = divmod(n, 3)
            fs, st, up = vals[q]; up = list(up)
            if r == 1: fs -= SCALE
            elif r == 2: st ^= 1
            else:
                if fs <= -2*SCALE: fs += SCALE
                elif fs < 0: fs //= 2
                else: vals[n] = val_zero_frac(n); continue
            vals[n] = (fs, st, tuple(up))
        return vals

    vals = build_values(limit)
    freq = {}
    for n in range(1, limit+1):
        v = vals[n]; freq[v] = freq.get(v, 0) + 1

    def add_vals(a, b):
        return (a[0]+b[0], a[1]^b[1], tuple(x+y for x,y in zip(a[2], b[2])))

    uniq = list(freq.keys())
    f = [freq[k] for k in uniq]
    pair_count = {}

    for i in range(len(uniq)):
        s = add_vals(uniq[i], uniq[i])
        pair_count[s] = pair_count.get(s, 0) + f[i]*(f[i]+1)//2
        for j in range(i+1, len(uniq)):
            s = add_vals(uniq[i], uniq[j])
            pair_count[s] = pair_count.get(s, 0) + f[i]*f[j]

    ans = sum(c*c for c in pair_count.values())
    return str(ans)

if __name__ == '__main__':
    print(solve())
