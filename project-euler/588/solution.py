def solve():
    nx = [[[0]*32 for _ in range(2)] for _ in range(2)]
    for t in range(2):
        for outb in range(2):
            for mask in range(32):
                nmask = 0
                for c in range(5):
                    if ((mask >> c) & 1) == 0:
                        continue
                    dmax = 4 if t else 0
                    for d in range(dmax + 1):
                        s = c + d
                        if (s & 1) != outb:
                            continue
                        cp = s >> 1
                        nmask ^= (1 << cp)
                nx[t][outb][mask] = nmask

    def Q(k):
        L = k.bit_length() + 3
        cnt = [0] * 32
        cnt[1] = 1
        
        for b in range(L):
            t = (k >> b) & 1
            nxt = [0] * 32
            for mask in range(32):
                ways = cnt[mask]
                if ways == 0:
                    continue
                nxt[nx[t][0][mask]] += ways
                nxt[nx[t][1][mask]] += ways
            cnt = nxt
            
        ans = 0
        for mask in range(32):
            if mask & 1:
                ans += cnt[mask]
        return ans

    total = 0
    k = 1
    for e in range(1, 19):
        k *= 10
        total += Q(k)
        
    return str(total)

if __name__ == '__main__':
    print(solve())
