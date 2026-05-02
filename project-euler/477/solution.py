def compute_score(seq):
    stack = []
    total_sum = 0
    
    for v in seq:
        total_sum += v
        stack.append(v)
        while len(stack) >= 3:
            a = stack[-3]
            b = stack[-2]
            c = stack[-1]
            if b < a or b < c:
                break
            stack[-3] = a - b + c
            stack.pop()
            stack.pop()
            
    delta = 0
    i = 0
    j = len(stack) - 1
    sign = 1
    
    while stack and i <= j:
        if stack[i] > stack[j]:
            delta += sign * stack[i]
            i += 1
        else:
            delta += sign * stack[j]
            if j == 0:
                break
            j -= 1
        sign = -sign
        
    return (total_sum + delta) // 2

def solve_n(n):
    if n == 0:
        return 0
        
    kMod = 1000000007
    seen = {}
    prefix = []
    
    s = 0
    cycle_start = -1
    cycle_len = 0
    
    for i in range(n):
        if s in seen:
            cycle_start = seen[s]
            cycle_len = len(prefix) - cycle_start
            break
        seen[s] = len(prefix)
        prefix.append(s)
        s = (s * s + 45) % kMod
        
    if cycle_start < 0:
        return compute_score(prefix)
        
    p = cycle_start
    c_len = cycle_len
    
    a = (n - p) % c_len
    b = c_len - a
    
    U = prefix[:p] + prefix[p:p+a]
    V = prefix[p+a:p+a+b] + prefix[p:p+a]
    T = U + V
    
    s1 = compute_score(U)
    s2 = compute_score(T)
    
    u_len = len(U)
    v_len = len(V)
    blocks = (n - u_len) // v_len
    
    result = s1 + (s2 - s1) * blocks
    return result

def solve():
    n = 100000000
    return str(solve_n(n))

if __name__ == '__main__':
    print(solve())
