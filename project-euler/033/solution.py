import math

def is_nontrivial_digit_canceling(num, den):
    if num >= den or num < 10 or den < 10:
        return False

    n1 = num // 10
    n2 = num % 10
    d1 = den // 10
    d2 = den % 10

    if n2 == 0 and d2 == 0:
        return False

    def equivalent(a, b):
        if b == 0:
            return False
        return num * b == den * a

    if n1 == d1 and n1 != 0 and equivalent(n2, d2):
        return True
    if n1 == d2 and n1 != 0 and equivalent(n2, d1):
        return True
    if n2 == d1 and n2 != 0 and equivalent(n1, d2):
        return True
    if n2 == d2 and n2 != 0 and equivalent(n1, d1):
        return True

    return False

def solve():
    product_num = 1
    product_den = 1

    for num in range(10, 100):
        for den in range(num + 1, 100):
            if is_nontrivial_digit_canceling(num, den):
                product_num *= num
                product_den *= den

    g = math.gcd(product_num, product_den)
    return product_den // g

if __name__ == "__main__":
    print(solve())
