def R_value(n):
    t5_nxt = [0] * n
    t5_p = [0.0] * n
    t6_nxt = [0] * n
    t6_p = [0.0] * n

    for r in range(1, n):
        m5 = 5 * r
        n5 = m5 % n
        t5_nxt[r] = n5
        t5_p[r] = float(n5) / float(m5)

        m6 = 6 * r
        n6 = m6 % n
        t6_nxt[r] = n6
        t6_p[r] = float(n6) / float(m6)

    v = [0.0] * n
    nv = [0.0] * n

    for iter_count in range(2000):
        diff = 0.0
        for r in range(1, n):
            c5 = 1.0 + t5_p[r] * v[t5_nxt[r]]
            c6 = 1.0 + t6_p[r] * v[t6_nxt[r]]
            nv[r] = c5 if c5 < c6 else c6
            
            d = abs(nv[r] - v[r])
            if d > diff:
                diff = d
                
        v, nv = nv, v
        if diff < 1e-18:
            break

    return v[1]

def solve():
    s = 0.0
    for k in range(2, 1001):
        s += R_value(k)
    return f"{s:.6f}"

if __name__ == "__main__":
    print(solve())
