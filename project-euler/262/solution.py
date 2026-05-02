import sys
import math
import heapq
from concurrent.futures import ThreadPoolExecutor

def compute_height(x, y):
    xx = x * x
    yy = y * y
    xy = x * y
    base = 5000.0 - 0.005 * (xx + yy + xy) + 12.5 * (x + y)
    expo = -abs(0.000001 * (xx + yy) - 0.0015 * (x + y) + 0.7)
    return base * math.exp(expo)

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def quantize(p, scale):
    return (round(p[0] * scale), round(p[1] * scale))

def from_key(k, scale):
    return (k[0] / scale, k[1] / scale)

def interp(p1, p2, v1, v2, f):
    denom = v2 - v1
    if abs(denom) < 1e-14:
        t = 0.5
    else:
        t = (f - v1) / denom
        if t < 0.0: t = 0.0
        if t > 1.0: t = 1.0
    return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))

def worker_heights(row_start, row_end, n, step):
    local_heights = {}
    for i in range(row_start, row_end):
        x = i * step
        base = i * n
        for j in range(n):
            y = j * step
            local_heights[base + j] = compute_height(x, y)
    return local_heights

def minimax_height(heights, n, start_idx, goal_idx):
    inf = float('inf')
    best = [inf] * len(heights)
    
    pq = []
    best[start_idx] = heights[start_idx]
    heapq.heappush(pq, (best[start_idx], start_idx))
    
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while pq:
        cost, idx = heapq.heappop(pq)
        if cost != best[idx]:
            continue
        if idx == goal_idx:
            return cost
            
        i = idx // n
        j = idx % n
        for di, dj in dirs:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                nidx = ni * n + nj
                nxt = max(cost, heights[nidx])
                if nxt < best[nidx]:
                    best[nidx] = nxt
                    heapq.heappush(pq, (nxt, nidx))
    return inf

def visible(a, b, f, step):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    dist_ab = math.hypot(dx, dy)
    if dist_ab == 0.0:
        return True
    samples = max(1, int(dist_ab / step))
    for s in range(1, samples):
        t = s / samples
        x = a[0] + dx * t
        y = a[1] + dy * t
        if compute_height(x, y) > f + 1e-10:
            return False
    return True

