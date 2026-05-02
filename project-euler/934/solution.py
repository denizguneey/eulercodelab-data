def sieve_primes(limit):
    composite = [False] * (limit + 1)
    primes = []
    for i in range(2, limit + 1):
        if not composite[i]:
            primes.append(i)
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    composite[j] = True
    return primes

def solve(N):
    primes = sieve_primes(10000)
    
    residues = [0]
    modulus = 1
    
    pass_count = N
    answer = 0
    
    for p in primes:
        next_modulus = modulus * p
        inv = pow(modulus % p, -1, p)
        
        next_residues = []
        for r in residues:
            rp = r % p
            for a in range(0, p, 7):
                t = (((a + p - rp) % p) * inv) % p
                
                if modulus > N and t != 0:
                    continue
                    
                x = r + modulus * t
                if x <= N:
                    next_residues.append(x)
                    
        next_count = 0
        if next_modulus <= N:
            for r in next_residues:
                if r == 0:
                    next_count += N // next_modulus
                else:
                    next_count += (N - r) // next_modulus + 1
        else:
            for r in next_residues:
                if r != 0:
                    next_count += 1
                    
        fail_here = pass_count - next_count
        answer += fail_here * p
        
        if next_count == 0:
            return answer
            
        residues = next_residues
        modulus = next_modulus
        pass_count = next_count
        
    return 0

def get_answer():
    N = 100000000000000000
    return str(solve(N))

if __name__ == "__main__":
    print(get_answer())
