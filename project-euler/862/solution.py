def S_value(k):
    fact = [1] * 13
    for i in range(1, k + 1):
        fact[i] = fact[i - 1] * i

    cnt = [0] * 10
    ans = [0]  # Using list to mutate inside nested function

    def dfs(d, rem):
        if d == 9:
            cnt[9] = rem
            perms = fact[k]
            for i in range(10):
                perms //= fact[cnt[i]]
            valid = perms * (k - cnt[0]) // k
            ans[0] += valid * (valid - 1) // 2
            return

        for v in range(rem + 1):
            cnt[d] = v
            dfs(d + 1, rem - v)

    dfs(0, k)
    return ans[0]

def solve():
    return str(S_value(12))

if __name__ == "__main__":
    print(solve())
