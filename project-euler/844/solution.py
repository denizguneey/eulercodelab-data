from collections import deque

kMod = 1405695061

def mod_add(a, b):
    a += b
    if a >= kMod:
        a -= kMod
    return a

def mod_sub(a, b):
    return (a - b) if a >= b else (a + kMod - b)

def mod_mul(a, b):
    return (a * b) % kMod

def mod_pow(a, e):
    r = 1
    while e > 0:
        if e & 1:
            r = mod_mul(r, a)
        a = mod_mul(a, a)
        e >>= 1
    return r

inv2 = mod_pow(2, kMod - 2)
inv6 = mod_pow(6, kMod - 2)

def sum1_prefix(n):
    a = n % kMod
    b = (n + 1) % kMod
    return mod_mul(mod_mul(a, b), inv2)

def sum2_prefix(n):
    a = n % kMod
    b = (n + 1) % kMod
    c = (2 * (n % kMod) + 1) % kMod
    return mod_mul(mod_mul(mod_mul(a, b), c), inv6)

def sum3_prefix(n):
    s1 = sum1_prefix(n)
    return mod_mul(s1, s1)

def range_sum1(l, r):
    if l > r: return 0
    return mod_sub(sum1_prefix(r), sum1_prefix(l - 1))

def range_sum2(l, r):
    if l > r: return 0
    return mod_sub(sum2_prefix(r), sum2_prefix(l - 1))

def range_sum3(l, r):
    if l > r: return 0
    return mod_sub(sum3_prefix(r), sum3_prefix(l - 1))

def max_k_u2(n):
    lo, hi = 0, 2000000000
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        val = mid * mid - mid - 1
        if val <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo

def max_k_u3(n):
    lo, hi = 0, 2000000
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        val = mid * mid * mid - mid * mid - 2 * mid + 1
        if val <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo

def max_k_seed4(n):
    lo, hi = 0, 2000000
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        val = mid * (mid - 1) * (mid * mid - mid - 1) - 1
        if val <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo

def capped_product_except(v, skip, cap):
    prod = 1
    for i in range(len(v)):
        if i == skip: continue
        if prod > cap // v[i]: return False, 0
        prod *= v[i]
    return True, prod

def exact_M_k(k, n):
    q = deque([tuple()])
    seen = {tuple()}
    numbers = {1}
    
    while q:
        cur = q.popleft()
        for x in cur:
            if x <= n: numbers.add(x)
            
        ones = k - len(cur)
        if ones > 0:
            cap = (n + 1) // k
            ok, prod = capped_product_except(cur, -1, cap)
            if ok:
                y = k * prod - 1
                if y <= n:
                    nxt = list(cur)
                    nxt.append(y)
                    nxt.sort()
                    nxt_t = tuple(nxt)
                    if nxt_t not in seen:
                        seen.add(nxt_t)
                        q.append(nxt_t)
                        
        for i in range(len(cur)):
            if i > 0 and cur[i] == cur[i - 1]: continue
            x = cur[i]
            cap = (n + x) // k
            ok, prod_others = capped_product_except(cur, i, cap)
            if not ok: continue
            
            y = k * prod_others - x
            if y == 0: continue
            
            nxt = list(cur[:i] + cur[i + 1:])
            if y > 1:
                import bisect
                bisect.insort(nxt, y)
            if nxt and nxt[-1] > n: continue
            
            nxt_t = tuple(nxt)
            if nxt_t not in seen:
                seen.add(nxt_t)
                q.append(nxt_t)
                
    out = 0
    for x in numbers:
        out = (out + (x % kMod)) % kMod
    return out

def chain_sum_range(l, r, n, k2max, k3max):
    if l > r: return 0
    ans = range_sum1(l, r)
    
    if l <= k2max:
        rr = min(r, k2max)
        cnt = (rr - l + 1) % kMod
        s2 = range_sum2(l, rr)
        s1 = range_sum1(l, rr)
        add = mod_sub(mod_sub(s2, s1), cnt)
        ans = mod_add(ans, add)
        
    if l <= k3max:
        rr = min(r, k3max)
        cnt = (rr - l + 1) % kMod
        s3 = range_sum3(l, rr)
        s2 = range_sum2(l, rr)
        s1 = range_sum1(l, rr)
        add = mod_sub(mod_sub(s3, s2), mod_mul(2, s1))
        add = mod_add(add, cnt)
        ans = mod_add(ans, add)
        
    return ans

def solve():
    K = 10**18
    N = 10**18
    
    k2max = max_k_u2(N)
    k3max = max_k_u3(N)
    k0 = max_k_seed4(N)
    
    exact_to = min(K, k0)
    ans = 0
    for k in range(3, exact_to + 1):
        ans = mod_add(ans, exact_M_k(k, N))
        
    if K > exact_to:
        l = max(3, exact_to + 1)
        ans = mod_add(ans, chain_sum_range(l, K, N, k2max, k3max))
        
    return str(ans)

if __name__ == "__main__":
    print(solve())
