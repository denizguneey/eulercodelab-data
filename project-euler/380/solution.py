import math

def solve():
    m, n = 100, 500
    pi = math.pi

    cos_m = [math.cos(pi * i / m) for i in range(m)]
    cos_n = [math.cos(pi * j / n) for j in range(n)]

    sum_log10 = 0.0
    for i in range(m):
        ci = cos_m[i]
        for j in range(n):
            if i == 0 and j == 0:
                continue
            cj = cos_n[j]
            eigenvalue = 4.0 - 2.0 * ci - 2.0 * cj
            sum_log10 += math.log10(eigenvalue)

    sum_log10 -= math.log10(m * n)

    # Format as scientific with 5 significant digits
    exponent = int(math.floor(sum_log10))
    mantissa = 10.0 ** (sum_log10 - exponent)
    scale = 10000.0
    rounded = round(mantissa * scale)
    if rounded >= 10.0 * scale:
        rounded /= 10.0
        exponent += 1
    result = rounded / scale
    return f"{result:.4f}e{exponent}"

if __name__ == '__main__':
    print(solve())
