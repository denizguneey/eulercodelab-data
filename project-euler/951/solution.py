def F(n):
    m = 2 * n
    
    cur = {}
    cur[(1, 1, 2, -1)] = 1
    cur[(0, 0, 2, -1)] = 1
    
    for length in range(1, m):
        nxt = {}
        for (r, first, a, b), ways in cur.items():
            b_cnt = length - r
            
            if r < n:
                ai = -(a + 2 * b) if first == 1 else -2 * a
                nk = (r + 1, 1, ai, a)
                nxt[nk] = nxt.get(nk, 0) + ways
                
            if b_cnt < n:
                ai = -(a + 2 * b) if first == 0 else -2 * a
                nk = (r, 0, ai, a)
                nxt[nk] = nxt.get(nk, 0) + ways
                
        cur = nxt
        
    ans = 0
    for (r, _, a, _), ways in cur.items():
        if r == n and a == 0:
            ans += ways
            
    return ans

def solve():
    return str(F(26))

if __name__ == "__main__":
    assert F(2) == 4
    assert F(8) == 11892
    print(solve())
