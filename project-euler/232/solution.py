def compute_t_limit(target):
    t = 1
    score = 1
    while score < target and t < 60:
        t += 1
        score <<= 1
    return t + 4

def p1_turn_value(f, a, b):
    if a <= 0: return 0.0
    if b <= 0: return 1.0
    prev_row = 0.0 if a == 1 else f[a - 1][b]
    return 0.5 * (f[a][b] + prev_row)

def solve(target=100):
    f = [[0.0] * (target + 1) for _ in range(target + 1)]
    
    for a in range(1, target + 1):
        f[a][0] = 1.0
        
    t_limit = compute_t_limit(target)
    q = [0.0] * (t_limit + 1)
    score = [0] * (t_limit + 1)
    
    for t in range(1, t_limit + 1):
        q[t] = 2.0 ** (-t)
        score[t] = 1 << (t - 1)
        
    for a in range(1, target + 1):
        for b in range(1, target + 1):
            prev_same_b = 0.0 if a == 1 else f[a - 1][b]
            best_value = 0.0
            
            for t in range(1, t_limit + 1):
                gain = score[t]
                if gain >= b:
                    success_value = 1.0
                else:
                    success_value = p1_turn_value(f, a, b - gain)
                    
                qt = q[t]
                candidate = (2.0 * qt * success_value + (1.0 - qt) * prev_same_b) / (1.0 + qt)
                
                if candidate > best_value:
                    best_value = candidate
                    
            f[a][b] = best_value
            
    ans = p1_turn_value(f, target, target)
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
