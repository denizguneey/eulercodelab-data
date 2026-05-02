import math

def simple_primes_up_to(limit):
    is_prime = [True] * (limit + 1)
    if limit >= 0: is_prime[0] = False
    if limit >= 1: is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for x in range(p * p, limit + 1, p):
                is_prime[x] = False
        p += 1
    return [i for i in range(2, limit + 1) if is_prime[i]]

def primes_in_segment(lo, hi):
    root = int(math.sqrt(hi)) + 1
    base_primes = simple_primes_up_to(root)
    is_prime = [True] * (hi - lo + 1)
    for p in base_primes:
        start = (lo + p - 1) // p * p
        if start < p * p:
            start = p * p
        for x in range(start, hi + 1, p):
            is_prime[x - lo] = False
            
    if lo == 0:
        if len(is_prime) > 0: is_prime[0] = False
        if len(is_prime) > 1: is_prime[1] = False
    elif lo == 1:
        is_prime[0] = False
        
    out = []
    for x in range(lo, hi + 1):
        if is_prime[x - lo]:
            out.append(x)
    return out

def lucas_V_mod(k, p, P=11):
    if k == 0: return 2 % p
    vm = 2 % p
    vmp1 = P % p
    msb = k.bit_length() - 1
    for bit in range(msb, -1, -1):
        v2m = (vm * vm - 2) % p
        v2m1 = (vm * vmp1 - P) % p
        v2m2 = (vmp1 * vmp1 - 2) % p
        if ((k >> bit) & 1) == 0:
            vm, vmp1 = v2m, v2m1
        else:
            vm, vmp1 = v2m1, v2m2
    return vm

def a_n_mod_p(n, p):
    if n == 1: return 1 % p
    leg = pow(117 % p, (p - 1) // 2, p)
    order_mod = (p - 1) if leg == 1 else (p + 1)
    idx = pow(2, n - 1, order_mod)
    b = lucas_V_mod(idx, p, 11)
    inv6 = pow(6, p - 2, p)
    a = ((b - 5) % p * inv6) % p
    return a

def B(x, y, n):
    lo = x
    hi = x + y
    primes = primes_in_segment(lo, hi)
    total = 0
    for p in primes:
        total += a_n_mod_p(n, p)
    return total

def solve():
    x = 1000000000
    y = 10000000
    n = 1000000000000000
    return str(B(x, y, n))

if __name__ == '__main__':
    print(solve())
