import math
import sys

def circle_points(m):
    r = int(math.isqrt(m))
    pts = []
    for x in range(-r, r + 1):
        y2 = m - x * x
        if y2 < 0:
            continue
        y = math.isqrt(y2)
        if y * y == y2:
            pts.append((x, y))
            if y != 0:
                pts.append((x, -y))
    
    pts.sort()
    unique = []
    for p in pts:
        if not unique or unique[-1] != p:
            unique.append(p)
    return unique

def opposite_pairs(points):
    used = set()
    pairs = []
    for x, y in points:
        k = (x, y)
        if k in used:
            continue
        ov = (-x, -y)
        used.add(k)
        used.add(ov)
        pairs.append(((x, y), ov))
    return pairs

def opposite_pair_count_by_factorization(m):
    if m == 0:
        return 0
    n = m
    pairs = 2
    
    while n & 1 == 0:
        n >>= 1
        
    p = 3
    while p * p <= n:
        if n % p != 0:
            p += 2
            continue
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        if (p & 3) == 3:
            if exp & 1:
                return 0
        elif (p & 3) == 1:
            pairs *= (exp + 1)
        p += 2
        
    if n > 1:
        if (n & 3) == 3:
            return 0
        if (n & 3) == 1:
            pairs *= 2
            
    return pairs

def build_bad_displacements(points):
    bad = set()
    for ax, ay in points:
        for bx, by in points:
            if ax == bx and ay == by:
                continue
            bad.add((ax - bx, ay - by))
    return bad

def four_tuple_has_forbidden_sum(selected, used_count, bad_disp):
    if used_count < 4:
        return False
        
    dx, dy = selected[used_count - 1]
    for i in range(used_count - 1):
        ax, ay = selected[i]
        for j in range(i + 1, used_count - 1):
            bx, by = selected[j]
            for k in range(j + 1, used_count - 1):
                cx, cy = selected[k]
                for mask in range(16):
                    sx = (-ax if (mask & 1) else ax) + \
                         (-bx if (mask & 2) else bx) + \
                         (-cx if (mask & 4) else cx) + \
                         (-dx if (mask & 8) else dx)
                    sy = (-ay if (mask & 1) else ay) + \
                         (-by if (mask & 2) else by) + \
                         (-cy if (mask & 4) else cy) + \
                         (-dy if (mask & 8) else dy)
                    if sx == 0 and sy == 0:
                        continue
                    if (sx, sy) in bad_disp:
                        return True
                        
    return False

def test_selected_vectors(v, lattice):
    d = len(v)
    full = 1 << d
    sums = [(0, 0)] * full
    
    for mask in range(1, full):
        bit = (mask & -mask).bit_length() - 1
        pm = mask ^ (1 << bit)
        sums[mask] = (sums[pm][0] + v[bit][0], sums[pm][1] + v[bit][1])
        
    even_keys = set()
    odd_keys = set()
    even_points = []
    
    for mask in range(full):
        key = sums[mask]
        if mask.bit_count() & 1 == 0:
            if key in even_keys:
                return False
            even_keys.add(key)
            even_points.append(sums[mask])
        else:
            if key in odd_keys:
                return False
            odd_keys.add(key)
            
    for cx, cy in even_points:
        for dx, dy in lattice:
            nx = cx + dx
            ny = cy + dy
            if (nx, ny) in odd_keys:
                continue
            count = 0
            for px, py in lattice:
                if (nx + px, ny + py) in even_keys:
                    count += 1
                    if count >= 2:
                        return False
                        
    return True

def dfs(next_idx, pos, d, reps, bad_disp, selected, lattice):
    if pos == d:
        return test_selected_vectors(selected, lattice)
        
    limit = len(reps) - (d - pos)
    for i in range(next_idx, limit + 1):
        selected[pos] = reps[i]
        if four_tuple_has_forbidden_sum(selected, pos + 1, bad_disp):
            continue
        if dfs(i + 1, pos + 1, d, reps, bad_disp, selected, lattice):
            return True
            
    return False

def find_for_m_and_dimension(m, d):
    lattice = circle_points(m)
    if not lattice: return False
    
    pairs = opposite_pairs(lattice)
    if len(pairs) < d: return False
    
    reps = []
    for a, b in pairs:
        take_a = (a[0] > b[0]) or (a[0] == b[0] and a[1] > b[1])
        reps.append(a if take_a else b)
        
    bad_disp = build_bad_displacements(lattice)
    u = len(reps)
    first_max = u - d
    if first_max < 0: return False
    
    selected = [(0, 0)] * d
    for first in range(first_max + 1):
        selected[0] = reps[first]
        if dfs(first + 1, 1, d, reps, bad_disp, selected, lattice):
            return True
            
    return False

def solve_r_sq(n):
    if n <= 2: return 1
    d = 1
    capacity = 1
    while capacity < n:
        d += 1
        if d >= 64: break
        capacity <<= 1
        
    m = 1
    while True:
        if opposite_pair_count_by_factorization(m) >= d:
            if find_for_m_and_dimension(m, d):
                return m
        m += 1

def solve():
    return str(solve_r_sq(500))

def run_checkpoints():
    assert solve_r_sq(2) == 1
    assert solve_r_sq(4) == 5

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
