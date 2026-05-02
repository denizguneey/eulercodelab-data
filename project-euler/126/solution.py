# Problem 126: Cuboid layers
# Find smallest n where C(n) = 1000.

def layer_size(a, b, c, n):
    return 2*(a*b + a*c + b*c) + 4*(n-1)*(a+b+c) + 4*(n-1)*(n-2)

def solve():
    target = 1000
    limit = 50000
    while True:
        count = [0] * (limit + 1)
        for a in range(1, limit + 1):
            if layer_size(a, a, a, 1) > limit: break
            for b in range(a, limit + 1):
                if layer_size(a, b, b, 1) > limit: break
                for c in range(b, limit + 1):
                    if layer_size(a, b, c, 1) > limit: break
                    for n in range(1, limit + 1):
                        cubes = layer_size(a, b, c, n)
                        if cubes > limit: break
                        count[cubes] += 1
        for i in range(1, limit + 1):
            if count[i] == target:
                print(i)
                return
        limit *= 2

solve()
