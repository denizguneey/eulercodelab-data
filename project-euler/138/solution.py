# Problem 138: Special isosceles triangles
# Sum of first 12 L values where |b - 2h| = 1 in isosceles triangle.
# Recurrence: L_n = 18*L_{n-1} - L_{n-2}, seeds L_1=17, L_2=305.

def solve():
    count = 12
    a, b = 17, 305
    total = a
    for i in range(2, count + 1):
        total += b
        a, b = b, 18 * b - a
    print(total)

solve()
