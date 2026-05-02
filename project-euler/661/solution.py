from decimal import Decimal, getcontext

getcontext().prec = 50

def expected_leads(pA, pB, pStop):
    one = Decimal('1')
    two = Decimal('2')
    four = Decimal('4')

    q = one - pStop
    c = one - q * (one - pA - pB)
    disc = c * c - four * q * q * pA * pB
    root = disc.sqrt()

    r_small = (c - root) / (two * q * pA)
    r_big = (c + root) / (two * q * pA)

    return (one - r_small) / (pStop * q * (r_big - r_small))

def solve():
    k_max = 50
    ans = Decimal('0')

    one = Decimal('1')

    for k in range(3, k_max + 1):
        dk = Decimal(str(k))
        dk3 = Decimal(str(k + 3))
        
        pA = one / dk3.sqrt()
        pB = pA + one / (dk * dk)
        p = one / (dk * dk * dk)

        ans += expected_leads(pA, pB, p)

    # rounding to 4 decimal places
    format_ans = "{:.4f}".format(ans)
    return format_ans

if __name__ == '__main__':
    print(solve())
