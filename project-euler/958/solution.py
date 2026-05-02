def mod_inv_in_range(a, m):
    a %= m
    if a < 0:
        a += m
    x, y = a, m
    vx, vy = 1, 0
    while x:
        k = y // x
        y %= x
        vy -= k * vx
        x, y = y, x
        vx, vy = vy, vx
    if y != 1:
        return False, 0
    inv = vy + m if vy < 0 else vy
    return True, inv

def solve_f(n):
    steps = 0
    while True:
        ans_steps = steps
        ans_val = n + 1
        d = (steps + 1) // 2
        
        def dfs(a, b, ca, cb, cur_depth):
            nonlocal ans_steps, ans_val
            
            if a > b:
                a, b = b, a
                ca, cb = cb, ca
                
            if cb < 0:
                return
            if ca < 0:
                k = (-ca + b - 1) // b
                ca += k * b
                cb -= k * a
                if cb < 0:
                    return
            if a * ca + b * cb != n:
                return
                
            if cur_depth == d:
                local_a, local_b, local_ca, local_cb = a, b, ca, cb
                if (steps & 1) != 0:
                    local_a *= 2
                    local_b *= 2
                    local_ca *= 2
                    local_cb *= 2
                    local_b -= local_a // 2
                    local_ca += local_cb // 2
                    if local_a * local_ca + local_b * local_cb != 4 * n:
                        return
                        
                norm = local_a * local_a + local_b * local_b
                if norm < n:
                    return
                    
                cross = local_ca * local_b - local_cb * local_a
                k = cross // norm
                local_ca -= k * local_b
                local_cb += k * local_a
                cross -= k * norm
                
                if cross < 0:
                    local_ca += local_b
                    local_cb -= local_a
                    cross += norm
                    
                def check(c_a, c_b):
                    nonlocal ans_steps, ans_val
                    if c_a < 0 or c_b < 0:
                        return
                    if c_a * c_a + c_b * c_b > norm:
                        return
                        
                    x = c_a
                    y = c_b
                    vx = local_a
                    vy = local_b
                    
                    if (steps & 1) != 0:
                        if (vx & 1) != 0 or (y & 1) != 0:
                            return
                        x -= y // 2
                        vy += vx // 2
                        if (vy & 1) != 0 or (x & 1) != 0:
                            return
                        x //= 2
                        y //= 2
                        vx //= 2
                        vy //= 2
                        
                    if x * vx + y * vy != n:
                        return
                        
                    ops = 0
                    while ops <= steps - d and x != 0 and y != 0:
                        if x > y:
                            x, y = y, x
                            vx, vy = vy, vx
                        y -= x
                        vx += vy
                        ops += 1
                        
                    if ops > steps - d:
                        return
                        
                    o = vx + vy - n
                    o %= n
                    if o < 0:
                        o += n
                        
                    ok, inv_o = mod_inv_in_range(o, n)
                    if not ok:
                        return
                        
                    c_ans_steps = cur_depth + ops
                    c_ans_val = min(o, n - o, inv_o, n - inv_o)
                    
                    if c_ans_steps < ans_steps or (c_ans_steps == ans_steps and c_ans_val < ans_val):
                        ans_steps = c_ans_steps
                        ans_val = c_ans_val
                        
                check(local_ca, local_cb)
                local_ca -= local_b
                local_cb += local_a
                check(local_ca, local_cb)
                return
                
            x, y = a, b
            for _ in range(cur_depth, steps // 2):
                if x > y:
                    x, y = y, x
                x += y
                x, y = y, x
            if x > y:
                x, y = y, x
                
            if (steps & 1) != 0:
                if 5 * y * y // 4 + x * y + x * x < n:
                    return
            else:
                if x * x + y * y < n:
                    return
                    
            dfs(b, a + b, cb - ca, ca, cur_depth + 1)
            if 0 < a < b:
                dfs(a, a + b, ca - cb, cb, cur_depth + 1)
                
        dfs(0, 1, 0, n, 0)
        
        if ans_val <= n:
            return ans_val
        steps += 1

def solve():
    return str(solve_f(1000000000039))

if __name__ == "__main__":
    assert solve_f(7) == 2
    assert solve_f(89) == 34
    assert solve_f(8191) == 1856
    print(solve())
