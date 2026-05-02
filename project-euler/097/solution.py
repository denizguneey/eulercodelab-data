# Problem 97: Large non-Mersenne prime
# Find the last ten digits of 28433 * 2^7830457 + 1.

def solve():
    mod = 10**10
    print((28433 * pow(2, 7830457, mod) + 1) % mod)

solve()
