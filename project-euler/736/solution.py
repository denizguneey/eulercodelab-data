kStartX = 45
kStartY = 90
kMaxM = 120

def can_reach_zero(x, y, r_rem, s_rem):
    pow2_s = 1 << s_rem
    pow2_r = 1 << r_rem
    
    min_diff = x * pow2_s + r_rem - (y * pow2_r + s_rem * pow2_r)
    max_diff = x * pow2_s + r_rem * pow2_s - (y * pow2_r + s_rem)
    
    return min_diff <= 0 and max_diff >= 0

class SearchSolver:
    def __init__(self, r_target, s_target):
        self.R = r_target
        self.S = s_target
        self.memo = {}

    def count_paths(self, x, y, r_used, s_used):
        if r_used == self.R and s_used == self.S:
            return 1 if x == y else 0
        if x == y:
            return 0
            
        r_rem = self.R - r_used
        s_rem = self.S - s_used
        
        if not can_reach_zero(x, y, r_rem, s_rem):
            return 0
            
        key = (x, y, r_used, s_used)
        if key in self.memo:
            return self.memo[key]
            
        total = 0
        if r_used < self.R:
            total += self.count_paths(x + 1, y * 2, r_used + 1, s_used)
            total = min(2, total)
            
        if s_used < self.S and total < 2:
            total += self.count_paths(x * 2, y + 1, r_used, s_used + 1)
            total = min(2, total)
            
        self.memo[key] = total
        return total

    def reconstruct_one_path(self):
        path = []
        x = kStartX
        y = kStartY
        r_used = 0
        s_used = 0
        
        while r_used < self.R or s_used < self.S:
            moved = False
            if r_used < self.R and self.count_paths(x + 1, y * 2, r_used + 1, s_used) > 0:
                path.append('r')
                x += 1
                y *= 2
                r_used += 1
                moved = True
            elif s_used < self.S and self.count_paths(x * 2, y + 1, r_used, s_used + 1) > 0:
                path.append('s')
                x *= 2
                y += 1
                s_used += 1
                moved = True
                
            if not moved:
                return None
                
        return "".join(path)

def apply_path_and_final_value(path):
    x = kStartX
    y = kStartY
    for i, char in enumerate(path):
        if char == 'r':
            x += 1
            y *= 2
        else:
            x *= 2
            y += 1
            
        if i + 1 < len(path) and x == y:
            return 0
            
    return x if x == y else 0

def solve():
    for m in range(0, kMaxM + 1, 2):
        found = False
        best_count = 0
        best_final_value = 0
        
        for r_target in range(m + 1):
            s_target = m - r_target
            
            solver = SearchSolver(r_target, s_target)
            c = solver.count_paths(kStartX, kStartY, 0, 0)
            
            if c == 0:
                continue
                
            path = solver.reconstruct_one_path()
            if not path:
                continue
                
            final_value = apply_path_and_final_value(path)
            if final_value == 0:
                continue
                
            if not found:
                found = True
                best_count = c
                best_final_value = final_value
            else:
                best_count = 2
                
        if found:
            if best_count == 1:
                return str(best_final_value)
    
    return None

if __name__ == "__main__":
    print(solve())
