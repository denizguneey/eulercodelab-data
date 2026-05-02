import math

def solve():
    LIMIT = 10**16

    def isqrt(x):
        r=int(math.isqrt(x))
        while (r+1)*(r+1)<=x: r+=1
        while r*r>x: r-=1
        return r

    inc = LIMIT - 1; mu = isqrt(inc)
    odd_cnt = mu//2+1
    # Sieve odd primes
    composite = bytearray(odd_cnt)
    odd_primes = []
    for idx in range(1, odd_cnt):
        if composite[idx]: continue
        p = 2*idx+1; odd_primes.append(p)
        if p<=mu//p:
            mark=(p*p-1)//2
            while mark<odd_cnt: composite[mark]=1; mark+=p

    # Mobius on odd numbers
    mob = [1]*odd_cnt
    for p in odd_primes:
        idx=(p-1)//2
        while idx<odd_cnt: mob[idx]=-mob[idx]; idx+=p
        if p<=mu//p:
            p2=p*p; idx=(p2-1)//2
            while idx<odd_cnt: mob[idx]=0; idx+=p2

    # Primes 3 mod 4
    p3m4 = [p for p in odd_primes if p%4==3]

    # Build coefficients c(u) = mu(u) + sum_{q|u, q==3(4)} mu(u/q)
    coeff = list(mob)
    for q in p3m4:
        n_idx=(q-1)//2; m_idx=0
        while n_idx<odd_cnt: coeff[n_idx]+=mob[m_idx]; m_idx+=1; n_idx+=q

    # Accumulate
    total = 0
    for idx in range(odd_cnt):
        c = coeff[idx]
        if c==0: continue
        u = 2*idx+1; u2=u*u
        terms = (inc//u2+3)//4
        total += c*terms
    return str(total)

if __name__=='__main__':
    print(solve())
