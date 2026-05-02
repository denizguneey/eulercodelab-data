MOD = 1000000000
DEG = 40

class Poly:
    def __init__(self):
        self.c = [0] * DEG

    def eval(self, x):
        res = 0
        p = 1
        for i in range(DEG):
            res = (res + p * self.c[i]) % MOD
            p = (p * x) % MOD
        return res

def add_poly(a, b):
    res = Poly()
    for i in range(DEG):
        res.c[i] = (a.c[i] + b.c[i]) % MOD
    return res

def lambda_poly(a, k):
    res = Poly()
    for i in range(DEG):
        res.c[i] = (a.c[i] * k) % MOD
    return res

exponent_poly = Poly()

def shift_poly(p):
    res = Poly()
    last = p.c[DEG - 1]
    for i in range(DEG - 1, 0, -1):
        res.c[i] = p.c[i - 1]
    res.c[0] = 0
    return add_poly(res, lambda_poly(exponent_poly, last))

def mul_poly(p, q):
    res = Poly()
    for i in range(DEG):
        res = add_poly(res, lambda_poly(q, p.c[i]))
        q = shift_poly(q)
    return res

def pow_poly(p, n):
    res = Poly()
    res.c[0] = 1
    while n > 0:
        if n & 1:
            res = mul_poly(res, p)
        n >>= 1
        if n > 0:
            p = mul_poly(p, p)
    return res

def compose_poly(p, q):
    res = Poly()
    prod = Poly()
    prod.c[0] = 1
    for i in range(DEG):
        res = add_poly(res, lambda_poly(prod, p.c[i]))
        prod = mul_poly(prod, q)
    return res

def iter_compose(p, n):
    if n == 0:
        id_poly = Poly()
        id_poly.c[0] = 1
        return id_poly

    res = Poly()
    init = False
    while n > 0:
        if n & 1:
            if not init:
                res = p
                init = True
            else:
                res = compose_poly(p, res)
        n >>= 1
        if n > 0:
            p = compose_poly(p, p)
    return res

def d1(n):
    p = Poly()
    p.c[1] = 1
    q = pow_poly(p, n)
    return add_poly(q, shift_poly(q))

def d2(n, u):
    w = iter_compose(u, n)
    return compose_poly(w, shift_poly(u))

def d3(n, m, l):
    if n == 0:
        u = d1(l)
        v = d2(m, u)
        return compose_poly(u, v)
    u = d3(n - 1, m, l)
    return d2(m, u)

def init_exponent_poly():
    global exponent_poly
    exponent_poly = Poly()
    exponent_poly.c[0] = 1

    for i in range(1, DEG + 1):
        for j in range(DEG - 1, 0, -1):
            exponent_poly.c[j] = (exponent_poly.c[j - 1] + i * exponent_poly.c[j]) % MOD
        exponent_poly.c[0] = (exponent_poly.c[0] * i) % MOD

    for i in range(DEG):
        exponent_poly.c[i] = (MOD - exponent_poly.c[i]) % MOD

def solve():
    a = 12
    b = 345678
    c = 9012345
    d = 678
    e = 90

    init_exponent_poly()
    p_poly = d3(a, b, c)
    ans = (p_poly.eval(d) + e) % MOD
    return f"{ans:09d}"

if __name__ == "__main__":
    print(solve())
