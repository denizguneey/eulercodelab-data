def solve():
    R, B = 24690, 12345
    prev = [0.0] * (R + 1)
    for b in range(1, B + 1):
        curr = [0.0] * (R + 1)
        curr[0] = 1.0
        for r in range(1, R + 1):
            if r == 1:
                curr[r] = prev[r]; continue
            num = (r - 1) * curr[r - 2] + 2 * b * prev[r]
            curr[r] = num / (r - 1 + 2 * b)
        prev = curr
    return f'{prev[R]:.10f}'

if __name__ == '__main__':
    print(solve())
