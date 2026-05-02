import math

def solve():
    N_MAX = 1_000_000_000

    total = 0
    n = 1
    while True:
        min_b = (n + 1)**2 * n**2
        if min_b > N_MAX:
            break
        for m in range(1, n + 1):
            if math.gcd(m, n) != 1:
                continue
            s = m + n
            b0 = s * s * n * n
            if b0 > N_MAX:
                break
            a0 = s * s * m * m
            c0 = m * m * n * n

            t_max = N_MAX // b0
            t_sum = t_max * (t_max + 1) // 2
            total += (a0 + b0 + c0) * t_sum
        n += 1

    return str(total)

if __name__ == '__main__':
    print(solve())
