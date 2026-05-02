# Problem 87: Prime power triples
# How many numbers below 50 million can be expressed as p^2 + q^3 + r^4?

def solve():
    limit = 50000000
    def sieve(n):
        s = [True] * (n + 1)
        s[0] = s[1] = False
        for p in range(2, int(n**0.5) + 1):
            if s[p]:
                for q in range(p*p, n + 1, p):
                    s[q] = False
        return [p for p in range(2, n + 1) if s[p]]
    
    primes = sieve(int(limit**0.5) + 1)
    sq = [p*p for p in primes if p*p < limit]
    cb = [p**3 for p in primes if p**3 < limit]
    ft = [p**4 for p in primes if p**4 < limit]
    
    values = set()
    for a in sq:
        for b in cb:
            if a + b >= limit: break
            for c in ft:
                s = a + b + c
                if s >= limit: break
                values.add(s)
    print(len(values))

solve()
