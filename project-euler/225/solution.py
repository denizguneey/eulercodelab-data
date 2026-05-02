def divides_tribonacci(n):
    def next_state(a, b, c):
        return b, c, (a + b + c) % n

    start_a, start_b, start_c = 1 % n, 1 % n, 1 % n
    
    t_a, t_b, t_c = next_state(start_a, start_b, start_c)
    h_a, h_b, h_c = next_state(*next_state(start_a, start_b, start_c))

    if t_c == 0 or h_c == 0:
        return True

    while not (t_a == h_a and t_b == h_b and t_c == h_c):
        t_a, t_b, t_c = next_state(t_a, t_b, t_c)
        
        h_a, h_b, h_c = next_state(h_a, h_b, h_c)
        h_a, h_b, h_c = next_state(h_a, h_b, h_c)
        
        if t_c == 0 or h_c == 0:
            return True

    cur_a, cur_b, cur_c = t_a, t_b, t_c
    while True:
        if cur_c == 0:
            return True
        cur_a, cur_b, cur_c = next_state(cur_a, cur_b, cur_c)
        if cur_a == t_a and cur_b == t_b and cur_c == t_c:
            break

    return False

def solve():
    target = 124
    found = 0
    n = 1
    
    while found < target:
        n += 2
        if not divides_tribonacci(n):
            found += 1
            
    return str(n)

if __name__ == '__main__':
    print(solve())
