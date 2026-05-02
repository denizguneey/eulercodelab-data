import math

def solve():
    pi = math.pi

    def concave_ratio(n):
        nl = float(n)
        s2n = math.sqrt(2.0 * nl)
        x0 = nl * (nl + 1.0 - s2n) / (nl * nl + 1.0)
        d = 1.0 - x0
        root = math.sqrt(max(0.0, 1.0 - d * d))
        area_line = x0 * x0 / (2.0 * nl)
        area_arc = d - 0.5 * (d * root + math.asin(d))
        area_concave = area_line + area_arc
        area_L = 1.0 - pi / 4.0
        return area_concave / area_L

    n = 1
    while True:
        if concave_ratio(n) < 0.001:
            return str(n)
        n += 1

if __name__ == '__main__':
    print(solve())
