import math
import heapq

def solve():
    LIMIT = 100_000_000_000_000

    def isqrt(n):
        return math.isqrt(n)

    def max_y_pronic_leq(t):
        s = isqrt(1 + 4 * t)
        return (s - 1) // 2

    y_global_max = max_y_pronic_leq(LIMIT)
    pronic = [y * (y + 1) for y in range(y_global_max + 1)]

    x_max = 0
    for x in range(1, y_global_max + 1):
        p = pronic[x]
        if p > LIMIT // p: break
        x_max = x

    # Build heap: (value, px, y, y_max)
    heap = []
    for x in range(1, x_max + 1):
        px = pronic[x]
        max_t = LIMIT // px
        y_lim = max_y_pronic_leq(max_t)
        if y_lim < x: continue
        heapq.heappush(heap, (px * px, px, x, y_lim))

    count = 0
    last = -1

    while heap:
        val, px, y, y_max = heapq.heappop(heap)
        if val != last:
            count += 1
            last = val
        if y < y_max:
            ny = y + 1
            nval = px * pronic[ny]
            heapq.heappush(heap, (nval, px, ny, y_max))

    return str(count)

if __name__ == '__main__':
    print(solve())
