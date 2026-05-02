def prefix_R(r, m):
    if m == 0:
        return 0
    if m == 1:
        return 4 * r + 2
    t = m - 1
    return (4 * r + 2) + t * (2 * r - m + 2)

def sum_R(r):
    return r * (r + 5)

def prefix_S(m):
    return m * (m + 1)

def sum_S(r):
    rr = r * r
    return 4 * rr + 2 * r

def prefix_U(r, m):
    if m == 0:
        return 0
    if m == 1:
        return 6 * r + 3
    t = m - 1
    return (6 * r + 3) + (t * (4 * r - m + 6)) // 2

def sum_U(r):
    rr = r * r
    return 2 * rr + 11 * r

class Precomp:
    def __init__(self):
        self.block_sum = [0] * 64
        self.block_pref_3q = [0] * 64
        self.pow_prefix = [0] * 64
        self.base_blocks = [[] for _ in range(5)]
        self.base_pref = [[] for _ in range(5)]

def build_precomp():
    pc = Precomp()
    pc.base_blocks[0] = [2]
    pc.base_blocks[1] = [2, 4]
    pc.base_blocks[2] = [3, 6, 2, 6]
    pc.base_blocks[3] = [3, 8, 2, 6, 2, 4, 9, 4]
    pc.base_blocks[4] = [3, 8, 2, 6, 2, 4, 10, 4, 2, 4, 6, 8, 15, 6, 5, 4]

    for k in range(5):
        blk = pc.base_blocks[k]
        pref = [0] * (len(blk) + 1)
        for i in range(len(blk)):
            pref[i + 1] = pref[i] + blk[i]
        pc.base_pref[k] = pref
        pc.block_sum[k] = pref[-1]

        first_three_quarters = (3 * (1 << k)) // 4
        pc.block_pref_3q[k] = pref[first_three_quarters]

    for k in range(5, 64):
        r = 1 << (k - 3)
        rr = r * r
        pc.block_pref_3q[k] = pc.block_pref_3q[k - 1] + 5 * rr + 7 * r
        pc.block_sum[k] = pc.block_pref_3q[k] + 2 * rr + 11 * r

    pc.pow_prefix[0] = 1
    for k in range(1, 64):
        pc.pow_prefix[k] = pc.pow_prefix[k - 1] + pc.block_sum[k - 1]

    return pc

def block_prefix_sum(pc, k, m):
    if m == 0:
        return 0
    length = 1 << k
    if m >= length:
        return pc.block_sum[k]

    if k <= 4:
        return pc.base_pref[k][m]

    q = 3 * (1 << (k - 3))
    r = 1 << (k - 3)
    s = 1 << (k - 2)

    if m <= q:
        return block_prefix_sum(pc, k - 1, m)
    if m <= q + r:
        return pc.block_pref_3q[k - 1] + prefix_R(r, m - q)
    if m <= q + r + s:
        return pc.block_pref_3q[k - 1] + sum_R(r) + prefix_S(m - q - r)
    return pc.block_pref_3q[k - 1] + sum_R(r) + sum_S(r) + prefix_U(r, m - q - r - s)

def prefix_sum(pc, n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    k = n.bit_length() - 1
    p = 1 << k
    out = pc.pow_prefix[k]
    if n > p:
        out += block_prefix_sum(pc, k, n - p)
    return out

def solve():
    n = 1_000_000_000_000
    mod = 100_000_000
    pc = build_precomp()
    total = prefix_sum(pc, n)
    # Output properly zero-padded to 8 digits
    return f"{total % mod:08d}"

if __name__ == '__main__':
    print(solve())
