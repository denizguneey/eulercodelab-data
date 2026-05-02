import math
from typing import Set, List

def generate_distinct_sums(limit: int) -> Set[int]:
    adj = [[] for _ in range(limit + 1)]
    
    m_max = int(math.isqrt(2 * limit)) + 4
    for m in range(2, m_max + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            if (m - n) % 3 == 0:
                continue
            
            x0 = m * m - n * n
            y0 = n * (2 * m + n)
            if x0 <= 0 or y0 <= 0:
                continue
            
            if x0 > limit or y0 > limit:
                continue
            
            k = 1
            while True:
                x = k * x0
                y = k * y0
                if x > limit or y > limit:
                    break
                
                adj[x].append(y)
                adj[y].append(x)
                k += 1
    
    for i in range(len(adj)):
        adj[i].sort()
        adj[i] = list(dict.fromkeys(adj[i]))  # Remove duplicates while preserving order
    
    sums: Set[int] = set()
    
    for p in range(1, limit + 1):
        vp = adj[p]
        if len(vp) < 2:
            continue
        
        for q in vp:
            if q <= p:
                continue
            if p + q >= limit:
                continue
            
            vq = adj[q]
            
            # Find first element > q in both lists
            it_p_idx = 0
            while it_p_idx < len(vp) and vp[it_p_idx] <= q:
                it_p_idx += 1
            
            it_q_idx = 0
            while it_q_idx < len(vq) and vq[it_q_idx] <= q:
                it_q_idx += 1
            
            while it_p_idx < len(vp) and it_q_idx < len(vq):
                if vp[it_p_idx] == vq[it_q_idx]:
                    r = vp[it_p_idx]
                    s = p + q + r
                    if s <= limit:
                        sums.add(s)
                    it_p_idx += 1
                    it_q_idx += 1
                elif vp[it_p_idx] < vq[it_q_idx]:
                    it_p_idx += 1
                else:
                    it_q_idx += 1
    
    return sums

def solve(limit: int) -> int:
    sums = generate_distinct_sums(limit)
    return sum(sums)

def brute_small(limit: int) -> int:
    def is_square(x: int) -> bool:
        r = int(math.isqrt(x))
        return r * r == x or (r + 1) * (r + 1) == x
    
    sums: Set[int] = set()
    
    for p in range(1, limit + 1):
        for q in range(p + 1, limit - p + 1):
            if not is_square(p * p + p * q + q * q):
                continue
            for r in range(q + 1, limit - p - q + 1):
                if is_square(p * p + p * r + r * r) and is_square(q * q + q * r + r * r):
                    sums.add(p + q + r)
    
    return sum(sums)

def run_checkpoints() -> bool:
    sums_1000 = generate_distinct_sums(1000)
    if 784 not in sums_1000:
        print("Checkpoint failed: 784 not generated for limit 1000", file=__import__('sys').stderr)
        return False
    if solve(1000) != 784:
        print("Checkpoint failed for limit 1000", file=__import__('sys').stderr)
        return False
    if solve(1500) != brute_small(1500):
        print("Checkpoint failed for brute-force cross-check limit 1500", file=__import__('sys').stderr)
        return False
    return True

def main():
    import sys
    
    limit = 120000
    run_checkpoints_flag = True
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--limit="):
            try:
                limit = int(arg[8:])
            except ValueError:
                print(f"Unknown argument: {arg}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
        i += 1
    
    if limit < 3:
        print("Limit must be at least 3", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
