from decimal import Decimal, getcontext
import math

def solve():
    getcontext().prec = 120
    n = 100000000000000
    k = 20

    euler_gamma = Decimal('0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495')

    def harmonic_large(n_):
        if n_ <= 1000000:
            h = Decimal(0)
            for i in range(1, n_ + 1): h += Decimal(1) / Decimal(i)
            return h
        x = Decimal(n_)
        inv = Decimal(1) / x
        inv2 = inv * inv
        inv4 = inv2 * inv2
        inv6 = inv4 * inv2
        inv8 = inv4 * inv4
        inv10 = inv8 * inv2
        inv12 = inv10 * inv2
        inv14 = inv12 * inv2
        inv16 = inv14 * inv2
        inv18 = inv16 * inv2
        inv20 = inv18 * inv2
        return (x.ln() + euler_gamma + inv/2 - inv2/12 + inv4/120 - inv6/252
                + inv8/240 - 5*inv10/660 + 691*inv12/32760 - inv14/12
                + 3617*inv16/8160 - 43867*inv18/14364 + 174611*inv20/6600)

    def harmonic_small(n_):
        h = Decimal(0)
        for i in range(1, n_ + 1): h += Decimal(1) / Decimal(i)
        return h

    comb = Decimal(1)
    for i in range(1, k + 1):
        comb *= Decimal(n + i)
        comb /= Decimal(i)
    result = comb * (harmonic_large(n + k) - harmonic_small(k))

    # Format as scientific with 10 sig digits
    s = f'{result:.9e}'
    # Normalize exponent
    parts = s.split('e')
    mantissa = parts[0]
    exp_str = parts[1]
    exp_val = int(exp_str)
    return f'{mantissa}e{exp_val}'

if __name__ == '__main__':
    print(solve())
