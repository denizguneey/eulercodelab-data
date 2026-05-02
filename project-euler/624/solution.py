def solve():
    MOD = 1000000009
    
    def mod_mul(a, b):
        return (a * b) % MOD
        
    def mat_mul(x, y):
        r00 = (mod_mul(x[0], y[0]) + mod_mul(x[1], y[2])) % MOD
        r01 = (mod_mul(x[0], y[1]) + mod_mul(x[1], y[3])) % MOD
        r10 = (mod_mul(x[2], y[0]) + mod_mul(x[3], y[2])) % MOD
        r11 = (mod_mul(x[2], y[1]) + mod_mul(x[3], y[3])) % MOD
        return (r00, r01, r10, r11)
        
    def mat_pow(base, e):
        r = (1, 0, 0, 1)
        cur = base
        while e > 0:
            if e & 1:
                r = mat_mul(r, cur)
            cur = mat_mul(cur, cur)
            e >>= 1
        return r
        
    def mod_pow(a, e):
        return pow(a, e, MOD)
        
    def P_mod(n):
        inv2 = (MOD + 1) // 2
        A = (inv2, inv2, inv2, 0)
        
        An = mat_pow(A, n)
        An1 = mat_pow(A, n - 1)
        
        w0 = An1[0]
        w1 = An1[2]
        
        m00 = (1 + MOD - An[0]) % MOD
        m01 = (0 + MOD - An[1]) % MOD
        m10 = (0 + MOD - An[2]) % MOD
        m11 = (1 + MOD - An[3]) % MOD
        
        det = (mod_mul(m00, m11) + MOD - mod_mul(m01, m10)) % MOD
        inv_det = mod_pow(det, MOD - 2)
        
        s1 = (mod_mul((MOD - m10) % MOD, w0) + mod_mul(m00, w1)) % MOD
        return mod_mul(inv2, mod_mul(s1, inv_det))
        
    def Q_P(n):
        r = P_mod(n)
        return MOD if r == 0 else r
        
    return str(Q_P(1000000000000000000))

if __name__ == '__main__':
    print(solve())
