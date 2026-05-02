def compute_totients(limit):
    phi = list(range(limit + 1))
    for p in range(2, limit + 1):
        if phi[p] == p:
            for k in range(p, limit + 1, p):
                phi[k] -= phi[k] // p
    return phi

def solve(from_n=1864, to_n=1909):
    phi = compute_totients(to_n)
    denominator_used = bytearray(to_n + 1)
    
    for n in range(from_n, to_n + 1):
        d = 1
        while d * d <= n:
            if n % d == 0:
                denominator_used[d] = 1
                denominator_used[n // d] = 1
            d += 1
            
    sides = 0
    for d in range(1, to_n + 1):
        if denominator_used[d]:
            sides += phi[d]
            
    return str(sides)

if __name__ == '__main__':
    print(solve())
