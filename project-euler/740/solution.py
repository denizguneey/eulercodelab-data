def solve():
    n = 100
    dim = n + 1

    memo = {}

    def idx(i, x, y, a1, a2):
        return (i, x, y, a1, a2)

    def apply_draw(cat, g, y, a1, a2):
        if cat == 0: return g-1, y, a1, a2
        elif cat == 1: return g, y-1, a1, a2
        elif cat == 2: return g, y, a1-1, a2
        else: return g, y, a1+1, a2-1

    def count_cat(cat, g, y, a1, a2):
        if cat == 0: return g
        elif cat == 1: return y
        elif cat == 2: return a1
        else: return 2*a2

    def rec(i, x, y, a1, a2):
        if i == n: return 1.0 if y > 0 else 0.0
        key = (i, x, y, a1, a2)
        if key in memo: return memo[key]

        total_slips = 2*(n - i + 1)
        g0 = total_slips - x - y - a1 - 2*a2
        avail0 = total_slips - x
        future = n - i - 1
        ans = 0.0

        for c1 in range(4):
            cnt1 = count_cat(c1, g0, y, a1, a2)
            if cnt1 <= 0: continue
            p1 = cnt1 / avail0
            g1, y1, a11, a21 = apply_draw(c1, g0, y, a1, a2)
            avail1 = avail0 - 1

            for c2 in range(4):
                cnt2 = count_cat(c2, g1, y1, a11, a21)
                if cnt2 <= 0: continue
                p2 = cnt2 / avail1
                g2, y2, a12, a22 = apply_draw(c2, g1, y1, a11, a21)

                if i == n - 1:
                    cont = 1.0 if y2 > 0 else 0.0
                else:
                    b1, b2 = a12, a22
                    b0 = future - b1 - b2
                    cont = 0.0
                    if b0 > 0: cont += (b0/future) * rec(i+1, 0, y2, b1, b2)
                    if b1 > 0: cont += (b1/future) * rec(i+1, 1, y2, b1-1, b2)
                    if b2 > 0: cont += (b2/future) * rec(i+1, 2, y2, b1, b2-1)

                ans += p1 * p2 * cont

        memo[key] = ans
        return ans

    return f'{rec(1, 2, 2, 0, n-2):.10f}'

if __name__ == '__main__':
    print(solve())
