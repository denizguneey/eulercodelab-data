import decimal

def solve():
    decimal.getcontext().prec = 50
    n = 100000000
    nl = decimal.Decimal(n)
    inv = 1 / nl
    inv2 = inv * inv
    inv3 = inv2 * inv
    inv4 = inv2 * inv2
    inv5 = inv4 * inv
    inv6 = inv3 * inv3
    inv7 = inv6 * inv
    inv8 = inv4 * inv4
    inv9 = inv8 * inv
    
    euler_gamma = decimal.Decimal('0.57721566490153286060651209008240243104215933593992')
    pi = decimal.Decimal('3.1415926535897932384626433832795028841971693993751')
    
    h1 = nl.ln() + euler_gamma + \
         decimal.Decimal('0.5') * inv - \
         (decimal.Decimal(1) / 12) * inv2 + \
         (decimal.Decimal(1) / 120) * inv4 - \
         (decimal.Decimal(1) / 252) * inv6 + \
         (decimal.Decimal(1) / 240) * inv8
         
    h2 = (pi * pi) / 6 - \
         inv + \
         decimal.Decimal('0.5') * inv2 - \
         (decimal.Decimal(1) / 6) * inv3 + \
         (decimal.Decimal(1) / 30) * inv5 - \
         (decimal.Decimal(1) / 42) * inv7 + \
         (decimal.Decimal(1) / 30) * inv9
         
    ans = decimal.Decimal('0.5') * nl * (h1 * h1 + h2)
    return str(int(ans.to_integral_value(rounding=decimal.ROUND_HALF_UP)))

if __name__ == "__main__":
    print(solve())