def solve():
    kMaxCoord = 1600
    grid_step = 1.0
    vis_step = 0.5
    threads = 4  # Adjust based on logic, Python threading is GIL limited, but computation is isolated if we use ProcessPool, however ThreadPool is easier and math is somewhat fast here. Wait, actually we can just sequentially do it or use ProcessPool.
    
    import multiprocessing
    threads = multiprocessing.cpu_count() or 1
    
    n = int(kMaxCoord / grid_step) + 1
    heights = [0.0] * (n * n)
    
    # Compute heights
    import os
    if threads > 1 and os.name == 'posix':
        with multiprocessing.Pool(threads) as pool:
            chunk = (n + threads - 1) // threads
            args = []
            for t in range(threads):
                start = t * chunk
                end = min(n, start + chunk)
                if start < end:
                    args.append((start, end, n, grid_step))
            results = pool.starmap(worker_heights, args)
            for res_dict in results:
                for idx, h in res_dict.items():
                    heights[idx] = h
    else:
        for idx, h in worker_heights(0, n, n, grid_step).items():
            heights[idx] = h
            
    A = (200.0, 200.0)
    B = (1400.0, 1400.0)
    start_idx = int(A[0] / grid_step) * n + int(A[1] / grid_step)
    goal_idx = int(B[0] / grid_step) * n + int(B[1] / grid_step)
    
    f_min = minimax_height(heights, n, start_idx, goal_idx)
    
    inside = [0] * (n * n)
    for idx in range(len(heights)):
        if heights[idx] > f_min:
            inside[idx] = 1
            
    kCaseCount = [0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0]
    kCaseEdges = [
        [(-1, -1), (-1, -1)],
        [(3, 0), (-1, -1)],
        [(0, 1), (-1, -1)],
        [(3, 1), (-1, -1)],
        [(1, 2), (-1, -1)],
        [(3, 2), (0, 1)],
        [(0, 2), (-1, -1)],
        [(3, 2), (-1, -1)],
        [(2, 3), (-1, -1)],
        [(0, 2), (-1, -1)],
        [(0, 1), (2, 3)],
        [(1, 2), (-1, -1)],
        [(3, 1), (-1, -1)],
        [(0, 1), (-1, -1)],
        [(3, 0), (-1, -1)],
        [(-1, -1), (-1, -1)]
    ]
    
    segments = []
    for i in range(n - 1):
        x = i * grid_step
        for j in range(n - 1):
            y = j * grid_step
            idx_ll = i * n + j
            idx_lr = (i + 1) * n + j
            idx_ur = (i + 1) * n + (j + 1)
            idx_ul = i * n + (j + 1)
            
            mask = (inside[idx_ll] | (inside[idx_lr] << 1) | (inside[idx_ur] << 2) | (inside[idx_ul] << 3))
            if mask == 0 or mask == 15:
                continue
                
            ll = (x, y)
            lr = (x + grid_step, y)
            ur = (x + grid_step, y + grid_step)
            ul = (x, y + grid_step)
            
            v_ll = heights[idx_ll]
            v_lr = heights[idx_lr]
            v_ur = heights[idx_ur]
            v_ul = heights[idx_ul]
            
            edges = [
                interp(ll, lr, v_ll, v_lr, f_min),
                interp(lr, ur, v_lr, v_ur, f_min),
                interp(ul, ur, v_ul, v_ur, f_min),
                interp(ll, ul, v_ll, v_ul, f_min)
            ]
            
            for s in range(kCaseCount[mask]):
                e0, e1 = kCaseEdges[mask][s]
                if e0 < 0 or e1 < 0:
                    continue
                segments.append((edges[e0], edges[e1]))
                
    key_scale = 1e6
    adj = {}
    for seg in segments:
        k1 = quantize(seg[0], key_scale)
        k2 = quantize(seg[1], key_scale)
        if k1 not in adj: adj[k1] = []
        if k2 not in adj: adj[k2] = []
        adj[k1].append(k2)
        adj[k2].append(k1)
        
    visited = set()
    contour_keys = []
    best_perimeter = -1.0
    
    for start_key in adj:
        if start_key in visited:
            continue
            
        loop = []
        prev = (-float('inf'), -float('inf'))
        cur = start_key
        
        while True:
            if cur in visited:
                break
            visited.add(cur)
            loop.append(cur)
            nbrs = adj[cur]
            nxt = nbrs[0]
            if prev == nxt:
                if len(nbrs) > 1:
                    nxt = nbrs[1]
            prev = cur
            cur = nxt
            
        per = 0.0
        for i in range(len(loop)):
            a = from_key(loop[i], key_scale)
            b = from_key(loop[(i + 1) % len(loop)], key_scale)
            per += dist(a, b)
            
        if per > best_perimeter:
            best_perimeter = per
            contour_keys = loop
            
    contour = [from_key(k, key_scale) for k in contour_keys]
    m = len(contour)
    
    prefix = [0.0] * (m + 1)
    for i in range(m):
        prefix[i + 1] = prefix[i] + dist(contour[i], contour[(i + 1) % m])
    perimeter = prefix[m]
    
    visA = []
    visB = []
    distA = [0.0] * m
    distB = [0.0] * m
    
    for i in range(m):
        distA[i] = dist(A, contour[i])
        distB[i] = dist(B, contour[i])
        if visible(A, contour[i], f_min, vis_step): visA.append(i)
        if visible(B, contour[i], f_min, vis_step): visB.append(i)
        
    best = float('inf')
    if visible(A, B, f_min, vis_step):
        best = dist(A, B)
        
    for i in visA:
        for j in visB:
            arc = abs(prefix[j] - prefix[i])
            arc = min(arc, perimeter - arc)
            total = distA[i] + distB[j] + arc
            if total < best:
                best = total
                
    return f"{best:.3f}"

if __name__ == '__main__':
    print(solve())
