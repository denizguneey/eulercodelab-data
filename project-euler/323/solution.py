from decimal import Decimal, getcontext

def solve(bits=32):
    getcontext().prec = 50
    expected = Decimal(0)
    
    for n in range(10000):
        bit_zero_prob = Decimal(2) ** -n
        all_ones_prob = (Decimal(1) - bit_zero_prob) ** bits
        term = Decimal(1) - all_ones_prob
        expected += term
        if term < Decimal('1e-20'):
            break
            
    return f"{expected:.10f}"

if __name__ == '__main__':
    print(solve())
