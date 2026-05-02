# Problem 151: Paper sheets of standard sizes (expected single-sheet picks)

def solve():
    memo = {}
    def dfs(state):
        key = state
        if key in memo: return memo[key]
        total = sum(state)
        if total == 0:
            memo[key] = 0.0
            return 0.0
        ans = 0.0
        # Count single-sheet states (but not the final A5 if it's the only one)
        if total == 1 and state[3] == 0:
            ans += 1.0
        for i in range(4):
            if state[i] == 0: continue
            prob = state[i] / total
            nxt = list(state)
            nxt[i] -= 1
            for j in range(i+1, 4):
                nxt[j] += 1
            ans += prob * dfs(tuple(nxt))
        memo[key] = ans
        return ans
    result = dfs((1, 1, 1, 1))
    print(f"{result:.6f}")

solve()
