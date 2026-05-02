def solve():
    p = 2000000011

    def mul_mod(a, b): return a * b % p
    def mod_pow(a, e):
        r = 1
        while e > 0:
            if e & 1: r = r * a % p
            a = a * a % p; e >>= 1
        return r

    def primes_upto(n):
        sieve = bytearray(b'\x01')*(n+1); sieve[0] = sieve[1] = 0
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i): sieve[j] = 0
        return [i for i in range(2, n+1) if sieve[i]]

    limit = 80
    while True:
        pmax = min(p-1, limit+1)
        primes = primes_upto(pmax)
        split = min(4, len(primes))
        pa, pb = primes[:split], primes[split:]

        def enum_min(prs, idx, cost, res, lim, best):
            if idx == len(prs):
                if res not in best or cost < best[res]: best[res] = cost
                return
            q = prs[idx]; w = q-1; me = (lim-cost)//w; r = res
            for e in range(me+1):
                enum_min(prs, idx+1, cost+e*w, r, lim, best)
                r = r * q % p

        bestA = {}; bestB = {}
        enum_min(pa, 0, 0, 1, limit, bestA)
        enum_min(pb, 0, 0, 1, limit, bestB)

        target = p - 1
        # Batch invert keys of bestA
        keys = list(bestA.keys()); costsA = [bestA[k] for k in keys]
        if not keys: limit += 40; continue
        prefix = [1]*(len(keys)+1)
        for i in range(len(keys)): prefix[i+1] = prefix[i] * keys[i] % p
        inv_total = mod_pow(prefix[-1], p-2)
        invs = [0]*len(keys)
        for i in range(len(keys)-1, -1, -1):
            invs[i] = inv_total * prefix[i] % p
            inv_total = inv_total * keys[i] % p

        bt = None; bca = bcb = -1; bra = brb = 0
        for i in range(len(keys)):
            need = target * invs[i] % p
            if need in bestB:
                cb = bestB[need]; tot = costsA[i]+cb
                if bt is None or tot < bt:
                    bt = tot; bca = costsA[i]; bcb = cb; bra = keys[i]; brb = need

        if bt is not None and bt <= limit:
            def find_exact(prs, idx, rc, res, tgt, exps):
                if idx == len(prs): return rc == 0 and res == tgt
                q = prs[idx]; w = q-1; me = rc//w; r = res
                for e in range(me+1):
                    exps[idx] = e
                    if find_exact(prs, idx+1, rc-e*w, r, tgt, exps): return True
                    r = r * q % p
                return False

            exA = [0]*len(pa); exB = [0]*len(pb)
            find_exact(pa, 0, bca, 1, bra, exA)
            find_exact(pb, 0, bcb, 1, brb, exB)

            prod = 1
            for i in range(len(pa)):
                for _ in range(exA[i]): prod *= pa[i]
            for i in range(len(pb)):
                for _ in range(exB[i]): prod *= pb[i]
            return str(prod)

        limit += 40
        if limit > 600: raise ValueError("No solution found")

if __name__ == '__main__':
    print(solve())
