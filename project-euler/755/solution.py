def S(n):
    fib = [1, 2]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
        
    prefix = [0] * len(fib)
    running = 0
    for i in range(len(fib)):
        running += fib[i]
        prefix[i] = running
        
    memo = [{} for _ in range(len(fib))]
    
    def dfs(i, limit):
        if i < 0:
            return 1
        if limit >= prefix[i]:
            return 1 << (i + 1)
            
        if limit in memo[i]:
            return memo[i][limit]
            
        total = dfs(i - 1, limit)
        if limit >= fib[i]:
            total += dfs(i - 1, limit - fib[i])
            
        memo[i][limit] = total
        return total
        
    return dfs(len(fib) - 1, n)

def solve():
    return str(S(10000000000000))

if __name__ == "__main__":
    print(solve())
