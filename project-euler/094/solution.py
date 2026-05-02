# Problem 94: Almost equilateral triangles
# Find the sum of perimeters of all almost equilateral triangles
# with integral side lengths and area, perimeter <= 10^9.

def solve():
    limit = 1000000000
    total = 0
    x, y = 2, 1
    while True:
        any_found = False
        for sign in [1, -1]:
            num = 2 * x + sign
            if num % 3 != 0:
                continue
            a = num // 3
            if a <= 1:
                continue
            perimeter = 3 * a + sign
            if perimeter <= limit:
                total += perimeter
                any_found = True
        nx = 2 * x + 3 * y
        ny = x + 2 * y
        x, y = nx, ny
        if not any_found and (2 * x - 1) // 3 > limit:
            break
    print(total)

solve()
