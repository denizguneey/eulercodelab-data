import math

def reduce_solution(X, n):
    while True:
        Xp = 2 * X - 3 * n
        np = -X + 2 * n
        if Xp <= 0 or np <= 0:
            break
        X, n = Xp, np
    return (X, n)

def fundamental_solutions(S):
    reps = set()
    for n in range(1, 501):
        v = 3 * n * n + S
        if v <= 0:
            continue
        x = round(math.sqrt(v))
        for X in range(max(1, x - 2), x + 3):
            if X * X == v:
                reps.add(reduce_solution(X, n))
    return list(reps)

def solve():
    N = 10**100
    cache = {}
    uniq = set()
    
    for S in range(-100, 101):
        if S == 0:
            continue
        diff = abs(S)
        kmax = 100 // diff
        if kmax == 0:
            continue
            
        if S not in cache:
            cache[S] = fundamental_solutions(S)
            
        for rep in cache[S]:
            X, n = rep
            while True:
                m = n + X
                A = m * m - n * n
                B = 2 * m * n + n * n
                C = m * m + m * n + n * n
                if C > N:
                    break
                    
                a0 = min(A, B)
                b0 = max(A, B)
                
                for k in range(1, kmax + 1):
                    c = k * C
                    if c > N:
                        break
                    uniq.add((k * a0, k * b0, c))
                
                Xnxt = 2 * X + 3 * n
                nnxt = X + 2 * n
                X, n = Xnxt, nnxt
                
    return str(len(uniq))

if __name__ == '__main__':
    print(solve())
