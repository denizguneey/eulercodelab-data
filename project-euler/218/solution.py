# Problem 218: Perfect Right-angled Triangles
# Every primitive right triangle with square hypotenuse is super-perfect.
# The answer is 0.

def solve():
    # Mathematical proof: For any primitive Pythagorean triple (a,b,c) where c is a perfect square,
    # the area (a*b/2) is always divisible by 6 and by 28 (hence by 84).
    # Therefore there are no "non-super-perfect" triangles, and the count is 0.
    print(0)

solve()
