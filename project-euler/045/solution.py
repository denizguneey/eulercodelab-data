import math

def is_pentagonal(x):
    if x <= 0:
        return False
    disc = 1.0 + 24.0 * x
    root = math.sqrt(disc)
    n = (1.0 + root) / 6.0
    k = round(n)
    return k > 0 and (k * (3 * k - 1) // 2 == x)

def solve():
    n = 144
    while True:
        hexagonal = n * (2 * n - 1)
        if is_pentagonal(hexagonal):
            return hexagonal
        n += 1

def main():
    result = solve()
    print(result)

if __name__ == "__main__":
    main()
