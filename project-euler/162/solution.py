# Problem 162: Hexadecimal numbers containing 0, 1, and A

def solve():
    max_digits = 16
    total = 0
    for n in range(1, max_digits + 1):
        # Inclusion-exclusion: count n-digit hex numbers (no leading zero) containing 0, 1, A
        t = 15 * 16**(n-1)  # total n-digit hex
        m0 = 15**n           # missing 0
        m1 = 14 * 15**(n-1)  # missing 1
        mA = 14 * 15**(n-1)  # missing A
        m01 = 14**n
        m0A = 14**n
        m1A = 13 * 14**(n-1)
        m01A = 13**n
        total += t - (m0 + m1 + mA) + (m01 + m0A + m1A) - m01A
    # Output in hex
    result = ""
    v = total
    if v == 0:
        result = "0"
    else:
        while v > 0:
            d = v & 0xF
            result = "0123456789ABCDEF"[d] + result
            v >>= 4
    print(result)

solve()
