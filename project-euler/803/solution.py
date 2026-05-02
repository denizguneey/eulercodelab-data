def solve():
    A = 25214903917; C = 11; M = 1 << 48; MASK = M - 1

    def mul_mod(x, y): return (x * y) & MASK
    def pow_mod(a, e):
        r = 1
        while e > 0:
            if e & 1: r = mul_mod(r, a)
            a = mul_mod(a, a); e >>= 1
        return r

    def inv_odd(a):
        x = 1
        for _ in range(48): x = mul_mod(x, (2 + M - mul_mod(a, x)) & MASK)
        return x

    def char_code(ch):
        return ord(ch) - ord('a') if ch.islower() else ord(ch) - ord('A') + 26

    def states_starting_with(pat):
        t = [char_code(c) for c in pat]; n = len(t)
        req = [(t[i+1] - t[i] + 4) & 3 for i in range(n-1)]
        low16_cands = []
        for low0 in range(1 << 16):
            low = low0; ok = True
            for i in range(n - 1):
                x = A * low + C; carry = (x >> 16) & 3
                if carry != req[i]: ok = False; break
                low = x & 0xFFFF
            if ok: low16_cands.append(low0)

        states = set()
        for low0 in low16_cands:
            carries = []; low = low0
            for i in range(n - 1):
                x = A * low + C; carries.append(x >> 16); low = x & 0xFFFF
            m = 0
            while True:
                q064 = t[0] + 52 * m
                if q064 > 0xFFFFFFFF: break
                q = q064; ok = True
                for i in range(n - 1):
                    q = ((A & 0xFFFFFFFF) * q + carries[i]) & 0xFFFFFFFF
                    if q % 52 != t[i+1]: ok = False; break
                if ok: states.add((q064 << 16) | low0)
                m += 1
        return sorted(states)

    def advance(start, steps):
        mul, add, bm, ba = 1, 0, A & MASK, C
        while steps > 0:
            if steps & 1:
                add = (mul_mod(bm, add) + ba) & MASK
                mul = mul_mod(bm, mul)
            ba = (mul_mod(bm, ba) + ba) & MASK
            bm = mul_mod(bm, bm); steps >>= 1
        return (mul_mod(mul, start) + add) & MASK

    def dlog(ratio):
        inv_a = inv_odd(A & MASK)
        inv_pows = [inv_a]
        for _ in range(45): inv_pows.append(mul_mod(inv_pows[-1], inv_pows[-1]))
        cur = ratio; exp = 0
        for i in range(46):
            test = pow_mod(cur, 1 << (45 - i))
            if test != 1:
                exp |= 1 << i; cur = mul_mod(cur, inv_pows[i])
        return exp

    def distance(s, t):
        bs = (mul_mod((A-1) & MASK, s) + C) & MASK
        bt = (mul_mod((A-1) & MASK, t) + C) & MASK
        ratio = mul_mod(bt, inv_odd(bs))
        base = dlog(ratio)
        ORDER = 1 << 46
        for k in range(4):
            if advance(s, base + k * ORDER) == t: return base + k * ORDER
        return -1

    ps = states_starting_with("PuzzleOne")
    ls = states_starting_with("LuckyText")
    return str(distance(ps[0], ls[0]))

if __name__ == '__main__':
    print(solve())
