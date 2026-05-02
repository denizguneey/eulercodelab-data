# Problem 207: Integer partition equations
# 4^t = 2^t + k => m(m-1) = k where m = 2^t
# "perfect" if t is integer (m is power of 2)
# Find least k such that P(k)/count < 1/12345

def solve():
    denominator = 12345
    p = 1  # number of perfect partitions
    next_pow2 = 4
    for m in range(2, 10**8):
        if m == next_pow2:
            p += 1
            next_pow2 <<= 1
        # p * denominator < (m - 1)
        if p * denominator < (m - 1):
            print(m * (m - 1))
            return

solve()
