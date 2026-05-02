def solve():
    MOD = 50515093
    TARGET_N = 2_000_000_000

    # Build period sequence
    s = 290797
    s = s * s % MOD  # S_1
    first = s
    seq = []
    while True:
        seq.append(s)
        s = s * s % MOD
        if s == first:
            break

    p = len(seq)

    # Build spans (d_left, d_right) for the periodic sequence
    d_left = [0] * p
    d_right = [0] * p

    def val_at(pos):
        return seq[(pos - 1) % p]

    # d_right: next position with value <= current (within 2 periods)
    stack = []
    for pos in range(2 * p, 0, -1):
        v = val_at(pos)
        while stack and val_at(stack[-1]) > v:
            stack.pop()
        if pos <= p:
            d_right[pos - 1] = stack[-1] - pos
        stack.append(pos)

    # d_left: prev position with value < current (within 2 periods)
    stack = []
    for pos in range(1, 2 * p + 1):
        v = val_at(pos)
        while stack and val_at(stack[-1]) >= v:
            stack.pop()
        if pos > p:
            idx = pos - p
            if stack and stack[-1] >= idx:
                d_left[idx - 1] = pos - stack[-1]
        stack.append(pos)

    # Compute sum of subarray minimums for prefix of length n
    n = TARGET_N
    q_full = n // p
    r = n % p

    total = 0
    for idx in range(1, p + 1):
        occ = q_full + (1 if idx <= r else 0)
        if occ == 0:
            continue
        v = seq[idx - 1]
        dr = d_right[idx - 1]
        dl = d_left[idx - 1]

        rem_last = (r - idx + 1) if idx <= r else (p + r - idx + 1)
        r_last = min(dr, rem_last)

        if dl == 0:
            if occ == 1:
                total += v * idx * r_last
            else:
                n1 = occ - 1
                sum_l = n1 * idx + p * (n1 - 1) * n1 // 2
                total += v * dr * sum_l
                l_last = (occ - 1) * p + idx
                total += v * l_last * r_last
        else:
            if occ == 1:
                l0 = min(dl, idx)
                total += v * l0 * r_last
            else:
                l0 = min(dl, idx)
                total += v * l0 * dr
                if occ > 2:
                    total += v * dl * dr * (occ - 2)
                total += v * dl * r_last

    return str(total)

if __name__ == '__main__':
    print(solve())
