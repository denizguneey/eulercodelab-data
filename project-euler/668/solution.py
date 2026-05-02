def solve_case(n):
    r = int(n**0.5)
    V = [n // i for i in range(1, r + 1)]
    for i in range(V[-1] - 1, 0, -1):
        V.append(i)
        
    S = {i: i - 1 for i in V}
    S[0] = 0
    
    for p in range(2, r + 1):
        if S[p] > S[p - 1]:
            sp = S[p - 1]
            p2 = p * p
            for v in V:
                if v < p2: break
                S[v] -= S[v // p] - sp
                
    non_smooth = 0
    for q in range(1, r + 1):
        non_smooth += S[n // q] - S[q - 1]
        
    return n - non_smooth

def solve():
    ans = solve_case(10000000000)
    return str(ans)

if __name__ == '__main__':
    print(solve())
