def solve():
    MOD = 1_000_000_000
    N = 450_283_905_890_997_363  # 3^37

    def reverse_bits_of_odd_core(n):
        while n % 2 == 0: n >>= 1
        rev = 0
        while n > 0:
            rev = (rev << 1) | (n & 1)
            n >>= 1
        return rev

    def f_mod(n):
        return reverse_bits_of_odd_core(n) % MOD

    sum_cache = {0: 0, 1: 1}
    odd_cache = {0: 0, 1: 1}

    def sum_mod(n):
        if n in sum_cache: return sum_cache[n]
        if n % 2 == 0:
            half = n >> 1
            val = (sum_mod(half) + odd_sum_mod(half)) % MOD
        else:
            val = (sum_mod(n-1) + f_mod(n)) % MOD
        sum_cache[n] = val
        return val

    def odd_sum_mod(n):
        if n in odd_cache: return odd_cache[n]
        if n % 2 == 0:
            half = n >> 1
            val = (-1 + 5 * odd_sum_mod(half) - 3 * sum_mod(half - 1)) % MOD
        else:
            half = n >> 1
            val = (odd_sum_mod(n-1) + 2 * f_mod(n) - f_mod(half)) % MOD
        odd_cache[n] = val
        return val

    import sys
    sys.setrecursionlimit(200)
    ans = sum_mod(N)
    return f"{ans:09d}"

if __name__ == '__main__':
    print(solve())
