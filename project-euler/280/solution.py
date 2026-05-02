class Grid:
    def __init__(self):
        self.neighbors = [[-1]*4 for _ in range(25)]
        self.degree = [0]*25
        
        for y in range(5):
            for x in range(5):
                p = y * 5 + x
                d = 0
                if x > 0:
                    self.neighbors[p][d] = p - 1
                    d += 1
                if x + 1 < 5:
                    self.neighbors[p][d] = p + 1
                    d += 1
                if y > 0:
                    self.neighbors[p][d] = p - 5
                    d += 1
                if y + 1 < 5:
                    self.neighbors[p][d] = p + 5
                    d += 1
                self.degree[p] = d

def solve_linear_system(a, rhs):
    eps = 1e-15
    for col in range(25):
        pivot = col
        best = abs(a[col][col])
        for row in range(col + 1, 25):
            cand = abs(a[row][col])
            if cand > best:
                best = cand
                pivot = row
                
        if best < eps:
            return False
            
        if pivot != col:
            a[pivot], a[col] = a[col], a[pivot]
            rhs[pivot], rhs[col] = rhs[col], rhs[pivot]
            
        inv_pivot = 1.0 / a[col][col]
        for j in range(col, 25):
            a[col][j] *= inv_pivot
        for r in range(6):
            rhs[col][r] *= inv_pivot
            
        for row in range(25):
            if row == col:
                continue
            factor = a[row][col]
            if abs(factor) < eps:
                continue
            for j in range(col, 25):
                a[row][j] -= factor * a[col][j]
            for r in range(6):
                rhs[row][r] -= factor * rhs[col][r]
                
    return True

class HittingData:
    def __init__(self):
        self.expect = [0.0] * 25
        self.prob = [[0.0]*5 for _ in range(25)]

def solve_hitting_data(grid, row, mask):
    data = HittingData()
    is_target = [False] * 25
    
    for col in range(5):
        if (mask & (1 << col)) != 0:
            is_target[row * 5 + col] = True
            
    a = [[0.0]*25 for _ in range(25)]
    rhs = [[0.0]*6 for _ in range(25)]
    
    for state in range(25):
        if is_target[state]:
            a[state][state] = 1.0
            rhs[state][0] = 0.0
            col = state % 5
            rhs[state][1 + col] = 1.0
            continue
            
        a[state][state] = 1.0
        deg = grid.degree[state]
        step = 1.0 / deg
        for i in range(deg):
            nb = grid.neighbors[state][i]
            a[state][nb] -= step
        rhs[state][0] = 1.0
        
    if not solve_linear_system(a, rhs):
        return None
        
    for state in range(25):
        data.expect[state] = rhs[state][0]
        for col in range(5):
            data.prob[state][col] = rhs[state][1 + col]
            
    return data

def build_solution_data():
    grid = Grid()
    
    hit_top = [None] * 32
    hit_bottom = [None] * 32
    
    for mask in range(1, 32):
        res = solve_hitting_data(grid, 0, mask)
        if res is None:
            return None
        hit_top[mask] = res
        
        res = solve_hitting_data(grid, 4, mask)
        if res is None:
            return None
        hit_bottom[mask] = res
        
    popcount = [bin(m).count('1') for m in range(32)]
    
    expected_nc = [[[0.0]*25 for _ in range(32)] for _ in range(32)]
    expected_c = [[[0.0]*25 for _ in range(32)] for _ in range(32)]
    
    expected_nc[0][31] = [0.0] * 25
    
    for top_count in range(4, -1, -1):
        for top_mask in range(32):
            if popcount[top_mask] != top_count:
                continue
            empty_top_mask = 31 ^ top_mask
            drop = hit_top[empty_top_mask]
            
            for bottom_mask in range(32):
                if popcount[bottom_mask] != 4 - top_count:
                    continue
                    
                for pos in range(25):
                    value = drop.expect[pos]
                    for col in range(5):
                        bit = 1 << col
                        if (empty_top_mask & bit) == 0:
                            continue
                        value += drop.prob[pos][col] * expected_nc[bottom_mask][top_mask | bit][col]
                        
                    expected_c[bottom_mask][top_mask][pos] = value
                    
        for top_mask in range(32):
            if popcount[top_mask] != top_count:
                continue
            for bottom_mask in range(32):
                if popcount[bottom_mask] != 5 - top_count:
                    continue
                    
                pick = hit_bottom[bottom_mask]
                for pos in range(25):
                    value = pick.expect[pos]
                    for col in range(5):
                        bit = 1 << col
                        if (bottom_mask & bit) == 0:
                            continue
                        value += pick.prob[pos][col] * expected_c[bottom_mask ^ bit][top_mask][20 + col]
                        
                    expected_nc[bottom_mask][top_mask][pos] = value
                    
    return expected_nc

def solve():
    expected_nc = build_solution_data()
    if expected_nc is None:
        return "Error"
        
    initial_pos = 2 * 5 + 2
    initial_bottom_mask = 31
    initial_top_mask = 0
    ans = expected_nc[initial_bottom_mask][initial_top_mask][initial_pos]
    return f"{ans:.6f}"

if __name__ == '__main__':
    print(solve())
