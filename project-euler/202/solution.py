# Problem 202: Laserbeam
# Count how many times a laser exits through vertex C after exactly 12017639147 reflections
# in an equilateral triangle.

from math import gcd

def solve():
    reflections = 12017639147
    n = (reflections + 3) // 2
    # Factor n
    factors = []
    tmp = n
    p = 2
    while p * p <= tmp:
        if tmp % p == 0:
            factors.append(p)
            while tmp % p == 0:
                tmp //= p
        p += 1
    if tmp > 1:
        factors.append(tmp)

    # Count t in [1, n) with t%3==2 and gcd(t, n)==1 using inclusion-exclusion
    def count_coprime_mod3(n_val, factors_list):
        ans = 0
        for mask in range(1 << len(factors_list)):
            d = 1
            bits = 0
            for i in range(len(factors_list)):
                if mask & (1 << i):
                    d *= factors_list[i]
                    bits += 1
            if d % 3 == 0:
                continue
            m = (n_val - 1) // d
            # Count t in [1, m] with (t*d) % 3 == 2
            # t*d % 3 == 2 => t % 3 == (2 * modinv(d,3)) % 3
            inv3 = 1 if d % 3 == 1 else 2
            residue = (2 * inv3) % 3
            if residue == 0:
                first = 3
            else:
                first = residue
            if first > m:
                cnt = 0
            else:
                cnt = 1 + (m - first) // 3
            if bits % 2 == 0:
                ans += cnt
            else:
                ans -= cnt
        return ans

    print(count_coprime_mod3(n, factors))

solve()
