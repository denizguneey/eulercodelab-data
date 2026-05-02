def solve():
    n = 20000000
    # Mobius sieve
    lp = [0] * (n + 1)
    primes = []
    mu = [0] * (n + 1)
    mu[1] = 1
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i; primes.append(i); mu[i] = -1
        for p in primes:
            v = i * p
            if v > n or p > lp[i]: break
            lp[v] = p
            if p == lp[i]: mu[v] = 0; break
            mu[v] = -mu[i]

    def count_pos_seg(wp, wn):
        prefix = [0] * (n + 1)
        cur = 0; mn = 0; mx = 0
        for i in range(1, n + 1):
            m = mu[i]
            if m == 1: cur += wp
            if m == -1: cur += wn
            prefix[i] = cur
            if cur < mn: mn = cur
            if cur > mx: mx = cur

        span = mx - mn + 1
        # Fenwick tree
        bit = [0] * (span + 2)
        def bit_add(idx, delta):
            while idx <= span + 1:
                bit[idx] += delta
                idx += idx & (-idx)
        def bit_sum(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s

        positives = 0
        for i in range(n + 1):
            idx = prefix[i] - mn + 1
            positives += bit_sum(idx - 1)
            bit_add(idx, 1)
        return positives

    total_pairs = n * (n + 1) // 2
    bad_a = count_pos_seg(99, -100)
    bad_b = count_pos_seg(-100, 99)
    return str(total_pairs - bad_a - bad_b)

if __name__ == '__main__':
    print(solve())
