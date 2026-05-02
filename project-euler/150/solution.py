def solve():
    rows = 1000
    triangle = []
    t = 0
    for r in range(rows):
        row = []
        for c in range(r + 1):
            t = (615949 * t + 797807) % (1 << 20)
            row.append(t - (1 << 19))
        triangle.append(row)

    prefix = []
    for r in range(rows):
        prow = [0] * (r + 2)
        for c in range(r + 1):
            prow[c + 1] = prow[c] + triangle[r][c]
        prefix.append(prow)

    best = float('inf')
    for top in range(rows):
        accum = [0] * (top + 1)
        for bottom in range(top, rows):
            height = bottom - top
            for c in range(top + 1):
                row_segment = prefix[bottom][c + height + 1] - prefix[bottom][c]
                accum[c] += row_segment
                if accum[c] < best:
                    best = accum[c]
    return str(best)

if __name__ == '__main__':
    print(solve())
