import math

def solve():
    rt2 = math.sqrt(2.0)
    d0 = 25.0 * (rt2 - 1.0)
    dv = [d0, 10.0, 10.0, 10.0, 10.0, 10.0, d0]
    sp = [10.0, 9.0, 8.0, 7.0, 6.0, 5.0, 10.0]
    U = 100.0 / rt2

    def horiz(k):
        s = 0.0
        for i in range(7):
            t = k * sp[i]
            c = math.sqrt(1.0 - t * t)
            s += dv[i] * t / c
        return s

    def time_needed(k):
        s = 0.0
        for i in range(7):
            t = k * sp[i]
            c = math.sqrt(1.0 - t * t)
            s += dv[i] / (sp[i] * c)
        return s

    lo, hi = 0.0, 0.1
    for _ in range(200):
        mid = (lo + hi) / 2
        if horiz(mid) < U: lo = mid
        else: hi = mid

    ans = time_needed((lo + hi) / 2)
    return f"{ans:.10f}"

if __name__ == '__main__':
    print(solve())
