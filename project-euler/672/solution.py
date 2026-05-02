MOD = 1117117717
DIM = 5

def identity():
    return [[1 if i == j else 0 for j in range(DIM)] for i in range(DIM)]

def multiply(x, y):
    z = [[0] * DIM for _ in range(DIM)]
    for i in range(DIM):
        for k in range(DIM):
            xik = x[i][k]
            if not xik:
                continue
            for j in range(DIM):
                ykj = y[k][j]
                if ykj:
                    z[i][j] = (z[i][j] + xik * ykj) % MOD
    return z

def power(base, exp):
    result = identity()
    while exp > 0:
        if exp & 1:
            result = multiply(base, result)
        exp >>= 1
        if exp > 0:
            base = multiply(base, base)
    return result

def apply_matrix(m, v):
    out = [0] * DIM
    for i in range(DIM):
        s = 0
        for j in range(DIM):
            s = (s + m[i][j] * v[j]) % MOD
        out[i] = s
    return out

def digit_matrix(d, weight, pref):
    m = [[0] * DIM for _ in range(DIM)]
    m[0][0] = 1

    m[1][0] = 6
    m[1][1] = 7
    m[1][4] = d

    m[2][0] = 15
    m[2][1] = 21
    m[2][2] = 7
    m[2][3] = d
    m[2][4] = pref[d]

    m[3][3] = 1
    m[3][4] = weight[d]

    m[4][4] = 1

    return m

def sequence_matrix(seq, weight, pref):
    all_mat = identity()
    for ch in seq:
        d = int(ch)
        md = digit_matrix(d, weight, pref)
        all_mat = multiply(md, all_mat)
    return all_mat

def solve_H(k):
    weight = [6, 5, 4, 3, 2, 1, 0]
    pref = [0] * 7
    run = 0
    for d in range(7):
        pref[d] = run
        run += weight[d]

    blockA = "4311623550"
    blockB = "431162355"
    remSingle = "31162355"
    remFirst = "311623550"

    MA = sequence_matrix(blockA, weight, pref)
    MB = sequence_matrix(blockB, weight, pref)
    MSingle = sequence_matrix(remSingle, weight, pref)
    MFirst = sequence_matrix(remFirst, weight, pref)

    t = k // 10

    v = [1, 3, 12, 2, 1]

    if t == 1:
        v = apply_matrix(MSingle, v)
    else:
        v = apply_matrix(MFirst, v)
        if t > 2:
            mid = power(MA, t - 2)
            v = apply_matrix(mid, v)
        v = apply_matrix(MB, v)

    return v[2] % MOD

def solve():
    ans = solve_H(1000000000)
    return str(ans)

if __name__ == '__main__':
    print(solve())
