import math

def minimal_n(p, q, target_nines):
    beta = math.sqrt(q) - math.sqrt(p)
    beta2 = beta * beta
    lam = -math.log10(beta2)
    target = float(target_nines)
    
    n = int(target / lam)
    if n == 0:
        n = 1
    while n * lam < target - 1e-15:
        n += 1
    while n > 1 and (n - 1) * lam >= target - 1e-15:
        n -= 1
    return n

def solve(max_sum=2011, target_nines=2011):
    total = 0
    for p in range(1, max_sum):
        for q in range(p + 1, max_sum - p + 1):
            beta = math.sqrt(q) - math.sqrt(p)
            if beta >= 1.0:
                continue
            total += minimal_n(p, q, target_nines)
    return str(total)

if __name__ == '__main__':
    print(solve())
