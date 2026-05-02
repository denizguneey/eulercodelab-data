def solve():
    n = 10**17; k = 9**17

    def highest_pow2_leq(x):
        return 1 << (x.bit_length()-1)

    cur = k; s = cur
    while cur < n:
        step = highest_pow2_leq(n - cur)
        cur += step; s += cur
    return str(s)

if __name__ == '__main__':
    print(solve())
