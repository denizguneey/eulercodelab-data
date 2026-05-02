# Problem 194: Coloured Configurations
# Count colourings of a graph with a=25 type-A nodes, b=75 type-B nodes, c=1984, mod 10^8.
# Formula: C(a+b, a) * c * (c-1) * ext_a(c)^a * ext_b(c)^b mod M

from math import comb

def solve():
    a, b, c = 25, 75, 1984
    M = 10**8

    # Brute force values for c=2..7:
    # type_a: 0, 4, 62, 372, 1396, 3980
    # type_b: 0, 6, 88, 486, 1728, 4750
    # These are degree-5 polynomials. Use Newton forward differences.

    def eval_poly(vals, c_val):
        """Evaluate polynomial at c_val using Newton forward differences from values at 2,3,...,7"""
        diffs = vals[:]
        for level in range(1, len(diffs)):
            for i in range(len(diffs)-1, level-1, -1):
                diffs[i] -= diffs[i-1]
        result = 0
        binom = 1
        for i, d in enumerate(diffs):
            result += binom * d
            if i < len(diffs)-1:
                binom = binom * (c_val - 2 - i) // (i + 1)
        return result

    ext_a = eval_poly([0, 4, 62, 372, 1396, 3980], c) % M
    ext_b = eval_poly([0, 6, 88, 486, 1728, 4750], c) % M

    result = comb(a+b, a) % M
    result = result * (c % M) % M * ((c-1) % M) % M
    result = result * pow(ext_a, a, M) % M
    result = result * pow(ext_b, b, M) % M
    print(result)

solve()
