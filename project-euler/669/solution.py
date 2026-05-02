def knight_from_right(right_pos, fk, fk_minus_1):
    if right_pos == 1:
        return fk
    m = right_pos // 2
    t = (m * fk_minus_1) % fk
    if right_pos % 2 == 0:
        v = t
    else:
        v = (fk - t) % fk
    if v == 0:
        v = fk
    return v

def solve():
    fib = [0] * 85
    fib[1] = 1
    fib[2] = 1
    for i in range(3, 85):
        fib[i] = fib[i - 1] + fib[i - 2]
        
    n = fib[83]
    left_pos = 10000000000000000
    right_pos = n - left_pos + 1
    
    ans = knight_from_right(right_pos, n, fib[82])
    return str(ans)

if __name__ == '__main__':
    print(solve())
