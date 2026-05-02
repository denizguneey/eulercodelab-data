# Problem 135: Same differences
# x^2 - y^2 - z^2 = n, where x,y,z is AP. Count n < 10^6 with exactly 10 solutions.

def solve():
    limit = 1000000
    count = [0] * limit
    for u in range(1, limit):
        vmax = min((limit - 1) // u, 3 * u - 1)
        if vmax < 1: continue
        v = (-u) % 4
        if v == 0: v = 4
        while v <= vmax:
            count[u * v] += 1
            v += 4
    print(sum(1 for n in range(1, limit) if count[n] == 10))

solve()
