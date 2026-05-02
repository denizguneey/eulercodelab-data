# Problem 159: Digital root clocks / Maximum Digital Root Sum (MDRS)

def solve():
    limit = 1000000
    
    def digital_root(n):
        if n == 0: return 0
        return 1 + (n - 1) % 9
    
    mdrs = [0] * limit
    for n in range(1, limit):
        mdrs[n] = digital_root(n)
    
    for a in range(2, limit):
        p = a * 2
        while p < limit:
            b = p // a
            cand = mdrs[a] + mdrs[b]
            if cand > mdrs[p]:
                mdrs[p] = cand
            p += a
    
    print(sum(mdrs[2:]))

solve()
