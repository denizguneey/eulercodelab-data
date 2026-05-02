import math

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def is_one_less_than_power_of_two(n):
    return n >= 1 and ((n + 1) & n) == 0

def highest_power_of_two_at_most(n):
    p = 1
    while (p << 1) <= n:
        p <<= 1
    return p

def log_k_infty(n):
    if n == 0:
        return (math.log(2) + 2 * math.log(4) + math.log(6)) / 4
        
    b = (1 << n) - 1
    
    if is_one_less_than_power_of_two(n):
        return (math.log(2) + 2 * math.log(b)) / 5
        
    if is_power_of_two(n):
        return math.log(b) / 2 + (math.log(b - 1) + math.log(b + 1)) / 12
        
    p = highest_power_of_two_at_most(n)
    q = p << 1
    e = q - n
    c = (1 << e) - 1
    
    return math.log(b) / 3 + math.log(c) / 6 + (math.log(c - 1) + math.log(c + 1)) / 12

def solve():
    sum_logs = 0.0
    for n in range(51):
        sum_logs += log_k_infty(n)
        
    ans = math.exp(sum_logs / 51.0)
    return f"{ans:.6f}"

if __name__ == "__main__":
    print(solve())
