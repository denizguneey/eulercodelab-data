def C(n):
    base = [1, 1, 2, 4, 9, 20, 46, 105, 243]
    if n < len(base):
        return base[n]
        
    MOD = 1000000000
    w = list(base)
    
    for _ in range(9, n + 1):
        next_val = 0
        next_val += 2 * w[8]
        next_val += 2 * w[7]
        next_val -= 1 * w[6]
        next_val -= 3 * w[5]
        next_val -= 5 * w[4]
        next_val += 4 * w[3]
        next_val -= 2 * w[2]
        next_val += 4 * w[1]
        
        next_val %= MOD
        if next_val < 0:
            next_val += MOD
            
        w = w[1:] + [next_val]
        
    return w[-1]

def solve():
    return str(C(100000))

if __name__ == "__main__":
    print(solve())
