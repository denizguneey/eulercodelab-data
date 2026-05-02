# Problem 199: Iterative Circle Packing
# Apollonius gasket: 3 mutually tangent circles inside a larger circle.
# Find fraction of area not covered after 10 iterations.

import math

def solve():
    depth = 10

    def fill_gap(k1, k2, k3, d):
        if d == 0: return 0.0
        k4 = k1 + k2 + k3 + 2.0 * math.sqrt(k1*k2 + k2*k3 + k3*k1)
        area = math.pi / (k4*k4)
        return area + fill_gap(k1, k2, k4, d-1) + fill_gap(k1, k3, k4, d-1) + fill_gap(k2, k3, k4, d-1)

    pi = math.pi
    k = 1.0 + 2.0/math.sqrt(3.0)
    r = 1.0/k
    covered = 3.0 * pi * r * r
    covered += fill_gap(k, k, k, depth)
    covered += 3.0 * fill_gap(-1.0, k, k, depth)
    ratio = 1.0 - covered/pi
    print(f"{ratio:.8f}")

solve()
