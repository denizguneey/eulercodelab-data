def solve():
    MOD = 1000000007

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r*base%MOD
            base = base*base%MOD; exp >>= 1
        return r

    def compute_g(n):
        if n <= 0: return 0
        isz = max(n+2, 9)
        inv = [0]*isz; inv[1] = 1
        for i in range(2, isz): inv[i] = (MOD - MOD//i)*inv[MOD%i]%MOD
        inv2 = inv[2]; inv3 = inv[3]; inv8 = inv[8]
        m = n//2
        fact = 1; fact_m = 1
        for i in range(1, n+1):
            fact = fact*i%MOD
            if i == m: fact_m = fact
        fact_n = fact
        # f(n): a recurrence
        ap, ac = 1, 0
        for i in range(1, n):
            an = (i*ac + inv2*ap)%MOD * inv[i+1]%MOD
            ap, ac = ac, an
        a_n = ap if n == 0 else ac
        f = fact_n*fact_n%MOD*a_n%MOD
        # D(n): diagonal
        if n == 0: b_n = 1
        elif n == 1: b_n = 0
        elif n == 2: b_n = inv2
        elif n == 3: b_n = 2*inv3%MOD
        else:
            bm3, bm2, bm1, bc = 1, 0, inv2, 2*inv3%MOD
            for i in range(3, n):
                bn = (2*i%MOD*bc%MOD - (i-2)*bm1%MOD - inv2*bm3%MOD)%MOD
                if bn < 0: bn += MOD
                bn = bn*inv[i+1]%MOD
                bm3, bm2, bm1, bc = bm2, bm1, bc, bn
            b_n = bc
        D = fact_n*b_n%MOD
        # R2: rotation 180
        R2 = 0
        if m > 0:
            hp, hc, pc = 1, 1, 0
            for k in range(1, m+1):
                pc = (4*pc + 2*hp)%MOD
                hn = ((4*k+1)%MOD*hc + 4*hp)%MOD*inv[k+1]%MOD
                hp, hc = hc, hn
            h_m = hp; fms = fact_m*fact_m%MOD
            R2 = fms*h_m%MOD if n%2==0 else fms*pc%MOD
        # R90
        R90 = 0
        if n%2==0 and m>0:
            cm2, cm1, cc = 0, 0, 1
            for k in range(m):
                cn = ((2*k+1)%MOD*cc - cm1 + 2*cm2)%MOD
                if cn < 0: cn += MOD
                cn = cn*inv[k+1]%MOD
                cm2, cm1, cc = cm1, cc, cn
            R90 = fact_m*cc%MOD
        # V
        V = fact_n*mod_pow(inv2, n//2)%MOD if n%2==0 else 0
        g = (f + R2 + 2*R90 + 2*V + 2*D)%MOD * inv8%MOD
        return g

    n1 = 7**7; n2 = 8**8
    return str((compute_g(n1) + compute_g(n2))%MOD)

if __name__ == '__main__':
    print(solve())
