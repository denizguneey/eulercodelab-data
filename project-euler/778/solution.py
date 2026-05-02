MOD = 1000000009
D = 10

def mat_mul(A, B):
    C = [[0] * D for _ in range(D)]
    for i in range(D):
        for k in range(D):
            aik = A[i][k]
            if aik == 0: continue
            for j in range(D):
                C[i][j] = (C[i][j] + aik * B[k][j]) % MOD
    return C

def mat_pow(base, exp):
    result = [[1 if i == j else 0 for j in range(D)] for i in range(D)]
    while exp > 0:
        if exp & 1:
            result = mat_mul(base, result)
        base = mat_mul(base, base)
        exp >>= 1
    return result

def digit_counts(M, p10):
    N = M + 1
    block = 10 * p10
    full = N // block
    rem = N % block
    
    c = [0] * D
    for d in range(D):
        cnt = full * p10
        shift = d * p10
        if rem > shift:
            extra = rem - shift
            cnt += extra if extra < p10 else p10
        c[d] = cnt % MOD
    return c

def contribution_for_position(R, M, p10):
    c = digit_counts(M, p10)
    T = [[0] * D for _ in range(D)]
    for frm in range(D):
        for d in range(D):
            to = (frm * d) % 10
            T[to][frm] = (T[to][frm] + c[d]) % MOD
            
    P = mat_pow(T, R)
    s = 0
    for r in range(D):
        s = (s + r * P[r][1]) % MOD
    return s

def f_mod(R, M):
    ans = 0
    place_mod = 1
    p10 = 1
    while p10 <= M:
        s = contribution_for_position(R, M, p10)
        ans = (ans + place_mod * s) % MOD
        place_mod = (place_mod * 10) % MOD
        p10 *= 10
    return ans

def solve():
    return str(f_mod(234567, 765432))

if __name__ == "__main__":
    print(solve())
