def solve(N):
    spf = [0] * (N + 1)
    primes = []
    
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
        for p in primes:
            v = p * i
            if v > N:
                break
            spf[v] = p
            if p == spf[i]:
                break
                
    exp = [0] * (N + 1)
    c = [0] * (N + 1)
    c[1] = 1
    
    for n in range(2, N + 1):
        p = spf[n]
        m = n // p
        
        if m % p == 0:
            e = exp[m] + 1
            exp[n] = e
            if e % 2 == 0:
                c[n] = c[m] * p * p
            else:
                c[n] = c[m] * p
        else:
            exp[n] = 1
            c[n] = c[m] * (p - 1)
            
    odd_count = (N + 1) // 2
    total = -odd_count * odd_count
    
    for d in range(2, N + 1, 2):
        m = N // d
        tri = m * (m + 1) // 2
        total += c[d] * tri
        
    return total

def get_ans():
    return str(solve(12345678))

if __name__ == "__main__":
    print(get_ans())
