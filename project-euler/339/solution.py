def solve():
    n = 10000

    def solve_fast(n):
        max_sum = 2 * n
        prev = [0.0]

        for s in range(1, max_sum + 1):
            cur = [0.0] * (s + 1)
            cur[0] = float(s)
            cur[s] = 0.0

            if s >= 2:
                t = (s - 1) // 2
                for w in range(t + 1, s):
                    cur[w] = prev[w - 1]
                if t >= 1:
                    s_f = float(s)
                    right_boundary = prev[t]
                    b = [0.0] * (t + 1)
                    c = [0.0] * (t + 1)
                    d = [0.0] * (t + 1)
                    b[1] = 1.0
                    c[1] = -1.0 / s_f if t >= 2 else 0.0
                    d[1] = s_f - 1.0
                    if t == 1:
                        d[1] += right_boundary / s_f
                    for w in range(2, t + 1):
                        a_coeff = -(s - w) / s_f
                        bw = 1.0
                        cw = -w / s_f if w < t else 0.0
                        dw = 0.0
                        if w == t:
                            dw += w * right_boundary / s_f
                        mult = a_coeff / b[w - 1]
                        bw -= mult * c[w - 1]
                        dw -= mult * d[w - 1]
                        b[w] = bw
                        c[w] = cw
                        d[w] = dw
                    cur[t] = d[t] / b[t]
                    for w in range(t - 1, 0, -1):
                        cur[w] = (d[w] - c[w] * cur[w + 1]) / b[w]

            prev = cur

        return 0.5 * (prev[n - 1] + prev[n + 1])

    answer = solve_fast(n)
    return f"{answer:.6f}"

if __name__ == '__main__':
    print(solve())
