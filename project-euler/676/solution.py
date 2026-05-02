MOD16 = 10**16

def add_mod(a, b):
    s = a + b
    if s >= MOD16:
        s -= MOD16
    return s

def mul_mod(a, b):
    return (a * b) % MOD16

def M(n, k, l):
    if n == 0:
        return 0

    max_bit = n.bit_length()

    coeff = [0] * max_bit
    max_abs = 0
    for p in range(max_bit):
        coeff[p] = (1 << (p % k)) - (1 << (p % l))
        max_abs += abs(coeff[p])

    offset = max_abs
    width = 2 * max_abs + 1

    cnt_lo = [0] * width
    cnt_hi = [0] * width
    sum_lo = [0] * width
    sum_hi = [0] * width

    cnt_hi[offset] = 1

    for pos in range(max_bit - 1, -1, -1):
        ncnt_lo = [0] * width
        ncnt_hi = [0] * width
        nsum_lo = [0] * width
        nsum_hi = [0] * width

        lim = (n >> pos) & 1
        c = coeff[pos]
        bit_value = (1 << pos) % MOD16

        for idx in range(width):
            c0 = cnt_lo[idx]
            if c0 != 0:
                s0 = sum_lo[idx]

                ncnt_lo[idx] = add_mod(ncnt_lo[idx], c0)
                nsum_lo[idx] = add_mod(nsum_lo[idx], s0)

                j = idx + c
                ncnt_lo[j] = add_mod(ncnt_lo[j], c0)
                add1 = add_mod(s0, mul_mod(c0, bit_value))
                nsum_lo[j] = add_mod(nsum_lo[j], add1)

            c1 = cnt_hi[idx]
            if c1 == 0:
                continue
            s1 = sum_hi[idx]

            if lim == 0:
                ncnt_hi[idx] = add_mod(ncnt_hi[idx], c1)
                nsum_hi[idx] = add_mod(nsum_hi[idx], s1)
            else:
                ncnt_lo[idx] = add_mod(ncnt_lo[idx], c1)
                nsum_lo[idx] = add_mod(nsum_lo[idx], s1)

                j = idx + c
                ncnt_hi[j] = add_mod(ncnt_hi[j], c1)
                add1 = add_mod(s1, mul_mod(c1, bit_value))
                nsum_hi[j] = add_mod(nsum_hi[j], add1)

        cnt_lo = ncnt_lo
        cnt_hi = ncnt_hi
        sum_lo = nsum_lo
        sum_hi = nsum_hi

    return add_mod(sum_lo[offset], sum_hi[offset])

def solve():
    ans = 0
    for k in range(3, 7):
        for l in range(1, k - 1):
            ans = add_mod(ans, M(10**16, k, l))

    return f"{ans:016d}"

if __name__ == '__main__':
    print(solve())
