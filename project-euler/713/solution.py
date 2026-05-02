def solve():
    n = 10000000
    total = 0
    for r in range(1, n):
        q = n // r
        s = n - r * q
        total += (r * q * (q - 1)) // 2 + s * q
    return str(total)

if __name__ == "__main__":
    print(solve())
