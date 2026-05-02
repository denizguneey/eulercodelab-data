import decimal

def solve():
    decimal.getcontext().prec = 60
    n = 123456789
    
    gamma = decimal.Decimal("0.57721566490153286060651209008240243104215933593992")
    nn = decimal.Decimal(n)
    inv = decimal.Decimal('1') / nn
    inv2 = inv * inv
    inv4 = inv2 * inv2
    inv6 = inv4 * inv2
    inv8 = inv4 * inv4
    inv10 = inv8 * inv2
    
    Hn = nn.ln() + gamma + decimal.Decimal("0.5") * inv \
         - (decimal.Decimal("1") / decimal.Decimal("12")) * inv2 \
         + (decimal.Decimal("1") / decimal.Decimal("120")) * inv4 \
         - (decimal.Decimal("1") / decimal.Decimal("252")) * inv6 \
         + (decimal.Decimal("1") / decimal.Decimal("240")) * inv8 \
         - (decimal.Decimal("5") / decimal.Decimal("660")) * inv10
         
    log10_Hn = Hn.log10()
    log10_2 = decimal.Decimal("2").log10()
    n_log10_2 = decimal.Decimal(n) * log10_2
    
    L = log10_Hn - n_log10_2
    
    frac = L - L.to_integral_value(rounding=decimal.ROUND_FLOOR)
    
    x = (decimal.Decimal(10) ** frac) * decimal.Decimal(1000000)
    ans = int(x + decimal.Decimal("1e-15"))
    if ans >= 10000000:
        ans = 9999999
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
