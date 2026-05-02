def solve():
    MOD = 987654321
    N = 10_000_000
    K = 1_000_000_000_000

    def mod_pow(a, e, m=MOD):
        a %= m
        r = 1 % m
        while e:
            if e & 1:
                r = r * a % m
            a = a * a % m
            e >>= 1
        return r

    def mod_inv(a, m=MOD):
        b = m
        u, v = 1, 0
        while b:
            t = a // b
            a, b = b, a - t * b
            u, v = v, u - t * v
        return u % m

    def fwht_xor(a, inverse=False):
        n = len(a)
        ln = 1
        while ln < n:
            for i in range(0, n, ln << 1):
                for j in range(ln):
                    u = a[i + j]
                    v = a[i + j + ln]
                    x = u + v
                    if x >= MOD:
                        x -= MOD
                    y = u - v
                    if y < 0:
                        y += MOD
                    a[i + j] = x
                    a[i + j + ln] = y
            ln <<= 1
        if inverse:
            iv = mod_inv(n)
            for i in range(n):
                a[i] = a[i] * iv % MOD

    def encode_pattern(exps):
        key = len(exps) << 60
        for i, e in enumerate(exps):
            key |= e << (6 * i)
        return key

    def decode_pattern(key):
        ln = key >> 60
        exps = []
        for i in range(ln):
            exps.append((key >> (6 * i)) & 63)
        return exps

    memo = {}

    def grundy(key):
        if key in memo:
            return memo[key]
        a = decode_pattern(key)
        ln = len(a)

        div_nims = []

        def dfs(idx, any_pos, all_eq, cur):
            if idx == ln:
                if not any_pos:
                    return
                if all_eq:
                    return
                b = sorted([c for c in cur if c > 0], reverse=True)
                dkey = encode_pattern(b)
                div_nims.append(grundy(dkey))
                return
            for e in range(a[idx] + 1):
                cur.append(e)
                dfs(idx + 1, any_pos or e > 0, all_eq and e == a[idx], cur)
                cur.pop()

        dfs(0, False, True, [])

        if not div_nims:
            memo[key] = 0
            return 0

        div_nims = sorted(set(div_nims))
        present = set(div_nims)

        mex = 0
        while True:
            ok = False
            for v in div_nims:
                t = v ^ mex
                if t in present:
                    ok = True
                    break
            if not ok:
                break
            mex += 1

        memo[key] = mex
        return mex

    # Build SPF
    spf = list(range(N + 1))
    primes = []
    for i in range(2, N + 1):
        if spf[i] == i:
            primes.append(i)
        for p in primes:
            if i * p > N:
                break
            spf[i * p] = p
            if p == spf[i]:
                break

    counts = {}
    max_g = 0
    for x in range(2, N + 1):
        t = x
        exps = []
        while t > 1:
            p = spf[t]
            c = 0
            while t > 1 and spf[t] == p:
                t //= p
                c += 1
            exps.append(c)
        exps.sort(reverse=True)
        key = encode_pattern(exps)
        g = grundy(key)
        counts[g] = counts.get(g, 0) + 1
        if g > max_g:
            max_g = g

    sz = 1
    while sz <= max_g:
        sz <<= 1
    a = [0] * sz
    for g, cnt in counts.items():
        a[g] = cnt % MOD

    fwht_xor(a)
    for i in range(sz):
        a[i] = mod_pow(a[i], K)
    fwht_xor(a, True)

    losing = a[0] % MOD
    total = mod_pow(N - 1, K)
    return str((total + MOD - losing) % MOD)

if __name__ == '__main__':
    print(solve())
