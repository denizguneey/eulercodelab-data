def solve():
    R1, X1 = 100000000, 1000000000
    R2, X2 = 1000000000, 100000000
    limit = max(min(R1, X1), min(R2, X2))

    # Build distinct prime factor count (omega) via sieve
    omega = bytearray(limit + 1)
    is_comp = bytearray((limit >> 1) + 1)
    root = int(limit**0.5)
    for p in range(3, root + 1, 2):
        if is_comp[p >> 1]: continue
        for j in range(p * p, limit + 1, p << 1):
            is_comp[j >> 1] = 1
    for m in range(2, limit + 1, 2):
        omega[m] += 1
    for p in range(3, limit + 1, 2):
        if is_comp[p >> 1]: continue
        for m in range(p, limit + 1, p):
            omega[m] += 1

    def solve_F(R, X):
        lim = min(R, X)
        total = 0
        for m in range(1, lim + 1):
            t = R // m
            g = X // m
            w = 1 << omega[m]
            if m & 1:
                unit = 2 * t * g
            else:
                unit = t * g + ((t & 1) & (g & 1))
            total += w * unit
        return total

    return str(solve_F(R1, X1) + solve_F(R2, X2))

if __name__ == '__main__':
    print(solve())
