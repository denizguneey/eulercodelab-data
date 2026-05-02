from math import gcd

def solve():
    max_n = 18

    def make_fraction(num, den):
        g = gcd(num, den)
        return (num // g, den // g)

    def parallel_combine(a, b):
        num = a[0] * b[1] + b[0] * a[1]
        den = a[1] * b[1]
        return make_fraction(num, den)

    ways = [[] for _ in range(max_n + 1)]
    ways[1] = [(1, 1)]
    all_fracs = set()
    all_fracs.add((1, 1))

    for n in range(2, max_n + 1):
        cur = set()
        for a in range(1, n // 2 + 1):
            b = n - a
            for fi in ways[a]:
                j_start = 0
                for idx, fj in enumerate(ways[b]):
                    if a == b and idx < ways[a].index(fi):
                        continue
                    p = parallel_combine(fi, fj)
                    cur.add(p)
                    if p[0] != p[1]:
                        cur.add((p[1], p[0]))
        ways[n] = sorted(cur)
        all_fracs.update(cur)

    return str(len(all_fracs))

if __name__ == '__main__':
    print(solve())
