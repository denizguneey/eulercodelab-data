def L_formula(n):
    unordered = 0
    k = 1
    while True:
        lo = 1 << (k - 1)
        if lo > n:
            break
        p = 1 << k
        hi = min(n, p - 1)
        A = hi - lo + 1
        C = (n + 1) // p
        unordered += A * C
        k += 1

    diagonal = 0
    k = 1
    while True:
        x = (1 << k) - 1
        if x > n:
            break
        diagonal += 1
        k += 1

    ordered = 2 * unordered - diagonal
    return ordered

def solve():
    n = 7 ** 17
    return str(L_formula(n))

if __name__ == "__main__":
    print(solve())
