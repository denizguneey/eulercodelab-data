def collatz_length(start, memo):
    if start in memo:
        return memo[start]
    stack = []
    n = start
    while n not in memo:
        stack.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    length = memo[n]
    while stack:
        length += 1
        memo[stack.pop()] = length
    return memo[start]

def solve(limit=1000000):
    memo = {1: 1}
    best_n, best_len = 1, 1
    for n in range(2, limit):
        length = collatz_length(n, memo)
        if length > best_len:
            best_len = length
            best_n = n
    return best_n

if __name__ == "__main__":
    assert solve(20) == 18, "Checkpoint failed for limit=20"
    print(solve())
