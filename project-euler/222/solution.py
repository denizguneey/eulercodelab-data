import math

def solve():
    pipe_radius = 50
    min_radius = 30
    max_radius = 50
    num_balls = max_radius - min_radius + 1
    shift = num_balls - 2

    def distance_y(a, b):
        s = a + b
        side = 2 * pipe_radius - s
        return math.sqrt(s * s - side * side)

    cache = {}

    def dfs(mask, last_radius):
        if mask == 0:
            return distance_y(last_radius, max_radius) + max_radius

        key = (mask, last_radius)
        if key in cache:
            return cache[key]

        best = float('inf')
        for radius in range(min_radius, max_radius + 1):
            bit = 1 << (radius - min_radius)
            if not (mask & bit):
                continue
            cand = distance_y(radius, last_radius) + dfs(mask & ~bit, radius)
            if cand < best:
                best = cand
        cache[key] = best
        return best

    full_mask = (1 << num_balls) - 1
    full_mask &= ~(1 << (max_radius - min_radius))
    full_mask &= ~(1 << (max_radius - 1 - min_radius))

    first = max_radius - 1
    best = first + dfs(full_mask, first)
    return str(round(1000.0 * best))

if __name__ == '__main__':
    print(solve())
