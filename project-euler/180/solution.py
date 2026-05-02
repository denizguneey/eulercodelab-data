from fractions import Fraction

def solve():
    order = 35
    fracs = []
    for d in range(2, order + 1):
        for n in range(1, d):
            from math import gcd
            if gcd(n, d) == 1:
                fracs.append(Fraction(n, d))

    allowed = set(fracs)
    sums_set = set()

    for x in fracs:
        for y in fracs:
            # n=1: z = x+y
            z1 = x + y
            if z1 in allowed:
                sums_set.add(x + y + z1)
            # n=-1: z = xy/(x+y)
            s = x + y
            if s != 0:
                zm1 = x * y / s
                if zm1 in allowed:
                    sums_set.add(x + y + zm1)
            # n=2: z = sqrt(x^2+y^2)
            z2sq = x*x + y*y
            # Check if z2sq is a perfect rational square
            if z2sq > 0:
                num = z2sq.numerator
                den = z2sq.denominator
                from math import isqrt
                rn = isqrt(num)
                rd = isqrt(den)
                if rn*rn == num and rd*rd == den:
                    z2 = Fraction(rn, rd)
                    if z2 in allowed:
                        sums_set.add(x + y + z2)
            # n=-2: 1/z^2 = 1/x^2 + 1/y^2
            if x != 0 and y != 0:
                inv_sq = Fraction(1, x*x) + Fraction(1, y*y)
                if inv_sq > 0:
                    zm2sq = Fraction(1, inv_sq)
                    num = zm2sq.numerator
                    den = zm2sq.denominator
                    from math import isqrt
                    rn = isqrt(num)
                    rd = isqrt(den)
                    if rn*rn == num and rd*rd == den:
                        zm2 = Fraction(rn, rd)
                        if zm2 in allowed:
                            sums_set.add(x + y + zm2)

    total = sum(sums_set)
    return str(total.numerator + total.denominator)

if __name__ == '__main__':
    print(solve())
