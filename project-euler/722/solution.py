import decimal
import math

def format_sci_12(x):
    exponent = int(x.logb())
    mantissa = x / (decimal.Decimal(10) ** exponent)
    
    mantissa = mantissa.quantize(decimal.Decimal('.000000000001'), rounding=decimal.ROUND_HALF_UP)
    if mantissa >= 10:
        mantissa /= 10
        exponent += 1
        
    return f"{mantissa:.12f}e{exponent}"

def bernoulli_even(n):
    if n == 4 or n == 8:
        return decimal.Decimal(-1) / 30
    if n == 16:
        return decimal.Decimal(-3617) / 510
    raise ValueError("Not implemented")

def solve():
    decimal.getcontext().prec = 100
    
    k = 15
    p = 25
    m = (k + 1) // 2
    weight = 2 * m
    
    q = decimal.Decimal(1) - (decimal.Decimal(2) ** -p)
    t = -q.ln()
    
    pi = decimal.Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
    y = t / (2 * pi)
    
    B = bernoulli_even(weight)
    y_neg_pow = y ** -weight
    
    ans = (decimal.Decimal(1) - y_neg_pow) * B / (4 * m)
    
    return format_sci_12(ans)

if __name__ == "__main__":
    print(solve())
