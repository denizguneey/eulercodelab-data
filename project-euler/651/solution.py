import math

MOD = 1000000007

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def factorize(n):
    factors = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            factors.append((p, e))
        p += 1 if p == 2 else 2
    if x > 1:
        factors.append((x, 1))
    return factors

def gen_div_phi_rec(factors, idx, d, phi, out):
    if idx == len(factors):
        out.append((d, phi))
        return

    p, emax = factors[idx]
    gen_div_phi_rec(factors, idx + 1, d, phi, out)

    p_pow = 1
    for e in range(1, emax + 1):
        p_pow *= p
        phi_factor = p - 1
        for i in range(1, e):
            phi_factor *= p
        gen_div_phi_rec(factors, idx + 1, d * p_pow, phi * phi_factor, out)

def divisors_with_phi(n):
    out = []
    factors = factorize(n)
    gen_div_phi_rec(factors, 0, 1, 1, out)
    return out

class CycleType:
    def __init__(self, length, count):
        self.length = length
        self.count = count

class ClassType:
    def __init__(self, multiplicity, cycles):
        self.multiplicity = multiplicity
        self.cycles = cycles

def build_affine_classes(n):
    classes = []
    if n == 1:
        classes.append(ClassType(1, [CycleType(1, 1)]))
        return classes
    if n == 2:
        classes.append(ClassType(1, [CycleType(1, 2)]))
        classes.append(ClassType(1, [CycleType(2, 1)]))
        return classes

    div_phi = divisors_with_phi(n)
    for u, phi_u in div_phi:
        classes.append(ClassType(phi_u, [CycleType(u, n // u)]))

    if n % 2 == 1:
        classes.append(ClassType(n, [CycleType(1, 1), CycleType(2, (n - 1) // 2)]))
    else:
        classes.append(ClassType(n // 2, [CycleType(1, 2), CycleType(2, (n - 2) // 2)]))
        classes.append(ClassType(n // 2, [CycleType(2, n // 2)]))

    return classes

def surjections_mod(cycle_count, colors, comb):
    result = 0
    for j in range(colors + 1):
        ways_pick = comb[colors][j]
        ways_map = mod_pow(colors - j, cycle_count)
        term = (ways_pick * ways_map) % MOD
        if j % 2 == 1:
            result = (result + MOD - term) % MOD
        else:
            result = (result + term) % MOD
    return result

def cycle_count_product(x, y):
    total = 0
    for cx in x:
        for cy in y:
            g = math.gcd(cx.length, cy.length)
            total += cx.count * cy.count * g
    return total

def solve_case(colors, a, b, comb):
    classes_a = build_affine_classes(a)
    classes_b = build_affine_classes(b)

    group_a = sum(c.multiplicity for c in classes_a)
    group_b = sum(c.multiplicity for c in classes_b)

    group_mod = ((group_a % MOD) * (group_b % MOD)) % MOD
    inv_group = mod_pow(group_mod, MOD - 2)

    burnside_sum = 0
    cache = {}

    for ca in classes_a:
        for cb in classes_b:
            c = cycle_count_product(ca.cycles, cb.cycles)
            if c not in cache:
                onto = surjections_mod(c, colors, comb)
                cache[c] = onto
            else:
                onto = cache[c]

            mult = ((ca.multiplicity % MOD) * (cb.multiplicity % MOD)) % MOD
            burnside_sum = (burnside_sum + mult * onto) % MOD

    return (burnside_sum * inv_group) % MOD

def build_comb():
    c = [[0] * 41 for _ in range(41)]
    c[0][0] = 1
    for n in range(1, 41):
        c[n][0] = 1
        c[n][n] = 1
        for k in range(1, n):
            c[n][k] = (c[n - 1][k - 1] + c[n - 1][k]) % MOD
    return c

def solve():
    comb = build_comb()
    
    fib = [0] * 41
    fib[1] = 1
    for i in range(2, 41):
        fib[i] = fib[i - 1] + fib[i - 2]
        
    ans = 0
    for i in range(4, 41):
        ans = (ans + solve_case(i, fib[i - 1], fib[i], comb)) % MOD
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
