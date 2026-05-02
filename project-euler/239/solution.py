def combination(n, k):
    if k < 0 or k > n:
        return 0.0
    k = min(k, n - k)
    value = 1.0
    for i in range(1, k + 1):
        value *= (n - k + i)
        value /= i
    return value

def probability_exact_marked_fixed(n, marked, fixed_marked):
    if n < 0 or marked < 0 or marked > n:
        return 0.0
    if fixed_marked < 0 or fixed_marked > marked:
        return 0.0
        
    bad_marked = marked - fixed_marked
    
    term = 1.0
    for i in range(fixed_marked):
        term /= (n - i)
        
    alternating_sum = term
    for j in range(bad_marked):
        numer = -(bad_marked - j)
        denom = (j + 1) * (n - fixed_marked - j)
        term *= numer / denom
        alternating_sum += term
        
    return combination(marked, fixed_marked) * alternating_sum

def solve(n=100, marked=25, misplaced_marked=22):
    fixed_marked = marked - misplaced_marked
    answer = probability_exact_marked_fixed(n, marked, fixed_marked)
    return f"{answer:.12f}"

if __name__ == '__main__':
    print(solve())
