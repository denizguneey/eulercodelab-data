import math

def solve():
    a, b = 5, 8
    DIGITS = 10

    def log10_fact(n):
        return math.lgamma(n + 1) / math.log(10)

    log10_val = a * log10_fact(b) + b * log10_fact(a) - 2 * log10_fact(a * b)

    exp_floor = math.floor(log10_val)
    exponent = int(exp_floor)
    mantissa = 10.0 ** (log10_val - exp_floor)

    scale = 10 ** DIGITS
    scaled = round(mantissa * scale)
    if scaled >= 10 * scale:
        scaled //= 10; exponent += 1

    int_part = scaled // scale
    frac_part = scaled % scale
    return f'{int_part}.{frac_part:0{DIGITS}d}e{exponent}'

if __name__ == '__main__':
    print(solve())
