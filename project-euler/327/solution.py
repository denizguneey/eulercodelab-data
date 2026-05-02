def M(c, rooms):
    f = 1
    for r in range(2, rooms + 1):
        trips = (f + c - 3) // (c - 2)
        f = f + 2 * trips - 1
    return f + 1

def solve(c_min=3, c_max=40, rooms=30):
    total = 0
    for c in range(c_min, c_max + 1):
        total += M(c, rooms)
    return str(total)

if __name__ == '__main__':
    print(solve())
