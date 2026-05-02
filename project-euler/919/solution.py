import math

def fortunate_sum_fast(perimeter_limit):
    coeffs = [(1, 15), (3, 5), (5, 3), (15, 1), (2, 30), (6, 10), (10, 6), (30, 2)]
    ans = 0
    for k, l in coeffs:
        r = 1
        while True:
            sm = k * r * r
            if sm > 4 * perimeter_limit:
                break
            s = 1
            while True:
                df = l * s * s
                if df >= sm:
                    break
                if math.gcd(r, s) == 1 and ((sm + df) & 1) == 0:
                    x = (sm + df) // 2
                    y = (sm - df) // 2
                    if (x * x - y * y) % 15 == 0:
                        z2 = (x * x - y * y) // 15
                        z = math.isqrt(z2)
                        if z * z == z2 and math.gcd(math.gcd(x, y), z) == 1:
                            # case 1: b = y + z
                            a, b, c = x, y + z, z
                            while (a & 3) != 0 or (b & 3) != 0:
                                a <<= 1
                                b <<= 1
                                c <<= 1
                            a >>= 2
                            b >>= 2
                            if math.gcd(math.gcd(a, b), c) <= 1:
                                if a + b + c > 2 * max(a, b, c) and b >= c:
                                    p = a + b + c
                                    ct = perimeter_limit // p
                                    ans += p * ct * (ct + 1) // 2
                            
                            if z < y:
                                # case 2: b = y - z
                                a, b, c = x, y - z, z
                                while (a & 3) != 0 or (b & 3) != 0:
                                    a <<= 1
                                    b <<= 1
                                    c <<= 1
                                a >>= 2
                                b >>= 2
                                if math.gcd(math.gcd(a, b), c) <= 1:
                                    if a + b + c > 2 * max(a, b, c) and b >= c:
                                        p = a + b + c
                                        ct = perimeter_limit // p
                                        ans += p * ct * (ct + 1) // 2
                s += 1
            r += 1
    return str(ans)

def solve():
    return fortunate_sum_fast(10000000)

if __name__ == "__main__":
    print(solve())
