def pow_with_cap(base, exp, cap):
    val = 1
    for _ in range(exp):
        val *= base
        if val > cap: return cap + 1
    return val

def int_root(n, p):
    lo = 1
    hi = 2
    while pow_with_cap(hi, p, n) <= n:
        if hi > n // 2:
            hi = n
            break
        hi *= 2
    
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if pow_with_cap(mid, p, n) <= n:
            lo = mid
        else:
            hi = mid
    return lo

def delta_value(u, p):
    v = u - 1
    D = 1
    vpow = 1
    for m in range(2, p + 2):
        vpow *= v
        D = u * D + vpow
    return D

def max_power_for_limit(n):
    p = 0
    x = 1
    while x <= n // 2:
        x *= 2
        p += 1
    return p

class Candidate:
    def __init__(self, n, d, limit):
        self.n = n
        self.d = d
        self.relevance = limit

def generate_record_candidates(limit):
    if limit < 4: return []
    p_max = max_power_for_limit(limit)
    u_max = [0] * (p_max + 1)
    for p in range(2, p_max + 1):
        u_max[p] = int_root(limit, p)
        
    records = []
    current_best_d = 0
    
    while True:
        found = False
        best_n = 0
        best_d = 0
        
        for p in range(2, p_max + 1):
            umax = u_max[p]
            if umax < 2: continue
            if delta_value(umax, p) <= current_best_d: continue
            
            lo, hi = 2, umax
            while lo < hi:
                mid = (lo + hi) // 2
                if delta_value(mid, p) > current_best_d:
                    hi = mid
                else:
                    lo = mid + 1
                    
            u = lo
            n = pow_with_cap(u, p, limit)
            d = delta_value(u, p)
            if not found or n < best_n or (n == best_n and d > best_d):
                found = True
                best_n = n
                best_d = d
                
        if not found: break
        records.append(Candidate(best_n, best_d, limit))
        current_best_d = best_d
        
    return records

def compute_relevance_bounds(candidates, limit):
    for i, ci in enumerate(candidates):
        best = limit
        for j, cj in enumerate(candidates):
            if cj.d * ci.n <= ci.d * cj.n: continue
            num = cj.d * cj.n * ci.n
            den = cj.d * ci.n - ci.d * cj.n
            r = num // den
            if r < best:
                best = r
        ci.relevance = best

def collect_events(candidates, limit):
    events = set()
    for c in candidates:
        lim = min(limit, c.relevance)
        if lim < c.n: continue
        t = c.n
        while t <= lim:
            events.add(t)
            if t > lim - c.n: break
            t += c.n
    return sorted(list(events))

def alternating_sign_sum(l, r):
    if l > r: return 0
    length = r - l + 1
    if length % 2 == 0: return 0
    return -1 if l % 2 else 1

class Solver542:
    def __init__(self, limit):
        self.limit = limit
        self.candidates = generate_record_candidates(limit)
        compute_relevance_bounds(self.candidates, limit)
        self.events = collect_events(self.candidates, limit)
        
    def S(self, k):
        if k < 4: return 0
        best = 0
        for c in self.candidates:
            if c.n > k: break
            if k > c.relevance: continue
            val = (k // c.n) * c.d
            if val > best: best = val
        return best
        
    def T(self, n):
        if n < 4: return 0
        ans = 0
        current = 4
        s_val = self.S(4)
        event_idx = 0
        events_len = len(self.events)
        
        while current <= n:
            next_event = self.events[event_idx] if event_idx < events_len and self.events[event_idx] <= n else n + 1
            if next_event > current:
                r = min(n, next_event - 1)
                sign = alternating_sign_sum(current, r)
                if sign != 0:
                    ans += sign * s_val
                current = r + 1
                if current > n: break
            s_val = self.S(current)
            event_idx += 1
        return ans

def solve():
    s = Solver542(100000000000000000)
    return str(s.T(100000000000000000))

if __name__ == "__main__":
    print(solve())
