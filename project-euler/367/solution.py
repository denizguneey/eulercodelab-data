import math
from collections import defaultdict

def generate_partitions(n):
    parts = []
    def dfs(rem, max_part, cur):
        if rem == 0:
            parts.append(list(cur))
            return
        for x in range(min(rem, max_part), 0, -1):
            cur.append(x)
            dfs(rem - x, x, cur)
            cur.pop()
    dfs(n, n, [])
    return parts

def build_representative_permutation(n, partition):
    perm = [0] * n
    cur = 0
    for length in partition:
        if length == 1:
            perm[cur] = cur
            cur += 1
            continue
        for i in range(length - 1):
            perm[cur + i] = cur + i + 1
        perm[cur + length - 1] = cur
        cur += length
    return perm

def cycle_type_partition(perm):
    n = len(perm)
    vis = [False] * n
    lengths = []
    for i in range(n):
        if vis[i]: continue
        j = i
        length = 0
        while not vis[j]:
            vis[j] = True
            j = perm[j]
            length += 1
        lengths.append(length)
    lengths.sort(reverse=True)
    return tuple(lengths)

def factorial(n):
    return math.factorial(n)

def class_size(n, partition):
    num = factorial(n)
    freq = defaultdict(int)
    for length in partition:
        freq[length] += 1
    
    den = 1
    for length, cnt in freq.items():
        if cnt == 0: continue
        den *= (length ** cnt)
        den *= factorial(cnt)
        
    return num // den

def solve_average_expectation(n):
    partitions = generate_partitions(n)
    ccount = len(partitions)
    
    class_index = {tuple(p): i for i, p in enumerate(partitions)}
    reps = [build_representative_permutation(n, p) for p in partitions]
    
    identity_partition = tuple([1] * n)
    id_idx = class_index[identity_partition]
    
    unknown_classes = [i for i in range(ccount) if i != id_idx]
    m = len(unknown_classes)
    
    trans_total = n * (n - 1) // 2
    cycle3_total = n * (n - 1) * (n - 2) // 3
    
    a = [[0.0] * (m + 1) for _ in range(m)]
    
    for ri in range(m):
        cls = unknown_classes[ri]
        perm = reps[cls]
        
        cnt2 = [0] * ccount
        cnt3 = [0] * ccount
        
        for x in range(n):
            for y in range(x + 1, n):
                q = list(perm)
                q[x], q[y] = q[y], q[x]
                to = class_index[cycle_type_partition(q)]
                cnt2[to] += 1
                
        for x in range(n):
            for y in range(x + 1, n):
                for z in range(y + 1, n):
                    q = list(perm)
                    px, py, pz = q[x], q[y], q[z]
                    q[x], q[y], q[z] = py, pz, px
                    to = class_index[cycle_type_partition(q)]
                    cnt3[to] += 1
                    
                    q = list(perm)
                    q[x], q[y], q[z] = pz, px, py
                    to = class_index[cycle_type_partition(q)]
                    cnt3[to] += 1
                    
        for cj in range(m):
            cls_to = unknown_classes[cj]
            p2 = cnt2[cls_to] / trans_total
            p3 = cnt3[cls_to] / cycle3_total
            
            coef = -0.5 * p2 - (1.0 / 3.0) * p3
            if cls == cls_to:
                coef += 5.0 / 6.0
            a[ri][cj] = coef
            
        a[ri][m] = 1.0
        
    for col in range(m):
        pivot = col
        for r in range(col + 1, m):
            if abs(a[r][col]) > abs(a[pivot][col]):
                pivot = r
        a[col], a[pivot] = a[pivot], a[col]
        
        pv = a[col][col]
        for j in range(col, m + 1):
            a[col][j] /= pv
            
        for r in range(m):
            if r == col: continue
            factor = a[r][col]
            if abs(factor) < 1e-30: continue
            for j in range(col, m + 1):
                a[r][j] -= factor * a[col][j]
                
    h = [0.0] * ccount
    for ri in range(m):
        cls = unknown_classes[ri]
        h[cls] = a[ri][m]
    h[id_idx] = 0.0
    
    total_perm = factorial(n)
    weighted_sum = 0.0
    for i in range(ccount):
        sz = class_size(n, partitions[i])
        weighted_sum += sz * h[i]
        
    return weighted_sum / total_perm

def solve():
    avg11 = solve_average_expectation(11)
    ans = round(avg11)
    return str(ans)

if __name__ == '__main__':
    print(solve())
