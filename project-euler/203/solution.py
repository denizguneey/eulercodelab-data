# Problem 203: Squarefree Binomial Coefficients
# Sum of distinct squarefree values in the first 51 rows of Pascal's triangle.

def solve():
    def is_squarefree(v):
        if v == 0: return False
        if v % 4 == 0: return False
        p = 3
        while p * p <= v:
            if v % (p*p) == 0: return False
            p += 2
        return True

    rows = 51
    values = set()
    for n in range(rows):
        c = 1
        for k in range(n+1):
            values.add(c)
            c = c * (n - k) // (k + 1)

    print(sum(v for v in values if is_squarefree(v)))

solve()
