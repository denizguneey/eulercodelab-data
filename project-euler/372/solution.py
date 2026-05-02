import math

def solve():
    def isqrt128(n):
        return math.isqrt(n)

    def floor_div_sqrt(t, d):
        return isqrt128(t * t // d)

    class BeattySumSqrt:
        def __init__(self):
            self.memo = {}

        def ge_asqrt_d(self, a, d, rhs):
            if rhs <= 0: return True
            return a * a * d >= rhs * rhs

        def floor_linear_surd(self, a, d, b, c):
            guess = math.floor((a * math.sqrt(d) + b) / c)
            while self.ge_asqrt_d(a, d, (guess+1)*c - b):
                guess += 1
            while not self.ge_asqrt_d(a, d, guess*c - b):
                guess -= 1
            return guess

        def sum_floor(self, d, n):
            return self._impl(d, n, 0, 1)

        def _impl(self, d, n, p, q):
            if n == 0: return 0
            s = int(math.sqrt(d))
            if s * s == d:
                return s * n * (n + 1) // 2
            key = (d, p, q, n)
            if key in self.memo: return self.memo[key]
            a = (s + p) // q
            p1 = a * q - p
            q1 = (d - p1 * p1) // q
            m = self.floor_linear_surd(n, d, -n * p1, q)
            tri = n * (n + 1) // 2
            result = a * tri + n * m - self._impl(d, m, p1, q1)
            self.memo[key] = result
            return result

    def sum_ceil_sqrt(beatty, d, l, r):
        if l > r: return 0
        s = int(math.sqrt(d))
        if s * s == d:
            cnt = r - l + 1
            return s * (l + r) * cnt // 2
        floors = beatty.sum_floor(d, r) - beatty.sum_floor(d, l - 1)
        return floors + (r - l + 1)

    def count_rays(m, n):
        l = m + 1
        k_max = (n * n) // (l * l)
        beatty = BeattySumSqrt()
        total = 0
        for k in range(1, k_max + 1, 2):
            u = floor_div_sqrt(n, k)
            if u < l: continue
            v = floor_div_sqrt(n + 1, k + 1)
            x1 = min(u, v)
            if x1 >= l:
                total += sum_ceil_sqrt(beatty, k+1, l, x1) - sum_ceil_sqrt(beatty, k, l, x1)
            x2 = max(l, v + 1)
            if u >= x2:
                total += (u - x2 + 1) * (n + 1) - sum_ceil_sqrt(beatty, k, x2, u)
        return total

    return str(count_rays(2000000, 1000000000))

if __name__ == '__main__':
    print(solve())
