def solve():
    MOD = 1111211113; N = 10000

    def mp(a, e):
        r = 1; a %= MOD
        while e > 0:
            if e&1: r=r*a%MOD
            a=a*a%MOD; e >>= 1
        return r

    # Sieve primes up to 2*N
    limit = 2*N; is_prime = [True]*(limit+1); is_prime[0]=is_prime[1]=False
    for p in range(2, int(limit**0.5)+1):
        if is_prime[p]:
            for q in range(p*p, limit+1, p): is_prime[q] = False
    primes = [x for x in range(2, limit+1) if is_prime[x]]

    def u_pp(p, e):
        if p == 2: return 1 << e
        u = (p+1)//2
        for k in range(2, e+1):
            d = (p-1) if k%2==0 else (p-1)//2
            u = p*u - d
        return u

    def u_from_fact(s):
        x = s; u = 1
        for p in primes:
            if p*p > x: break
            if x%p != 0: continue
            e = 0
            while x%p == 0: x //= p; e += 1
            u *= u_pp(p, e)
        if x > 1: u *= u_pp(x, 1)
        return u

    # Mobius sieve
    spf = [0]*(N+1); mu = [0]*(N+1); ps = []; mu[1] = 1
    for i in range(2, N+1):
        if spf[i]==0: spf[i]=i; ps.append(i); mu[i]=-1
        for p in ps:
            if p*i>N: break
            spf[p*i]=p
            if i%p==0: mu[p*i]=0; break
            mu[p*i]=-mu[i]

    # Enumerate states
    states = []
    for x_power in range(64):
        x = 1 << x_power
        if x > 2*N: break
        states.append((x, x, 1))

    head = 0
    while head < len(states):
        integer, count, pi = states[head]; head += 1
        if count > N: continue
        max_f = N // count
        if max_f < 2: continue
        max_p = 2*max_f - 1
        for idx in range(pi, len(primes)):
            p = primes[idx]
            if p > max_p: break
            ni = integer * p; pp = p; nvf = (p+1)//2
            while nvf <= max_f:
                nv = count * nvf
                states.append((ni, nv, idx+1))
                next_pp = pp * p
                if next_pp > 10**18: break
                pp = next_pp
                nvf = int(p*pp / (2*p + 2) + 1)
                ni_next = ni * p
                if ni_next > 10**18: break
                ni = ni_next

    # Compute inv
    inv = [0]*(N+2); inv[1] = 1
    for i in range(2, N+2): inv[i] = (MOD - MOD//i*inv[MOD%i]%MOD) % MOD

    rep = [0]*(N+1)
    for integer, count, pi in states:
        if count > N: continue
        free = integer - count
        max_k = min(free, N-count)
        comb = 1; p = count
        for k in range(int(max_k)+1):
            rep[p] = (rep[p]+comb) % MOD
            if k == max_k: break
            comb = comb*(free-k) % MOD * inv[k+1] % MOD
            p += 1

    for i in range(2, N+1): rep[i] = (rep[i]+rep[i-1]) % MOD

    result = 0
    for i in range(1, N+1):
        result += mu[i]*rep[N//i]
        result %= MOD
    if result < 0: result += MOD
    return str(result)

if __name__ == '__main__':
    print(solve())
