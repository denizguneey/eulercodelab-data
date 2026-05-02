# Problem 148: Exploring Pascal's Triangle
# Count entries in first 10^9 rows of Pascal's triangle not divisible by 7.
# Use Lucas' theorem: base-7 digits.

def solve():
    rows = 10**9
    # Convert rows to base 7
    digits = []
    x = rows
    while x > 0:
        digits.append(x % 7)
        x //= 7
    digits.reverse()
    
    # For each digit d at position i, contribution from "full" blocks below
    # is d * 28^remaining * prefix_product, where prefix_product = prod(d_j+1) for j<i
    pow28 = [1] * (len(digits) + 1)
    for i in range(1, len(pow28)):
        pow28[i] = pow28[i-1] * 28
    
    answer = 0
    prefix_product = 1
    for i, d in enumerate(digits):
        rem = len(digits) - i - 1
        for xd in range(d):
            answer += prefix_product * (xd + 1) * pow28[rem]
        prefix_product *= (d + 1)
    
    print(answer)

solve()
