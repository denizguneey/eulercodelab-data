import math

def sieve_prime_flags(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
    return is_prime

def solve():
    squares = 500
    sequence = "PPPPNNPPPNPPNPN"
    
    is_prime = sieve_prime_flags(squares)
    state = [1] * (squares + 1)
    state[0] = 0
    
    denom = squares
    
    for step in range(len(sequence)):
        croak = sequence[step]
        for pos in range(1, squares + 1):
            prime_square = is_prime[pos]
            good = prime_square if croak == 'P' else not prime_square
            if good:
                state[pos] *= 2
                
        denom *= 3
        
        if step + 1 < len(sequence):
            nxt = [0] * (squares + 1)
            for pos in range(1, squares + 1):
                w = state[pos]
                if pos == 1:
                    nxt[2] += w * 2
                elif pos == squares:
                    nxt[squares - 1] += w * 2
                else:
                    nxt[pos - 1] += w
                    nxt[pos + 1] += w
            denom *= 2
            state = nxt
            
    numer = sum(state[1:])
    g = math.gcd(numer, denom)
    
    return f"{numer // g}/{denom // g}"
    
if __name__ == '__main__':
    print(solve())
