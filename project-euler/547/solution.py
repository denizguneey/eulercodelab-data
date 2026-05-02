import math

def legendre_polynomial_and_derivative(n, x):
    pnm1 = 1.0
    pn_local = x
    if n == 0:
        return 1.0, 0.0
    if n == 1:
        return x, 1.0
        
    for k in range(2, n + 1):
        pk = ((2.0 * k - 1.0) * x * pn_local - (k - 1.0) * pnm1) / k
        pnm1 = pn_local
        pn_local = pk
        
    dpn = n * (x * pn_local - pnm1) / (x * x - 1.0)
    return pn_local, dpn

def build_gauss_legendre_01(order):
    nodes = [0.0] * order
    weights = [0.0] * order
    half = (order + 1) // 2
    
    for i in range(half):
        z = math.cos(math.pi * (i + 0.75) / (order + 0.5))
        for _ in range(80):
            pn, dpn = legendre_polynomial_and_derivative(order, z)
            dz = pn / dpn
            z -= dz
            if abs(dz) < 1e-15:
                break
                
        pn, dpn = legendre_polynomial_and_derivative(order, z)
        w = 2.0 / ((1.0 - z * z) * dpn * dpn)
        
        j = order - 1 - i
        nodes[i] = (1.0 - z) * 0.5
        nodes[j] = (1.0 + z) * 0.5
        weights[i] = w * 0.5
        weights[j] = w * 0.5
        
    return nodes, weights

def build_kernel_table(max_n, q_order):
    max_diff = max_n - 1
    kernel = [[0.0] * (max_diff + 1) for _ in range(max_diff + 1)]
    nodes, weights = build_gauss_legendre_01(q_order)
    
    for dx in range(max_diff + 1):
        for dy in range(max_diff + 1):
            s = 0.0
            for i in range(q_order):
                u = nodes[i]
                wu = weights[i]
                ux = 1.0 - u
                for j in range(q_order):
                    v = nodes[j]
                    wv = weights[j]
                    vy = 1.0 - v
                    
                    p1 = math.hypot(dx + u, dy + v)
                    p2 = math.hypot(dx + u, dy - v)
                    p3 = math.hypot(dx - u, dy + v)
                    p4 = math.hypot(dx - u, dy - v)
                    s += wu * wv * ux * vy * (p1 + p2 + p3 + p4)
            kernel[dx][dy] = s
    return kernel

def build_rect_self_table(max_n, kernel):
    self_table = [[0.0] * (max_n + 1) for _ in range(max_n + 1)]
    for w in range(1, max_n + 1):
        for h in range(1, max_n + 1):
            s = 0.0
            for dx in range(-(w - 1), w):
                cx = w - abs(dx)
                for dy in range(-(h - 1), h):
                    cy = h - abs(dy)
                    s += cx * cy * kernel[abs(dx)][abs(dy)]
            self_table[w][h] = s
    return self_table

def build_outer_prefix(n, kernel):
    w = [[0.0] * n for _ in range(n)]
    for hx in range(n):
        for hy in range(n):
            s = 0.0
            for ox in range(n):
                for oy in range(n):
                    s += kernel[abs(ox - hx)][abs(oy - hy)]
            w[hx][hy] = s
            
    prefix = [[0.0] * (n + 1) for _ in range(n + 1)]
    for x in range(n):
        row_acc = 0.0
        for y in range(n):
            row_acc += w[x][y]
            prefix[x + 1][y + 1] = prefix[x][y + 1] + row_acc
    return prefix

def compute_s_for_n(n, kernel, rect_self):
    if n < 3: return 0.0
    prefix = build_outer_prefix(n, kernel)
    f_outer_outer = rect_self[n][n]
    
    total = 0.0
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            f_hole_hole = rect_self[x][y]
            area_ring = n * n - x * y
            inv_area_sq = 1.0 / (area_ring * area_ring)
            
            local_sum = 0.0
            for a in range(1, n - x):
                for b in range(1, n - y):
                    f_outer_hole = prefix[a + x][b + y] - prefix[a][b + y] - prefix[a + x][b] + prefix[a][b]
                    f_ring_ring = f_outer_outer - 2.0 * f_outer_hole + f_hole_hole
                    local_sum += f_ring_ring * inv_area_sq
            total += local_sum
    return total

def solve():
    n = 40
    q_order = 64
    kernel = build_kernel_table(n, q_order)
    rect_self = build_rect_self_table(n, kernel)
    ans = compute_s_for_n(n, kernel, rect_self)
    return f"{ans:.4f}"

if __name__ == '__main__':
    print(solve())
