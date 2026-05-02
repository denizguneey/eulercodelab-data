import heapq

def solve():
    MOD = 1000000007
    p = 6
    A = 17**p; B = 19**p; C = 23**p

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD; exp >>= 1
        return r

    INF = float('inf')
    dist = [INF] * A; dist[0] = 0
    pq = [(0, 0)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]: continue
        for step in [B, C]:
            v = (u + step) % A; nd = d + step
            if nd < dist[v]:
                dist[v] = nd; heapq.heappush(pq, (nd, v))

    sw = sw2 = 0
    for w in dist:
        wm = w % MOD
        sw = (sw + wm) % MOD
        sw2 = (sw2 + wm * wm) % MOD

    inv2 = (MOD + 1) // 2
    inv12 = mod_pow(12, MOD - 2)
    Am = A % MOD; invA = mod_pow(Am, MOD - 2)

    genus = sw * invA % MOD
    genus = (genus - (Am - 1) * inv2) % MOD

    gaps = sw2 * inv2 % MOD * invA % MOD
    gaps = (gaps - sw * inv2) % MOD
    A2m = Am * Am % MOD
    gaps = (gaps + (A2m - 1) * inv12) % MOD

    shift = (A % MOD + B % MOD + C % MOD) % MOD
    tri = shift * ((shift - 1) % MOD) % MOD * inv2 % MOD

    ans = (tri + genus * shift + gaps) % MOD
    return str(ans)

if __name__ == '__main__':
    print(solve())
