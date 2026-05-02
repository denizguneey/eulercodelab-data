def fib_upto(n):
    f = [0, 1, 2]
    while f[-1] <= n:
        f.append(f[-1] + f[-2])
    return f

import bisect

def solve():
    n = 23416728348467685
    f = fib_upto(n)
    
    pref = [0] * len(f)
    if len(f) > 1: pref[1] = 0
    if len(f) > 2: pref[2] = 1
    
    for m in range(2, len(f) - 1):
        pref[m + 1] = pref[m] + f[m] + pref[m - 1]
        
    x = n
    out = 0
    
    while x > 0:
        m = bisect.bisect_right(f, x) - 1
        out += pref[m] + f[m]
        x -= f[m]
        
    return str(out)

if __name__ == '__main__':
    print(solve())
