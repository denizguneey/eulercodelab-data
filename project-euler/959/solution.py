import decimal

decimal.getcontext().prec = 100

def f_value(a, b):
    if a == b:
        return decimal.Decimal('0')
        
    ab = a + b
    pow2 = decimal.Decimal('1')
    for _ in range(ab):
        pow2 *= 2
        
    term = decimal.Decimal('1')
    total_sum = decimal.Decimal('1')
    threshold = decimal.Decimal('1e-80')
    
    for t in range(100000):
        ratio = decimal.Decimal('1')
        
        for i in range(1, ab + 1):
            ratio *= (ab * t + i)
        for i in range(1, a + 1):
            ratio /= (a * t + i)
        for i in range(1, b + 1):
            ratio /= (b * t + i)
            
        ratio /= pow2
        term *= ratio
        total_sum += term
        
        if term < threshold:
            break
            
    return decimal.Decimal('1') / total_sum

def run_validations():
    assert f_value(1, 1) == decimal.Decimal('0')
    v12 = f_value(1, 2)
    target = decimal.Decimal('0.427050983124842272')
    assert abs(v12 - target) < decimal.Decimal('1e-15')

def solve():
    return f"{f_value(89, 97):.9f}"

if __name__ == "__main__":
    run_validations()
    print(solve())
