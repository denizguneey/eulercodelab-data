import math

def solve():
    m, n = 64, 10000000000000000

    def bounded_lcm(a, b, limit):
        g = math.gcd(a, b); r = a // g
        if r > limit // b: return 0
        return r * b

    def build_forbidden(m, d, n):
        qs = set()
        for e in range(d+1, m+1):
            q = e // math.gcd(e, d)
            if q > 1 and q <= n: qs.add(q)
        qs = sorted(qs)
        minimal = []
        for q in qs:
            if not any(q % k == 0 for k in minimal):
                minimal.append(q)
        minimal.sort(reverse=True)
        return minimal

    def ie_dfs(divs, n, start, cur_lcm, sign, acc):
        for i in range(start, len(divs)):
            nl = bounded_lcm(cur_lcm, divs[i], n)
            if nl == 0 or nl > n: continue
            acc[0] += sign * (n // nl)
            ie_dfs(divs, n, i+1, nl, -sign, acc)

    def count_not_div(n, divs):
        acc = [n]
        ie_dfs(divs, n, 0, 1, -1, acc)
        return acc[0]

    total = 0
    for d in range(1, m+1):
        forbidden = build_forbidden(m, d, n)
        total += count_not_div(n, forbidden)
    return str(total)

if __name__ == '__main__':
    print(solve())
