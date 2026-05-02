import math

def solve(defects, chips):
    if defects <= 2:
        return 0.0

    answer = 1.0
    
    logp = 0.0
    for j in range(defects):
        logp += math.log(1.0 - float(j) / float(chips))
        
    answer -= math.exp(logp)

    for i in range(1, defects // 2 + 1):
        num_term1 = float(defects - 2 * (i - 1)) * float(defects - 1 - 2 * (i - 1))
        den_term1 = 2.0 * float(chips) * float(i)
        
        term2_j = defects - i
        term2_val = 1.0 - float(term2_j) / float(chips)
        
        logp += math.log(num_term1 / den_term1) - math.log(term2_val)
        
        answer -= math.exp(logp)

    return answer

def solve_problem():
    ans = solve(20000, 1000000)
    return "{:.10f}".format(ans)

if __name__ == '__main__':
    print(solve_problem())
