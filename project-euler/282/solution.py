import sys
from concurrent.futures import ThreadPoolExecutor

MOD_MAIN = 1475789056

sys.setrecursionlimit(2000)

def get_phi(n):
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result

def hyper_tower_2(height, m):
    if m == 1:
        return 0
    if height == 0:
        return 1 % m
    if height == 1:
        return 2 % m
    if height == 2:
        return 4 % m
    if height == 3:
        return 16 % m
    if height == 4:
        return 65536 % m

    phi = get_phi(m)
    exponent_val = hyper_tower_2(height - 1, phi)

    eff_exponent = exponent_val + phi
    return pow(2, eff_exponent, m)

def solve_n0(): return 1
def solve_n1(): return 3
def solve_n2(): return 7
def solve_n3(): return 61

def solve_n4():
    term = hyper_tower_2(7, MOD_MAIN)
    return (term - 3 + MOD_MAIN) % MOD_MAIN

def solve_large_n():
    term = hyper_tower_2(200, MOD_MAIN)
    return (term - 3 + MOD_MAIN) % MOD_MAIN

def solve():
    with ThreadPoolExecutor(max_workers=7) as executor:
        f0 = executor.submit(solve_n0)
        f1 = executor.submit(solve_n1)
        f2 = executor.submit(solve_n2)
        f3 = executor.submit(solve_n3)
        f4 = executor.submit(solve_n4)
        f5 = executor.submit(solve_large_n)
        f6 = executor.submit(solve_large_n)

        s0 = f0.result()
        s1 = f1.result()
        s2 = f2.result()
        s3 = f3.result()
        s4 = f4.result()
        s5 = f5.result()
        s6 = f6.result()

    total = (s0 + s1 + s2 + s3 + s4 + s5 + s6) % MOD_MAIN
    return str(total)

if __name__ == '__main__':
    print(solve())
