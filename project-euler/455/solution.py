def solve():
    LIMIT = 1_000_000
    MOD = 1_000_000_000

    def mod_pow(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1: result = result * base % mod
            base = base * base % mod
            exp >>= 1
        return result

    def f_value(n, mod):
        x = 0
        seen = []
        for _ in range(80):
            nx = mod_pow(n, x, mod)
            if nx == x:
                return x if x > 0 else 0
            if nx in seen:
                return 0
            seen.append(nx)
            x = nx
        nx = mod_pow(n, x, mod)
        if nx == x and x > 0:
            return x
        return 0

    total = sum(f_value(n, MOD) for n in range(2, LIMIT + 1))
    return str(total)

if __name__ == '__main__':
    print(solve())
