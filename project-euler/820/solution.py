def solve():
    N = 10_000_000

    def pow_mod10(exp, mod):
        base = 10 % mod
        res = 1 % mod
        while exp > 0:
            if exp & 1: res = res * base % mod
            base = base * base % mod
            exp >>= 1
        return res

    def nth_digit(n, k):
        r = pow_mod10(n - 1, k)
        return (10 * r) // k

    ans = sum(nth_digit(N, k) for k in range(1, N + 1))
    return str(ans)

if __name__ == '__main__':
    print(solve())
