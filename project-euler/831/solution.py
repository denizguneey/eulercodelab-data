def solve():
    def mul_trunc(a, b):
        c = [0]*6
        for i in range(6):
            if a[i] == 0: continue
            for j in range(6-i): c[i+j] += a[i]*b[j]
        return c

    def pow_poly(base, exp):
        res = [0]*6; res[0] = 1
        while exp > 0:
            if exp & 1: res = mul_trunc(res, base)
            exp >>= 1
            if exp > 0: base = mul_trunc(base, base)
        return res

    R = [1, 3, 5, 5, 3, 1]; m = 142857
    P = pow_poly(R, m)
    B = [1, 5, 10, 10, 5, 1]
    h = sum(P[i]*B[5-i] for i in range(6))

    # Convert h to base 7 and take first 10 digits
    s = ''
    while h > 0: s = str(h%7) + s; h //= 7
    if len(s) < 10: s += '0'*(10-len(s))
    return s[:10]

if __name__ == '__main__':
    print(solve())
