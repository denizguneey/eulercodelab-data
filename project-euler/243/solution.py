def solve(target_num=15499, target_den=94744):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    best = [float('inf')]
    
    def dfs(prime_index, max_exp, n, phi_n):
        if n >= best[0]:
            return
            
        if n > 1 and phi_n * target_den < target_num * (n - 1):
            best[0] = n
            return
            
        if prime_index >= len(primes):
            return
            
        p = primes[prime_index]
        n_mul = n
        phi_mul = phi_n
        
        for exp in range(1, max_exp + 1):
            if n_mul > best[0] // p:
                break
                
            n_mul *= p
            if exp == 1:
                phi_mul *= (p - 1)
            else:
                phi_mul *= p
                
            dfs(prime_index + 1, exp, n_mul, phi_mul)

    dfs(0, 64, 1, 1)
    return str(best[0])

if __name__ == '__main__':
    print(solve())
