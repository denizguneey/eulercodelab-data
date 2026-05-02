import decimal

def solve_expectation(n, k):
    decimal.getcontext().prec = 50
    m1 = decimal.Decimal(k)
    m2 = decimal.Decimal(k * k)
    total = decimal.Decimal(0)
    
    dec_k = decimal.Decimal(k)
    dec_2 = decimal.Decimal(2)
    dec_1 = decimal.Decimal(1)
    
    for t in range(1, n + 1):
        m = decimal.Decimal(n - t + 2)
        a = dec_2 / m
        c = (dec_2 * decimal.Decimal(2 * k - 1)) / (m * (dec_k * m - dec_1))
        
        total += c * m2 + (a - c) * m1
        
        if t == n:
            break
            
        r = (m - dec_2) / m
        s = ((m - dec_2) * (dec_k * (m - dec_2) - dec_1)) / (m * (dec_k * m - dec_1))
        
        next_m2 = s * m2 + (dec_2 * dec_k * r + r - s) * m1 + dec_k * dec_k
        next_m1 = r * m1 + dec_k
        
        m1 = next_m1
        m2 = next_m2
        
    return total

def solve():
    ans = solve_expectation(1000000, 10)
    # Round to nearest integer (long long in C++)
    # rounding behavior: half to even is default typically, but half up is common for simple rounding
    return str(int(ans.to_integral_value(rounding=decimal.ROUND_HALF_UP)))

if __name__ == "__main__":
    print(solve())
