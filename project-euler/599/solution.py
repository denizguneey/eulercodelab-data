import math
from collections import Counter
from itertools import product

def get_parts(n, max_val=8):
    if n == 0: return [[]]
    res = []
    for i in range(min(n, max_val), 0, -1):
        for p in get_parts(n - i, i):
            res.append([i] + p)
    return res

def count_perms(p):
    cnt = math.factorial(8)
    counts = Counter(p)
    for k, v in counts.items():
        cnt //= (k ** v) * math.factorial(v)
    return cnt

def solve_m(m):
    parts = get_parts(8, 8)
    total = 0
    
    for p in parts:
        perms = count_perms(p)
        k = len(p)
        w_inner = 3 ** (8 - k)
        
        for seq in product(range(3), repeat=k):
            if sum(seq) % 3 != 0: continue
            
            c_g = 0
            for S in seq:
                if S == 0:
                    c_g += 3
                else:
                    c_g += 1
            total += perms * w_inner * (m ** c_g)
            
    return total // 88179840

def solve():
    return str(solve_m(10))

if __name__ == '__main__':
    print(solve())
