import math

def is_square(value):
    root = math.isqrt(value)
    return root * root == value

def solve():
    limit = 10**12
    progressive_squares = set()
    a = 1
    while a * a <= limit:
        b = 1
        while b < a and a * a * b * b <= limit:
            if math.gcd(a, b) != 1:
                b += 1
                continue
            k = 1
            while k * k * a * a * b * b <= limit:
                candidate1 = k * a * a * k * b * b + k * a * b
                if candidate1 <= limit and is_square(candidate1):
                    progressive_squares.add(candidate1)
                candidate2 = k * a * a * k * a * b + k * b * b
                if candidate2 <= limit and is_square(candidate2):
                    progressive_squares.add(candidate2)
                k += 1
            b += 1
        a += 1
    return str(sum(progressive_squares))

if __name__ == '__main__':
    print(solve())
