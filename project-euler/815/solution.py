def solve():
    n = 60
    BASE = 61

    def pack(n0, n1, n2, n3):
        return ((n0 * BASE + n1) * BASE + n2) * BASE + n3

    def prob_max_lt(n, k):
        cur = {pack(n, 0, 0, 0): 1.0}
        total_cards = 4 * n
        for step in range(total_cards):
            nxt = {}
            for key, prob in cur.items():
                n3 = key % BASE; key2 = key // BASE
                n2 = key2 % BASE; key2 //= BASE
                n1 = key2 % BASE; n0 = key2 // BASE
                rem = 4*n0 + 3*n1 + 2*n2 + n3
                piles = n1 + n2 + n3
                inv = 1.0 / rem
                if n0 > 0 and piles + 1 < k:
                    nk = pack(n0-1, n1+1, n2, n3)
                    nxt[nk] = nxt.get(nk, 0.0) + prob * (4*n0) * inv
                if n1 > 0 and piles < k:
                    nk = pack(n0, n1-1, n2+1, n3)
                    nxt[nk] = nxt.get(nk, 0.0) + prob * (3*n1) * inv
                if n2 > 0 and piles < k:
                    nk = pack(n0, n1, n2-1, n3+1)
                    nxt[nk] = nxt.get(nk, 0.0) + prob * (2*n2) * inv
                if n3 > 0 and piles - 1 < k:
                    nk = pack(n0, n1, n2, n3-1)
                    nxt[nk] = nxt.get(nk, 0.0) + prob * n3 * inv
            cur = nxt
            if not cur: return 0.0
        return cur.get(pack(0,0,0,0), 0.0)

    ans = 0.0
    for k in range(1, n + 1):
        ans += 1.0 - prob_max_lt(n, k)
    return f'{round(ans * 1e8) / 1e8:.8f}'

if __name__ == '__main__':
    print(solve())
