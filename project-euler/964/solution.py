import math
import decimal

decimal.getcontext().prec = 100

def choose(n, r):
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)

def factorial_dec(n):
    return decimal.Decimal(math.factorial(n))

def probability(k):
    n = k * (k - 1) // 2 + 1
    total_sum = decimal.Decimal('0')
    
    for r in range(n):
        dim = decimal.Decimal(choose(n - 1, r))
        prod = decimal.Decimal('1')
        for i in range(1, k + 1):
            prod *= decimal.Decimal(choose(n - i, r)) / dim
            
        term = dim * prod
        if r % 2 != 0:
            term = -term
        total_sum += term
        
    return total_sum / factorial_dec(n)

def close_to(a, b, eps):
    return abs(a - b) <= eps

def run_validations():
    assert close_to(probability(2), decimal.Decimal('5e-1'), decimal.Decimal('1e-40'))
    assert close_to(probability(3), decimal.Decimal('1.38888888888888888888888888888888888889e-2'), decimal.Decimal('1e-40'))
    assert close_to(probability(4), decimal.Decimal('6.61375661375661375661375661375661375661e-6'), decimal.Decimal('1e-40'))

def solve():
    ans = probability(7)
    return f"{ans:.10e}"

if __name__ == "__main__":
    run_validations()
    print(solve())
