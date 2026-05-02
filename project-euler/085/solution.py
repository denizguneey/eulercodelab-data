# Problem 85: Counting rectangles
# Find the area of the grid closest to containing two million rectangles.

def solve():
    target = 2000000
    best_area, best_diff = 0, float('inf')
    for a in range(1, 2001):
        for b in range(a, 2001):
            count = a * (a + 1) * b * (b + 1) // 4
            diff = abs(count - target)
            if diff < best_diff:
                best_diff = diff
                best_area = a * b
            if count > target:
                break
    print(best_area)

solve()
