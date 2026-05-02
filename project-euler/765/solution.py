import decimal

def optimal_success_probability(rounds, p_win, target):
    decimal.getcontext().prec = 50
    
    if target <= 1:
        return decimal.Decimal(1)
        
    budget_q = decimal.Decimal(1) / decimal.Decimal(str(target))
    
    q = [decimal.Decimal(0)] * (rounds + 1)
    q[0] = decimal.Decimal(1) / (decimal.Decimal(2) ** rounds)
    for w in range(rounds):
        q[w + 1] = q[w] * decimal.Decimal(rounds - w) / decimal.Decimal(w + 1)
        
    p = [decimal.Decimal(0)] * (rounds + 1)
    dp_win = decimal.Decimal(str(p_win))
    one_minus_p = decimal.Decimal(1) - dp_win
    base = (decimal.Decimal(2) * one_minus_p) ** rounds
    ratio = dp_win / one_minus_p
    ratio_pow = decimal.Decimal(1)
    
    for w in range(rounds + 1):
        p[w] = q[w] * base * ratio_pow
        ratio_pow *= ratio
        
    used_q = decimal.Decimal(0)
    success_p = decimal.Decimal(0)
    boundary_w = -1
    eps = decimal.Decimal('1e-30')
    
    for w in range(rounds, -1, -1):
        candidate_q = used_q + q[w]
        if candidate_q <= budget_q + eps:
            used_q = candidate_q
            success_p += p[w]
        else:
            boundary_w = w
            break
            
    if boundary_w == -1:
        return decimal.Decimal(1)
        
    frac = (budget_q - used_q) / q[boundary_w]
    if frac < decimal.Decimal(0): frac = decimal.Decimal(0)
    if frac > decimal.Decimal(1): frac = decimal.Decimal(1)
    
    success_p += frac * p[boundary_w]
    return success_p

def solve():
    ans = optimal_success_probability(1000, 0.6, 1000000000000.0)
    return f"{ans:.10f}"

if __name__ == "__main__":
    print(solve())
