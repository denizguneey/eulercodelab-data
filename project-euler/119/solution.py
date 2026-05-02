# Problem 119: Digit power sum
# Find the 30th term where n = (digit_sum(n))^k for some k.

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve():
    limit = 10**18
    values = set()
    max_ds = 9 * 18  # max digit sum for 18-digit numbers
    for s in range(2, max_ds + 1):
        val = s * s
        while val <= limit:
            if val >= 10 and digit_sum(val) == s:
                values.add(val)
            val *= s
    
    result = sorted(values)
    print(result[29])  # 30th term (0-indexed)

solve()
