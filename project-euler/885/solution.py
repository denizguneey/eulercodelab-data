def S_mod(n, mod):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i

    pow10_mod = [1] * (n + 1)
    pow10_mod[0] = 1 % mod
    rep_mod = [0] * (n + 1)

    for i in range(1, n + 1):
        pow10_mod[i] = (pow10_mod[i - 1] * 10) % mod

    for i in range(1, n + 1):
        rep_mod[i] = (rep_mod[i - 1] * 10 + 1) % mod

    ans = [0]  # Use list to mutate inside recursive function

    def dfs(digit, rem, s, denom, val_mod):
        if digit == 10:
            ways = fact[n] // (fact[n - s] * denom)
            ans[0] = (ans[0] + (ways % mod) * val_mod) % mod
            return

        for c in range(rem + 1):
            next_denom = denom * fact[c]
            next_mod = (val_mod * pow10_mod[c] + digit * rep_mod[c]) % mod
            dfs(digit + 1, rem - c, s + c, next_denom, next_mod)

    dfs(1, n, 0, 1, 0)
    return ans[0]

def solve():
    MOD = 1123455689
    return str(S_mod(18, MOD))

if __name__ == "__main__":
    print(solve())
