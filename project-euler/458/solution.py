def solve():
    MOD = 1000000000
    kLen = 6
    kAlphabet = 7
    n = 1000000000000

    def mod_pow(base, exp):
        r = 1; base %= MOD
        while exp > 0:
            if exp & 1: r = r * base % MOD
            base = base * base % MOD
            exp >>= 1
        return r

    if n <= 6: return str(mod_pow(7, n))

    def canonicalize(p):
        remap = {}; nxt = 0; out = []
        for v in p:
            if v not in remap: remap[v] = nxt; nxt += 1
            out.append(remap[v])
        return tuple(out)

    def gen_patterns(pos, mx, cur, out):
        if pos == kLen: out.append(tuple(cur)); return
        for v in range(mx + 2):
            cur.append(v)
            gen_patterns(pos+1, max(mx,v), cur, out)
            cur.pop()

    patterns = []
    gen_patterns(0, -1, [], patterns)
    id_map = {p: i for i, p in enumerate(patterns)}
    sc = len(patterns)

    # Build transition matrix
    trans = [[0]*sc for _ in range(sc)]
    for idx, p in enumerate(patterns):
        k = max(p) + 1
        for label in range(k):
            nxt = canonicalize(p[1:] + (label,))
            nid = id_map[nxt]
            trans[nid][idx] = (trans[nid][idx] + 1) % MOD
        new_count = kAlphabet - k
        if new_count > 0 and k < 6:
            nxt = canonicalize(p[1:] + (k,))
            nid = id_map[nxt]
            trans[nid][idx] = (trans[nid][idx] + new_count) % MOD

    # Initial vector
    vec = [0] * sc
    for idx, p in enumerate(patterns):
        k = max(p) + 1; w = 1
        for t in range(k): w = w * (kAlphabet - t) % MOD
        vec[idx] = w

    # Matrix-vector power
    def mat_vec_mul(M, v):
        r = [0]*len(v)
        for i in range(len(v)):
            s = 0
            for j in range(len(v)):
                s += M[i][j] * v[j]
            r[i] = s % MOD
        return r

    def mat_mul(A, B):
        sz = len(A)
        C = [[0]*sz for _ in range(sz)]
        for i in range(sz):
            for k in range(sz):
                if A[i][k] == 0: continue
                for j in range(sz):
                    C[i][j] += A[i][k] * B[k][j]
            for j in range(sz):
                C[i][j] %= MOD
        return C

    steps = n - 6
    power = trans
    while steps > 0:
        if steps & 1: vec = mat_vec_mul(power, vec)
        steps >>= 1
        if steps > 0: power = mat_mul(power, power)

    return str(sum(vec) % MOD)

if __name__ == '__main__':
    print(solve())
