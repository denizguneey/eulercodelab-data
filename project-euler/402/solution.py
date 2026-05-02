import math

MOD = 1000000000
DIM = 11

def gcd4(a, b, c, d):
    g2 = math.gcd
    return g2(g2(a, b), g2(c, d))

def build_coefficients():
    a3 = 0
    a2 = [0] * 24
    a1 = [0] * 24
    a0 = [0] * 24
    for ra in range(1, 25):
        for rb in range(1, 25):
            for rc in range(1, 25):
                m = gcd4(24, 36 + 6 * ra, 14 + 6 * ra + 2 * rb, 1 + ra + rb + rc)
                a3 = (a3 + m) % MOD
                for rem in range(24):
                    ea = 1 if ra <= rem else 0
                    eb = 1 if rb <= rem else 0
                    ec = 1 if rc <= rem else 0
                    u = m % MOD
                    a2[rem] = (a2[rem] + u * (ea + eb + ec)) % MOD
                    a1[rem] = (a1[rem] + u * (ea * eb + ea * ec + eb * ec)) % MOD
                    a0[rem] = (a0[rem] + u * (ea * eb * ec)) % MOD
    return a3, a2, a1, a0

def mat_identity():
    return [[1 if i == j else 0 for j in range(DIM)] for i in range(DIM)]

def mat_mul(x, y):
    z = [[0] * DIM for _ in range(DIM)]
    for i in range(DIM):
        for k in range(DIM):
            if x[i][k] == 0:
                continue
            for j in range(DIM):
                if y[k][j] == 0:
                    continue
                z[i][j] = (z[i][j] + x[i][k] * y[k][j]) % MOD
    return z

def mat_pow(base, exp):
    res = mat_identity()
    e = exp
    while e > 0:
        if e & 1:
            res = mat_mul(base, res)
        base = mat_mul(base, base)
        e >>= 1
    return res

def mat_vec_mul(m, v):
    out = [0] * DIM
    for i in range(DIM):
        s = 0
        for j in range(DIM):
            if m[i][j] != 0:
                s = (s + m[i][j] * v[j]) % MOD
        out[i] = s
    return out

def step_matrix(carry, rem, a3, a2, a1, a0):
    m = [[0] * DIM for _ in range(DIM)]
    c = carry % MOD
    c2 = (c * c) % MOD
    c3 = (c2 * c) % MOD
    
    m[0][0] = 1
    m[1][2] = 1
    m[2][0] = c
    m[2][1] = 1
    m[2][2] = 1
    
    m[3][5] = 1
    m[4][2] = c
    m[4][4] = 1
    m[4][5] = 1
    
    m[5][0] = c2
    m[5][1] = (2 * c) % MOD
    m[5][2] = (2 * c) % MOD
    m[5][3] = 1
    m[5][4] = 2
    m[5][5] = 1
    
    m[6][9] = 1
    m[7][5] = c
    m[7][8] = 1
    m[7][9] = 1
    
    m[8][2] = c2
    m[8][4] = (2 * c) % MOD
    m[8][5] = (2 * c) % MOD
    m[8][7] = 1
    m[8][8] = 2
    m[8][9] = 1
    
    m[9][0] = c3
    m[9][1] = (3 * c2) % MOD
    m[9][2] = (3 * c2) % MOD
    m[9][3] = (3 * c) % MOD
    m[9][4] = (6 * c) % MOD
    m[9][5] = (3 * c) % MOD
    m[9][6] = 1
    m[9][7] = 3
    m[9][8] = 3
    m[9][9] = 1
    
    m[10][0] = a0[rem]
    m[10][1] = a1[rem]
    m[10][3] = a2[rem]
    m[10][6] = a3
    m[10][10] = 1
    
    return m

def solve():
    k_max = 1234567890123
    a3, a2, a1, a0 = build_coefficients()
    
    fib_mod24 = [0] * 24
    fib_mod24[0] = 0
    fib_mod24[1] = 1
    for i in range(2, 24):
        fib_mod24[i] = (fib_mod24[i-1] + fib_mod24[i-2]) % 24
        
    carry = [0] * 24
    for i in range(24):
        carry[i] = (fib_mod24[i] + fib_mod24[(i+1)%24]) // 24
        
    step = []
    for phase in range(24):
        step.append(step_matrix(carry[phase], fib_mod24[phase], a3, a2, a1, a0))
        
    steps = k_max - 1
    start_phase = 2 % 24
    
    block = mat_identity()
    for t in range(24):
        phase = (start_phase + t) % 24
        block = mat_mul(step[phase], block)
        
    state = [0] * DIM
    state[0] = 1
    
    full_blocks = steps // 24
    rem_steps = steps % 24
    
    if full_blocks > 0:
        block_pow = mat_pow(block, full_blocks)
        state = mat_vec_mul(block_pow, state)
        
    for t in range(rem_steps):
        phase = (start_phase + t) % 24
        state = mat_vec_mul(step[phase], state)
        
    return "{:09d}".format(state[10] % MOD)

if __name__ == '__main__':
    print(solve())
