# Problem 172: Investigating numbers with few repeated digits
# Count 18-digit numbers where no digit occurs more than 3 times.

import math

def solve():
    length = 18
    max_rep = 3
    fact = [math.factorial(i) for i in range(length+1)]
    total = 0

    def dfs(digit, remaining, denom):
        nonlocal total
        if digit == 10:
            if remaining != 0: return
            all_perm = fact[length] // denom
            lz = 0
            if counts[0] > 0:
                denom2 = (denom // fact[counts[0]]) * fact[counts[0]-1]
                lz = fact[length-1] // denom2
            total += all_perm - lz
            return
        mx = min(max_rep, remaining)
        for c in range(mx+1):
            counts[digit] = c
            dfs(digit+1, remaining-c, denom * fact[c])

    counts = [0]*10
    dfs(0, length, 1)
    print(total)

solve()
