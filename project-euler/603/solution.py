import math

def solve():
    MOD = 1000000007

    def addmod(a, b):
        s = a + b
        return s - MOD if s >= MOD else s
    def mulmod(a, b): return a * b % MOD

    # 4x4 matrix operations
    def mat_id():
        m = [[0]*4 for _ in range(4)]
        for i in range(4): m[i][i] = 1
        return m

    def mat_mul(x, y):
        z = [[0]*4 for _ in range(4)]
        for i in range(4):
            for k in range(4):
                if x[i][k] == 0: continue
                for j in range(4):
                    z[i][j] = addmod(z[i][j], mulmod(x[i][k], y[k][j]))
        return z

    def mat_vec(m, v):
        r = [0]*4
        for i in range(4):
            acc = 0
            for k in range(4): acc += m[i][k] * v[k]
            r[i] = acc % MOD
        return r

    def feed_digit(m, d):
        for col in range(4):
            f, s, t, one = m[0][col], m[1][col], m[2][col], m[3][col]
            f2 = addmod(addmod(mulmod(10, f), mulmod(d, t)), mulmod(d, one))
            s2 = addmod(s, f2); t2 = addmod(t, one)
            m[0][col] = f2; m[1][col] = s2; m[2][col] = t2

    def feed_number(m, x):
        digits = []
        while x > 0: digits.append(x % 10); x //= 10
        for d in reversed(digits): feed_digit(m, d)

    # Sieve primes up to bound for first N primes
    N = 1000000; K = 1000000000000
    bound = int(N * (math.log(N) + math.log(math.log(N)))) + 200
    sieve = bytearray(b'\x01') * ((bound >> 1) + 1)
    r = int(bound**0.5)
    for p in range(3, r+1, 2):
        if sieve[p >> 1]:
            for x in range(p*p, bound+1, 2*p): sieve[x >> 1] = 0

    # Build per-block matrix
    base = mat_id(); count = 0
    feed_number(base, 2); count += 1
    for x in range(3, bound+1, 2):
        if count >= N: break
        if sieve[x >> 1]:
            feed_number(base, x); count += 1

    # Matrix exponentiation: base^K applied to [0,0,0,1]
    state = [0, 0, 0, 1]; e = K
    while e:
        if e & 1: state = mat_vec(base, state)
        base = mat_mul(base, base); e >>= 1

    return str(state[1])

if __name__ == '__main__':
    print(solve())
