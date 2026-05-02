import sys

# Increase recursion depth just in case, though it only goes to O(log N) depth.
sys.setrecursionlimit(2000)

memo = {}

def odd_numbers_sum(x):
    m = (x + 1) // 2
    return m * m

def odd_part_prefix_sum(n):
    total = 0
    x = n
    while x > 0:
        total += odd_numbers_sum(x)
        x //= 2
    return total

def get_sum(n):
    if n == 0:
        return 0
    if n in memo:
        return memo[n]
    
    result = odd_part_prefix_sum(n)
    l = 2
    while l <= n:
        q = n // l
        r = n // q
        result -= (r - l + 1) * get_sum(q)
        l = r + 1
        
    memo[n] = result
    return result

def solve():
    n = 500000000
    ans = get_sum(n)
    return str(ans)

if __name__ == '__main__':
    print(solve())
