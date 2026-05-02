def ratio_binom_drop(a, drop, choose_r):
    ratio = 1.0
    for j in range(choose_r):
        ratio *= float(a - drop - j) / float(a - j)
    return ratio

def expected_second_shortest(n, m):
    r = m - 1
    a_r = n - 1
    a_s = n - 1
    ratio_r = 1.0
    ratio_s = 1.0
    
    answer = 0.0
    while True:
        tail = float(m) * ratio_r - float(m - 1) * ratio_s
        answer += tail
        
        has_next = False
        if a_r - (m - 1) >= r:
            ratio_r *= ratio_binom_drop(a_r, m - 1, r)
            a_r -= (m - 1)
            has_next = True
        else:
            ratio_r = 0.0
            
        if a_s - m >= r:
            ratio_s *= ratio_binom_drop(a_s, m, r)
            a_s -= m
            has_next = True
        else:
            ratio_s = 0.0
            
        if not has_next:
            break
            
    return answer

def solve():
    n = 10000000
    m = 100
    ans = expected_second_shortest(n, m)
    return "{:.5f}".format(ans)

if __name__ == '__main__':
    print(solve())
