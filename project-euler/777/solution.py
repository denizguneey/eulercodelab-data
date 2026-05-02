def solve():
    n = 1000000

    def sum_upto(n): return n * (n+1) // 2

    # Mobius sieve
    mu = [0]*(n+1); mu[1] = 1; comp = bytearray(n+1); primes = []
    for i in range(2, n+1):
        if not comp[i]: primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > n: break
            comp[i*p] = 1
            if i % p == 0: mu[i*p] = 0; break
            mu[i*p] = -mu[i]

    # Compute sum_ab and sum_a
    sum_ab = 0; sum_a_val = 0
    for d in range(1, n+1):
        md = mu[d]
        if md == 0: continue
        k = n // d; s = sum_upto(k)
        sum_ab += md * d * d * s * s
        sum_a_val += md * d * s * k
    s_all = sum_upto(n)
    sum_ab_2n = sum_ab - 2*s_all + 1
    sum_a_2n = sum_a_val - n - s_all + 1

    # Subset counting
    cnt10 = [0]*(n+1); sum10 = [0]*(n+1)
    cnt5o = [0]*(n+1); sum5o = [0]*(n+1)
    cnt2n = [0]*(n+1); sum2n = [0]*(n+1)
    cntg1 = [0]*(n+1); sumg1 = [0]*(n+1)

    for d in range(1, n+1):
        md = mu[d]
        if md == 0: continue
        # S10
        g = 1
        if d%10==0: g=10
        elif d%5==0: g=5
        elif d%2==0: g=2
        L = d//g * 10; t = n//L
        if t > 0:
            c10 = t; s10_v = L*t*(t+1)//2
            for a in range(d, n+1, d): cnt10[a] += md*c10; sum10[a] += md*s10_v
        # S5Odd
        if d%2 != 0:
            g5 = 5 if d%5==0 else 1
            L5 = d//g5 * 5; t5 = n//L5; k5 = (t5+1)//2
            if k5 > 0:
                c5o = k5; s5o_v = L5*k5*k5
                for a in range(d, n+1, d): cnt5o[a] += md*c5o; sum5o[a] += md*s5o_v
        # S2Not5
        if d%5 != 0:
            L2 = d if d%2==0 else 2*d; t2 = n//L2; t25 = n//(5*L2)
            c2n = t2-t25
            if c2n > 0:
                s2n_v = L2*t2*(t2+1)//2 - 5*L2*t25*(t25+1)//2
                for a in range(d, n+1, d): cnt2n[a] += md*c2n; sum2n[a] += md*s2n_v
        # SCoprime10
        if d%2 != 0 and d%5 != 0:
            x = n//d; t2c = x//2; t5c = x//5; t10c = x//10
            cg = x - t2c - t5c + t10c
            if cg > 0:
                sg = (sum_upto(x) - 2*sum_upto(t2c) - 5*sum_upto(t5c) + 10*sum_upto(t10c))
                sg_v = d * sg
                for a in range(d, n+1, d): cntg1[a] += md*cg; sumg1[a] += md*sg_v

    count10_total = 0; sum_a10 = 0; sum_ab10 = 0
    for a in range(2, n+1):
        g = 1
        if a%10==0: g=10
        elif a%5==0: g=5
        elif a%2==0: g=2
        if g==1: cnt=cnt10[a]; s=sum10[a]
        elif g==2: cnt=cnt5o[a]; s=sum5o[a]
        elif g==5: cnt=cnt2n[a]; s=sum2n[a]
        else: cnt=cntg1[a]-1; s=sumg1[a]-1
        count10_total += cnt; sum_a10 += a*cnt; sum_ab10 += a*s

    base = 2*sum_ab_2n - 3*sum_a_2n
    corr = 6*sum_a10 + 4*count10_total - 6*sum_ab10
    total_num = 4*base + corr
    value = total_num / 4.0

    # Format in scientific notation
    import math
    if value == 0: return "0.000000000e0"
    exp = int(math.floor(math.log10(abs(value))))
    mantissa = value / 10**exp
    return f"{mantissa:.9f}e{exp}"

if __name__ == '__main__':
    print(solve())
