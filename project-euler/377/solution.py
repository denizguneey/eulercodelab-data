def solve():
    kMod = 1000000000
    kSize = 18

    def zero_matrix():
        return [[0]*kSize for _ in range(kSize)]

    def multiply(a, b):
        c = zero_matrix()
        for i in range(kSize):
            for k in range(kSize):
                if a[i][k] == 0: continue
                for j in range(kSize):
                    if b[k][j] == 0: continue
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % kMod
        return c

    def apply_matrix_vector(a, v):
        out = [0]*kSize
        for i in range(kSize):
            s = 0
            for j in range(kSize):
                if a[i][j] == 0 or v[j] == 0: continue
                s += a[i][j] * v[j]
            out[i] = s % kMod
        return out

    def build_transition():
        t = zero_matrix()
        for i in range(9):
            t[0][i] = 1
        for i in range(1, 9):
            t[i][i - 1] = 1
        for i in range(9):
            t[9][i] = i + 1
            t[9][9 + i] = 10
        for i in range(10, 18):
            t[i][i - 1] = 1
        return t

    transition = build_transition()
    powers = [transition]
    for _ in range(1, 64):
        powers.append(multiply(powers[-1], powers[-1]))

    def f_of_n(n):
        state = [0]*kSize
        state[0] = 1
        e = n
        bit = 0
        while e > 0:
            if (e & 1) != 0:
                state = apply_matrix_vector(powers[bit], state)
            e >>= 1
            bit += 1
        return state[9]

    ans = 0
    p13 = 1
    for _ in range(1, 18):
        p13 *= 13
        ans = (ans + f_of_n(p13)) % kMod

    return str(ans)

if __name__ == '__main__':
    print(solve())
