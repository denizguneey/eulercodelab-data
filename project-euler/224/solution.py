def solve():
    perimeter_limit = 75_000_000

    M1 = [[1, -2, 2], [2, -1, 2], [2, -2, 3]]
    M2 = [[1, 2, 2], [2, 1, 2], [2, 2, 3]]
    M3 = [[-1, 2, 2], [-2, 1, 2], [-2, 2, 3]]

    def transform(m, t):
        return (
            m[0][0]*t[0] + m[0][1]*t[1] + m[0][2]*t[2],
            m[1][0]*t[0] + m[1][1]*t[1] + m[1][2]*t[2],
            m[2][0]*t[0] + m[2][1]*t[1] + m[2][2]*t[2]
        )

    stack = [(2, 2, 3)]
    count = 0

    while stack:
        a, b, c = stack.pop()
        perimeter = a + b + c
        if perimeter > perimeter_limit:
            continue
        if a <= b and a + b > c:
            count += 1
        for m in (M1, M2, M3):
            child = transform(m, (a, b, c))
            if child[0] > 0 and child[1] > 0 and child[2] > 0:
                if child[0] + child[1] + child[2] <= perimeter_limit:
                    stack.append(child)

    return str(count)

if __name__ == '__main__':
    print(solve())
