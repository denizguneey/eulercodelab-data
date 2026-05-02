import math

def generate_pell_pairs(pell_n, d_max, k_max):
    if pell_n == -39:
        seeds = [(3, 4), (6, 5)]
    elif pell_n == -3:
        seeds = [(3, 2)]
    else:
        return []
        
    all_pairs = []
    for k0, d0 in seeds:
        k, d = k0, d0
        while d <= d_max and k <= k_max:
            all_pairs.append((d, k))
            next_k = 2 * k + 3 * d
            next_d = k + 2 * d
            k, d = next_k, next_d
    return sorted(list(set(all_pairs)))

def build_directions(n):
    directions = []
    for q0 in (3, 39):
        pell_n = -117 // q0
        limit = int(math.sqrt(q0)) + 2
        for u in range(-limit, limit + 1):
            for v in range(-limit, limit + 1):
                if u == 0 and v == 0: continue
                if math.gcd(abs(u), abs(v)) != 1: continue
                if u * u + u * v + v * v != q0: continue
                
                a = 2 * u + v
                b = u + 2 * v
                m = math.gcd(abs(a), abs(b))
                if m != 3: continue
                
                x_scale = max(abs(u), abs(v), abs(u + v))
                y_scale_raw = max(abs(a), abs(b), abs(u - v))
                if x_scale == 0 or y_scale_raw % m != 0: continue
                
                y_scale = y_scale_raw // m
                if y_scale == 0: continue
                
                d_max = n // x_scale
                k_max = n // y_scale
                
                if d_max > 0 and k_max > 0:
                    directions.append({
                        'q0': q0, 'u': u, 'v': v, 'm': m,
                        'pell_n': pell_n, 'd_max': d_max, 'k_max': k_max
                    })
                    
    directions.sort(key=lambda d: (d['q0'], d['u'], d['v']))
    return directions

def build_triangle_key(dir_obj, d, k, n):
    u, v, m = dir_obj['u'], dir_obj['v'], dir_obj['m']
    a = 2 * u + v
    b = u + 2 * v
    if a % m != 0 or b % m != 0 or (u - v) % m != 0:
        return None
        
    x1 = d * u
    x2 = d * v
    x3 = -d * (u + v)
    
    y1 = (b // m) * k
    y2 = -(a // m) * k
    y3 = ((u - v) // m) * k
    
    if max(abs(x1), abs(x2), abs(x3), abs(y1), abs(y2), abs(y3)) > n:
        return None
        
    points = sorted([(x1, y1), (x2, y2), (x3, y3)])
    if points[0] == points[1] or points[1] == points[2]:
        return None
        
    area = dir_obj['q0'] * abs(d * k)
    return tuple(points), area

def solve():
    n = 1000000000
    directions = build_directions(n)
    if not directions: return "0"
    
    max_d_n39 = max_k_n39 = max_d_n3 = max_k_n3 = 0
    for d in directions:
        if d['pell_n'] == -39:
            max_d_n39 = max(max_d_n39, d['d_max'])
            max_k_n39 = max(max_k_n39, d['k_max'])
        elif d['pell_n'] == -3:
            max_d_n3 = max(max_d_n3, d['d_max'])
            max_k_n3 = max(max_k_n3, d['k_max'])
            
    pairs_n39 = generate_pell_pairs(-39, max_d_n39, max_k_n39)
    pairs_n3 = generate_pell_pairs(-3, max_d_n3, max_k_n3)
    
    triangles = {}
    for d_obj in directions:
        pairs = pairs_n39 if d_obj['pell_n'] == -39 else pairs_n3
        for d, k_abs in pairs:
            if d > d_obj['d_max'] or k_abs > d_obj['k_max']:
                continue
            for sign in (-1, 1):
                res = build_triangle_key(d_obj, d, sign * k_abs, n)
                if not res: continue
                key, area = res
                if key not in triangles:
                    triangles[key] = area
                elif triangles[key] != area:
                    raise Exception("Inconsistency: same triangle got two areas.")
                    
    total_area = sum(triangles.values())
    return str(total_area)

if __name__ == '__main__':
    print(solve())
