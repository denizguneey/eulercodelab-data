import math

class Direction:
    def __init__(self, length, dx, dy, angle):
        self.length = length
        self.dx = dx
        self.dy = dy
        self.angle = angle

def gcd2(x, y):
    x = abs(x)
    y = abs(y)
    if y == 0: return x
    if x == 0: return y
    while y != 0:
        x, y = y, x % y
    return x

def init_vectors(n):
    vectors = []
    for y in range(-n, n + 1):
        for x in range(-n, n + 1):
            t = x * x + y * y
            t2 = int(math.sqrt(t) + 0.5)
            if gcd2(x, y) != 1 or t2 * t2 != t:
                continue
            
            ang = math.atan2(y, x)
            if ang < 0.0:
                ang += 6.2831853071795862
            vectors.append(Direction(t2, x, y, ang))
            
    vectors.sort(key=lambda d: (d.angle, d.dx, d.dy))
    return vectors

def add_transitions(src, dx, dy, nrl, n, dst):
    base = n + 1
    nrl2 = nrl * nrl
    
    for packed, count in src.items():
        cy = packed % base
        cx = packed // base - n
        nx = cx + dx
        ny = cy + dy
        np = nx * nx + ny * ny
        
        if ny >= 0 and np <= nrl2:
            key = (nx + n) * base + ny
            dst[key] = dst.get(key, 0) + count

def count_polygons(n):
    if n < 3:
        return 0
        
    vectors = init_vectors((n - 1) // 2)
    
    arr = [{} for _ in range(n + 1)]
    origin_key = n * (n + 1)
    arr[n][origin_key] = 1
    
    for v in vectors:
        for i in range(v.length, n + 1):
            src = arr[i]
            if not src:
                continue
            for g in range(1, i // v.length + 1):
                nrl = i - v.length * g
                add_transitions(src, v.dx * g, v.dy * g, nrl, n, arr[nrl])
                
    diagonal = 0
    for v in vectors:
        diagonal += n // (2 * v.length)
    diagonal //= 2
    
    answer = -diagonal - 1
    for i in range(n + 1):
        if origin_key in arr[i]:
            answer += arr[i][origin_key]
            
    return answer

def solve(perimeter_limit=120):
    return str(count_polygons(perimeter_limit))

if __name__ == '__main__':
    print(solve())
