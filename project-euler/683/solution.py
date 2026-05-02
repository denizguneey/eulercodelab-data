import cmath, math

def solve():
    def expected_round_payment(m):
        pi = math.pi
        den = [0.0]*m; mu = [0.0]*m
        for k in range(1, m):
            th = 2*pi*k/m
            lam = 1/3 + 4/9*math.cos(th) + 2/9*math.cos(2*th)
            den[k] = 1 - lam
        for k in range(1, m):
            inv = 1/den[k]; th = 2*pi*k/m
            base = complex(math.cos(th), math.sin(th)); cur = 1+0j
            for d in range(1, m):
                cur *= base
                mu[d] += (1 - cur.real) * inv
        r = [0.0]*m; sr = 0.0
        for d in range(1, m): r[d] = 2*mu[d]-1; sr += r[d]
        r[0] = -sr
        ss = 0+0j
        for k in range(1, m):
            th = -2*pi*k/m
            base = complex(math.cos(th), math.sin(th)); cur = 1+0j
            rhat = 0+0j
            for d in range(m): rhat += cur*r[d]; cur *= base
            ss += rhat / den[k]
        return -ss.real / m

    acc = 0.0
    for m in range(2, 501): acc += expected_round_payment(m)
    import math as m2
    return f"{acc:.8e}"

if __name__ == '__main__':
    print(solve())
