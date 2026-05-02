def solve():
    max_k = 100
    primes = [2,3,5,7,11,13,17,19,23]

    def gen_smooth(limit):
        result = []
        def rec(idx, cur):
            if idx == len(primes):
                result.append(cur); return
            p = primes[idx]; v = cur
            while v <= limit:
                rec(idx+1, v)
                if v > limit // p: break
                v *= p
        rec(0, 1)
        return sorted(set(result))

    side_limit = 1000000
    while True:
        smooth = gen_smooth(side_limit)
        cnt = {}
        for i, x in enumerate(smooth):
            ymax = 11 * x // 10
            for j in range(i, len(smooth)):
                y = smooth[j]
                if y > ymax: break
                area = x * y
                cnt[area] = cnt.get(area, 0) + 1

        INF = float('inf')
        M = [INF] * (max_k + 1)
        for area, k in cnt.items():
            if 2 <= k <= max_k and area < M[k]: M[k] = area

        if all(M[k] < INF for k in range(2, max_k+1)):
            maxM = max(M[k] for k in range(2, max_k+1))
            import math
            s = math.isqrt(maxM)
            if s*s < maxM: s += 1
            needed = (11*s + 9) // 10
            if side_limit >= needed:
                return str(sum(M[k] for k in range(2, max_k+1)))
            side_limit = needed
        else:
            side_limit *= 10

if __name__ == '__main__':
    print(solve())
