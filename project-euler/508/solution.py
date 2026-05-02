MOD = 1000000007
BRUTE_LIMIT = 1024

def floor_div(a, b):
    q = a // b
    return q

def ceil_div(a, b):
    return -floor_div(-a, b)

def count_even_odd(l, r):
    if l > r: return 0, 0
    first_even = l if l % 2 == 0 else l + 1
    last_even = r if r % 2 == 0 else r - 1
    if first_even > last_even:
        even = 0
    else:
        even = (last_even - first_even) // 2 + 1
    odd = (r - l + 1) - even
    return even, odd

def mod_add(a, b):
    return (a + b) % MOD

def ones_in_base(a, b):
    count = 0
    while a != 0 or b != 0:
        r = (a - b) & 1
        count += r
        na = (b - a + r) // 2
        nb = (r - a - b) // 2
        a, b = na, nb
    return count

class Solver:
    def __init__(self):
        self.memo_b = {}
        self.memo_a = {}
        
    def brute_b(self, amin, amax, bmin, bmax):
        total = 0
        for a in range(amin, amax + 1):
            for b in range(bmin, bmax + 1):
                total += ones_in_base(a, b)
        return total % MOD

    def sum_b(self, amin, amax, bmin, bmax):
        if amin > amax or bmin > bmax:
            return 0
        key = (amin, amax, bmin, bmax)
        if key in self.memo_b:
            return self.memo_b[key]
            
        area = (amax - amin + 1) * (bmax - bmin + 1)
        if area <= BRUTE_LIMIT:
            res = self.brute_b(amin, amax, bmin, bmax)
            self.memo_b[key] = res
            return res
            
        a_even, a_odd = count_even_odd(amin, amax)
        b_even, b_odd = count_even_odd(bmin, bmax)
        
        odd_pairs = a_even * b_odd + a_odd * b_even
        res = odd_pairs % MOD
        
        u0_min = -amax
        u0_max = -amin
        u1_min = 1 - amax
        u1_max = 1 - amin
        
        res = mod_add(res, self.sum_a(u0_min, u0_max, bmin, bmax))
        res = mod_add(res, self.sum_a(u1_min, u1_max, bmin, bmax))
        
        self.memo_b[key] = res
        return res

    def sum_a(self, umin, umax, vmin, vmax):
        if umin > umax or vmin > vmax:
            return 0
        key = (umin, umax, vmin, vmax)
        if key in self.memo_a:
            return self.memo_a[key]
            
        u_even, u_odd = count_even_odd(umin, umax)
        v_even, v_odd = count_even_odd(vmin, vmax)
        
        odd_pairs = u_odd * v_odd
        res = odd_pairs % MOD
        
        if u_even > 0 and v_even > 0:
            x_min = ceil_div(umin, 2)
            x_max = floor_div(umax, 2)
            y_min = ceil_div(vmin, 2)
            y_max = floor_div(vmax, 2)
            if x_min <= x_max and y_min <= y_max:
                res = mod_add(res, self.sum_b(-y_max, -y_min, -x_max, -x_min))
                
        if u_odd > 0 and v_odd > 0:
            x_min = ceil_div(umin - 1, 2)
            x_max = floor_div(umax - 1, 2)
            y_min = ceil_div(vmin - 1, 2)
            y_max = floor_div(vmax - 1, 2)
            if x_min <= x_max and y_min <= y_max:
                res = mod_add(res, self.sum_b(-y_max, -y_min, -x_max, -x_min))
                
        self.memo_a[key] = res
        return res

    def compute_square(self, L):
        return self.sum_b(-L, L, -L, L)

def compute_parallel(L):
    solver = Solver()
    return solver.compute_square(L) % MOD

def solve():
    L = 1000000000000000
    ans = compute_parallel(L)
    return str(ans)

if __name__ == '__main__':
    print(solve())
