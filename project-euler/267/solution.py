import math

def binomial_tail_probability(n, k_min):
    if k_min <= 0:
        return 1.0
    if k_min > n:
        return 0.0
        
    prob = [0.0] * (n + 1)
    # math.ldexp is available in math package but pow(2.0, -n) is also fine
    prob[0] = math.ldexp(1.0, -n)
    
    for k in range(n):
        prob[k + 1] = prob[k] * (n - k) / (k + 1)
        
    return sum(prob[k_min : n + 1])

def minimum_wins_needed(n, target):
    ln_target = math.log(target)
    for k in range(n + 1):
        best_gain = -1.0e300
        if k == n:
            best_gain = n * math.log(3.0)
        else:
            f_star = (3.0 * k - n) / (2.0 * n)
            if 0.0 < f_star < 1.0:
                best_gain = k * math.log(1.0 + 2.0 * f_star) + (n - k) * math.log(1.0 - f_star)
            elif f_star <= 0.0:
                best_gain = 0.0
                
        if best_gain >= ln_target:
            return k
            
    return n + 1

def solve_probability(tosses, target):
    k_min = minimum_wins_needed(tosses, target)
    return binomial_tail_probability(tosses, k_min)

def solve():
    ans = solve_probability(1000, 1.0e9)
    return f"{ans:.12f}"

if __name__ == '__main__':
    print(solve())
