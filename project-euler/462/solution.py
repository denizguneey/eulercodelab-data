import math

def count_exact(n):
    rows = []
    p3 = 1
    while p3 <= n:
        bound = n // p3
        max_a = bound.bit_length() - 1
        rows.append(max_a + 1)
        if p3 > n // 3:
            break
        p3 *= 3
    
    if not rows:
        return 0
    max_width = rows[0]
    cell_count = sum(rows)
    
    col_heights = [0] * max_width
    for c in range(max_width):
        h = sum(1 for w in rows if w > c)
        col_heights[c] = h
        
    numerator = math.factorial(cell_count)
    denominator = 1
    for r in range(len(rows)):
        w = rows[r]
        for c in range(w):
            right = w - c - 1
            below = col_heights[c] - r - 1
            hook = right + below + 1
            denominator *= hook
            
    return numerator // denominator

def format_scientific_10(value):
    digits = str(value)
    exponent = len(digits) - 1
    if len(digits) < 12:
        digits += '0' * (12 - len(digits))
        
    leading = int(digits[:11])
    round_digit = int(digits[11])
    if round_digit >= 5:
        leading += 1
        
    if leading == 100000000000:
        leading = 10000000000
        exponent += 1
        
    integer_part = leading // 10000000000
    fractional_part = leading % 10000000000
    return f"{integer_part}.{fractional_part:010d}e{exponent}"

def solve():
    n = 1000000000000000000
    return format_scientific_10(count_exact(n))

if __name__ == '__main__':
    print(solve())
