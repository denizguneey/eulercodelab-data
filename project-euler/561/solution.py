def v2_factorial(n):
    return n - n.bit_count()

def Q(m, N):
    K = (N + 1) // 2
    T = N // 4
    
    part_odd = m * v2_factorial(K)
    part_mult4 = T + v2_factorial(T)
    return part_odd + part_mult4

def solve():
    m = 904961
    N = 1000000000000
    return str(Q(m, N))

if __name__ == '__main__':
    print(solve())
