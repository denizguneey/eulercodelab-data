def solve():
    def ceil_div(a, b):
        return (a + b - 1) // b

    def total_iterations(lo, hi, x):
        if lo > hi:
            return 0
        total = hi - lo + 1
        cmin = ceil_div(lo, x)
        cmax = ceil_div(hi, x)
        ymin = (x + cmin) // 2
        ymax = (x + cmax) // 2
        for y in range(ymin, ymax + 1):
            cl = 2 * y - x
            ch = cl + 1
            fr = max(cl, cmin)
            to = min(ch, cmax)
            if fr > to:
                continue
            nl = (fr - 1) * x + 1
            nr = to * x
            nl = max(nl, lo)
            nr = min(nr, hi)
            if y == x:
                continue
            total += total_iterations(nl, nr, y)
        return total

    def average_iterations_for_digits(d):
        lo = 10 ** (d - 1)
        hi = 10 ** d - 1
        exp = (d - 1) // 2 if d % 2 == 1 else (d - 2) // 2
        p10 = 10 ** exp
        x0 = 2 * p10 if d % 2 == 1 else 7 * p10
        tot = total_iterations(lo, hi, x0)
        cnt = hi - lo + 1
        return tot / cnt

    ans = average_iterations_for_digits(14)
    return f'{ans:.10f}'

if __name__ == '__main__':
    print(solve())
