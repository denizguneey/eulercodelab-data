# Problem 104: Pandigital Fibonacci ends
# Find the first Fibonacci number where both the first and last 9 digits are 1-9 pandigital.

import math

def is_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')

def solve():
    MOD = 10**9
    a, b = 1, 1
    log_phi = math.log10((1 + math.sqrt(5)) / 2)
    log_sqrt5 = math.log10(5) / 2
    
    for n in range(3, 1000000):
        a, b = b, (a + b) % MOD
        if not is_pandigital(str(b).zfill(9)):
            continue
        # Check leading digits using logarithms
        log_fn = n * log_phi - log_sqrt5
        frac = log_fn - int(log_fn)
        leading = str(int(10**(frac + 8)))[:9]
        if is_pandigital(leading):
            print(n)
            return

solve()
