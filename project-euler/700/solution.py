def solve():
    A = 1504170715041707
    M = 4503599627370517
    FORWARD_STOP = 20000000

    def mod_inv(a, mod):
        t, new_t = 0, 1
        r, new_r = mod, a
        while new_r:
            q = r // new_r
            t, new_t = new_t, t - q * new_t
            r, new_r = new_r, r - q * new_r
        return t % mod

    total = 0
    term = A
    best = A
    total += best

    while best > FORWARD_STOP:
        term += A
        if term >= M: term -= M
        if term < best:
            best = term
            total += best

    inv = mod_inv(A, M)
    best_idx = M + 1
    for value in range(1, best):
        idx = inv * value % M
        if idx < best_idx:
            best_idx = idx
            total += value

    return str(total)

if __name__ == '__main__':
    print(solve())
