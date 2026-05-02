import math
kMod = 1000000007

def primes_up_to(n):
    composite = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not composite[i]:
            primes.append(i)
            if i * i <= n:
                for j in range(i * i, n + 1, i):
                    composite[j] = True
    return primes

def vp_factorial(n, p):
    e = 0
    while n > 0:
        n //= p
        e += n
    return e

def r_of_factorial_optimized(n):
    if n < 2: return 0
    primes = primes_up_to(n)
    count_by_exp = {}
    max_e = 0
    for p in primes:
        e = vp_factorial(n, p)
        count_by_exp[e] = count_by_exp.get(e, 0) + 1
        max_e = max(max_e, e)
        
    groups = sorted(count_by_exp.items())
    
    d1 = 1
    for e, c in groups:
        d1 = (d1 * pow(e + 1, c, kMod)) % kMod
        
    events = []
    for e, c in groups:
        prev_term = e + 1
        l = 2
        while l <= e:
            q = e // l
            r = e // q
            term = q + 1
            if term != prev_term:
                ratio = (term * pow(prev_term, -1, kMod)) % kMod
                events.append((l, pow(ratio, c, kMod)))
                prev_term = term
            l = r + 1
        if e + 1 <= max_e and prev_term != 1:
            ratio = pow(prev_term, -1, kMod)
            events.append((e + 1, pow(ratio, c, kMod)))
            
    events.sort()
    
    curr_d = d1
    answer = curr_d - 1
    
    idx = 0
    for k in range(2, max_e + 1):
        while idx < len(events) and events[idx][0] == k:
            curr_d = (curr_d * events[idx][1]) % kMod
            idx += 1
        answer = (answer + curr_d - 1) % kMod
        
    return answer

def solve():
    return str(r_of_factorial_optimized(10000000))

if __name__ == "__main__":
    print(solve())
