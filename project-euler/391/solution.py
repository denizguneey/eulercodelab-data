def solve():
    MAX_N = 1000
    SHIFT = 10
    STRIDE = 1 << SHIFT

    a = [0] * (STRIDE * STRIDE)
    b = [0] * (STRIDE * STRIDE)

    for v in range(MAX_N + 1):
        a[(0 << SHIFT) + v] = v
        b[(0 << SHIFT) + v] = v

    total = 0
    for n in range(1, MAX_N + 1):
        step = n + 1
        for s in range(1, step + 1):
            for m in range(1, s + 1):
                add = s - m + 1
                prev_row = (m - 1) << SHIFT
                cur_row = m << SHIFT
                for v in range(n + 1):
                    value = b[prev_row + v] + add
                    if value >= step:
                        value = 0
                    b[cur_row + v] = a[prev_row + value]

            row = s << SHIFT
            val = b[row]
            v = 1
            while v <= n and b[row + v] == val:
                v += 1
            if v > n:
                m_val = val
                break
            a, b = b, a
        else:
            m_val = a[(step << SHIFT)]

        total += m_val * m_val * m_val

    return str(total)

if __name__ == '__main__':
    print(solve())
