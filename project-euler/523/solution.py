import math

def solve():
    N = 30

    # Compute D = lcm(1..N)
    D = 1
    for i in range(1, N + 1):
        D = D * i // math.gcd(D, i)

    scaled_E = [0] * (N + 1)
    prefix = 0
    for n in range(1, N + 1):
        two_pow = 1 << n
        c = two_pow - n - 1
        numerator = prefix + c * D
        scaled_E[n] = numerator // n
        prefix += scaled_E[n]

    # E(30) = scaled_E[30] / D, round to 2 decimal places
    num100 = scaled_E[N] * 100
    q = num100 // D
    rem = num100 % D
    if rem * 2 >= D:
        q += 1
    integer = q // 100
    frac = q % 100
    return f"{integer}.{frac:02d}"

if __name__ == '__main__':
    print(solve())
