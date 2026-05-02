import math

def solve():
    def primes_below(limit):
        is_p = bytearray(b'\x01' * limit)
        is_p[0] = 0
        is_p[1] = 0
        for p in range(2, limit):
            if p * p >= limit:
                break
            if is_p[p]:
                for q in range(p*p, limit, p):
                    is_p[q] = 0
        return [p for p in range(2, limit) if is_p[p]]

    primes = primes_below(190)
    n = len(primes)
    product_all = 1
    for p in primes:
        product_all *= p
    total_log = sum(math.log(p) for p in primes)
    target_log = total_log * 0.5

    split = n // 2
    left_primes = primes[:split]
    right_primes = primes[split:]

    def enumerate_subsets(ps):
        m = len(ps)
        logs = [math.log(p) for p in ps]
        subsets = []
        for mask in range(1 << m):
            log_val = 0.0
            for i in range(m):
                if mask & (1 << i):
                    log_val += logs[i]
            subsets.append((log_val, mask))
        subsets.sort()
        return subsets

    left = enumerate_subsets(left_primes)
    right = enumerate_subsets(right_primes)

    def build_value(lmask, rmask):
        v = 1
        for i in range(len(left_primes)):
            if lmask & (1 << i):
                v *= left_primes[i]
        for i in range(len(right_primes)):
            if rmask & (1 << i):
                v *= right_primes[i]
        return v

    # Two-pointer pass to find best log
    best_log = -1.0
    j = len(right) - 1
    for lv, lm in left:
        while j > 0 and lv + right[j][0] > target_log + 1e-12:
            j -= 1
        cand = lv + right[j][0]
        if cand <= target_log + 1e-12 and cand > best_log:
            best_log = cand

    # Second pass to find exact best value
    best_value = 0
    j = len(right) - 1
    for lv, lm in left:
        while j > 0 and lv + right[j][0] > target_log + 1e-10:
            j -= 1
        for t in range(-1, 13):
            k = j - t
            if k < 0 or k >= len(right):
                continue
            rv, rm = right[k]
            cand_log = lv + rv
            if t >= 0 and cand_log + 1e-9 < best_log:
                break
            if cand_log > target_log + 1e-8:
                continue
            cand = build_value(lm, rm)
            if cand * cand <= product_all and cand > best_value:
                best_value = cand

    MOD = 10**16
    return str(best_value % MOD)

if __name__ == '__main__':
    print(solve())
