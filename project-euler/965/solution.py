def compute_F(N):
    a = 0
    b = 1
    c = 1
    d = N
    
    total_sum = 0.0
    compensation = 0.0
    
    while c <= N:
        term = 1.0 / (2.0 * b * d * d)
        
        y = term - compensation
        t = total_sum + y
        compensation = (t - total_sum) - y
        total_sum = t
        
        k = (N + b) // d
        next_c = k * c - a
        next_d = k * d - b
        a, b = c, d
        c, d = next_c, next_d
        
    return total_sum

def nearly_equal(x, y, eps):
    return abs(x - y) <= eps

def run_checkpoints():
    assert nearly_equal(compute_F(1), 0.5, 1e-15)
    assert nearly_equal(compute_F(4), 0.25, 1e-15)
    assert nearly_equal(compute_F(10), 19.0 / 144.0, 1e-15)

def solve():
    ans = compute_F(10000)
    return f"{ans:.13f}"

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
