def solve():
    kMod = 1000000000
    kOrder = 8
    kRecurrence = [3, -2, 2, -5, 1, 1, 3, -2]
    
    def zero_mat():
        return [[0]*9 for _ in range(9)]
        
    def mat_mul(a, b):
        c = zero_mat()
        for i in range(9):
            for k in range(9):
                if a[i][k] == 0: continue
                for j in range(9):
                    if b[k][j] == 0: continue
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % kMod
        return c

    def apply_mat_pow(base, exp, vec):
        acc = zero_mat()
        for i in range(9): acc[i][i] = 1
        
        while exp > 0:
            if exp & 1:
                acc = mat_mul(base, acc)
            base = mat_mul(base, base)
            exp >>= 1
            
        out = [0]*9
        for i in range(9):
            s = 0
            for j in range(9):
                s = (s + acc[i][j] * vec[j]) % kMod
            out[i] = s
        return out

    def mod_norm(val):
        return val % kMod

    kBase = [1, 2, 4, 6, 11, 20, 36, 67]
    n = 1000000000000000000
    
    s8 = sum(kBase) % kMod
    state = [
        kBase[7]%kMod, kBase[6]%kMod, kBase[5]%kMod, kBase[4]%kMod,
        kBase[3]%kMod, kBase[2]%kMod, kBase[1]%kMod, kBase[0]%kMod, s8
    ]
    
    trans = zero_mat()
    for j in range(kOrder):
        trans[0][j] = mod_norm(kRecurrence[j])
    for r in range(1, kOrder):
        trans[r][r-1] = 1
    for j in range(kOrder):
        trans[8][j] = mod_norm(kRecurrence[j])
    trans[8][8] = 1
    
    advanced = apply_mat_pow(trans, n - 8, state)
    sum_b = advanced[8]
    
    pow2 = pow(2, n, kMod)
    ans = (pow2 - 1 - sum_b) % kMod
    return str(ans)

if __name__ == '__main__':
    print(solve())
