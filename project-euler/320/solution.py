def solve():
    K = 1234567890
    OUTPUT_MOD = 10**18
    upper = 1000000

    def valuation_factorial(n, p):
        s = 0
        while n > 0:
            n //= p
            s += n
        return s

    def minimal_n_for_target(p, target, previous):
        if target == 0:
            return 0
        factor = p - 1
        lower = max(previous, target * factor)
        hi = lower
        while True:
            have = valuation_factorial(hi, p)
            if have >= target:
                break
            hi += (target - have) * factor
        lo = lower
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if valuation_factorial(mid, p) >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    # Build SPF
    spf = list(range(upper + 1))
    for i in range(2, upper + 1):
        if i * i > upper:
            break
        if spf[i] == i:
            for j in range(i*i, upper + 1, i):
                if spf[j] == j:
                    spf[j] = i

    required = [0] * (upper + 1)
    needed_n = [0] * (upper + 1)
    current_max = 0
    total = 0

    for i in range(2, upper + 1):
        x = i
        while x > 1:
            p = spf[x]
            exp = 0
            while x % p == 0:
                x //= p
                exp += 1
            required[p] += K * exp
            updated = minimal_n_for_target(p, required[p], needed_n[p])
            needed_n[p] = updated
            if updated > current_max:
                current_max = updated
        if i >= 10:
            total += current_max

    return str(total % OUTPUT_MOD)

if __name__ == '__main__':
    print(solve())
