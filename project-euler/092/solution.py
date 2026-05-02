# Problem 92: Square digit chains
# How many starting numbers below 10 million arrive at 89?

def solve():
    memo = {1: 1, 89: 89}
    
    def chain_end(n):
        if n in memo:
            return memo[n]
        result = chain_end(sum(int(d)**2 for d in str(n)))
        memo[n] = result
        return result
    
    count = sum(1 for n in range(1, 10000000) if chain_end(n) == 89)
    print(count)

solve()
