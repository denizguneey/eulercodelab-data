import math

def solve():
    n = 36

    def augment(u, edges, mr, seen):
        mask = edges[u]
        for v in range(len(mr)):
            if mask & (1<<v) and not seen[v]:
                seen[v] = True
                if mr[v] == -1 or augment(mr[v], edges, mr, seen):
                    mr[v] = u; return True
        return False

    def has_pm(masks, sz):
        order = sorted(range(sz), key=lambda i: bin(masks[i]).count('1'))
        edges = [masks[order[i]] for i in range(sz)]
        mr = [-1]*sz
        for u in range(sz):
            seen = [False]*sz
            if not augment(u, edges, mr, seen): return False
        return True

    def lcm_upto(n):
        l = 1
        for i in range(1,n+1): l = l * i // math.gcd(l, i)
        return l

    def prime_powers(n):
        sieve = [True]*(n+1); sieve[0]=sieve[1]=False
        for p in range(2, int(n**0.5)+1):
            if sieve[p]:
                for q in range(p*p, n+1, p): sieve[q]=False
        f = []
        for p in range(2, n+1):
            if sieve[p]:
                pp = 1
                while pp <= n//p: pp *= p
                f.append(pp)
        return f

    def build_cache(n):
        cache = [[None]*(n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for d in range(1, i+1):
                if i%d != 0: continue
                cache[i][d] = [0]*d
                for r in range(d):
                    mask = 0
                    for o in range(n):
                        if (r+o)%d == 0: mask |= 1<<o
                    cache[i][d][r] = mask
        return cache

    cache = build_cache(n)
    factors = prime_powers(n)

    residues = [0]; modulus = 1
    for factor in factors:
        nm = modulus * factor; nxt = []
        for c in residues:
            for k in range(factor):
                cand = c + k * modulus; masks = [0]*n
                for i in range(1, n+1):
                    d = math.gcd(nm, i); r = cand % d
                    masks[i-1] = cache[i][d][r]
                if has_pm(masks, n): nxt.append(cand)
        residues = nxt; modulus = nm

    L = lcm_upto(n)
    starts = sorted(set(L if r==0 else r for r in residues))

    # nth_divisible_range_start(36, 36)
    nth = 36; per = len(starts)
    block = (nth-1)//per; idx = (nth-1)%per
    return str(block*L + starts[idx])

if __name__ == '__main__':
    print(solve())
