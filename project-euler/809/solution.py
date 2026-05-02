import sys

sys.setrecursionlimit(2000)

def inv_mod(a, mod):
    t, nt = 0, 1
    r, nr = mod, a % mod
    while nr != 0:
        q = r // nr
        t, nt = nt, t - q * nt
        r, nr = nr, r - q * nr
    if t < 0:
        t += mod
    return t

def pow_mod_signed_2(exp, mod):
    if mod == 1:
        return 0
    if exp >= 0:
        return pow(2, exp, mod)
    inv2 = inv_mod(2, mod)
    return pow(inv2, -exp, mod)

def phi(n):
    if n == 0:
        return 0
    result = n
    if n % 2 == 0:
        result -= result // 2
        while n % 2 == 0:
            n //= 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        result -= result // n
    return result

memo = {1: 0}

def tower2_fixpoint_mod(mod):
    if mod in memo:
        return memo[mod]
        
    odd = mod
    twos = 0
    while odd % 2 == 0:
        odd //= 2
        twos += 1
        
    t = phi(odd)
    w = 0 if t == 1 else tower2_fixpoint_mod(t) - twos
    
    odd_part = pow_mod_signed_2(w, odd)
    ans = (odd_part << twos) % mod
    memo[mod] = ans
    return ans

def solve():
    MOD = 1000000000000000
    top = tower2_fixpoint_mod(MOD)
    return str((top + MOD - 3) % MOD)

if __name__ == "__main__":
    print(solve())
