import math

def solve():
    R = 1_000_000_000

    def isqrt_u64(n):
        r = math.isqrt(n)
        return r

    def count_circle_u_range(limit, parity, begin_u, end_u):
        if begin_u > end_u:
            return 0
        v = isqrt_u64(limit - begin_u * begin_u)
        if (v & 1) != parity:
            if v == 0:
                return 0
            v -= 1

        total = 0
        u = begin_u
        while u <= end_u:
            u2 = u * u
            while u2 + v * v > limit:
                if v <= 1:
                    v = -1
                    break
                v -= 2
            if v < 0:
                break
            count_v = v + 1
            multiplicity = 1 if u == 0 else 2
            total += multiplicity * count_v
            u += 2
        return total

    a = R // 4
    limit = 2 * a * a - 1
    parity = a & 1
    max_u = isqrt_u64(limit)
    if (max_u & 1) != parity:
        max_u -= 1
    first_u = parity

    count_b = count_circle_u_range(limit, parity, first_u, max_u)

    count_o = R * R + R // 2
    count_c = R * (2 * R + 1) // 4
    degenerate = R - 1

    answer = count_o + count_c + count_b - degenerate
    return str(answer)

if __name__ == '__main__':
    print(solve())
