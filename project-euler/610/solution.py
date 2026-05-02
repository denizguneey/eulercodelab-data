def roman_value(c):
    return {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}.get(c, 0)

def roman_to_int(s):
    total = 0
    for i in range(len(s)):
        v = roman_value(s[i])
        if i + 1 < len(s) and roman_value(s[i + 1]) > v:
            total -= v
        else:
            total += v
    return total

def int_to_minimal_roman(value):
    if value <= 0: return ""
    table = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
        (40, "XL"),  (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"),  (1, "I")
    ]
    out = ""
    for v, tok in table:
        while value >= v:
            out += tok
            value -= v
    return out

def solve():
    p_stop = 0.02
    p_letter = 0.14
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    minr = [int_to_minimal_roman(v) for v in range(1000)]
    nxt = [[r for _ in range(7)] for r in range(1000)]
    
    for r in range(1, 1000):
        s = minr[r]
        for i, let in enumerate(letters):
            cand = s + let
            v = roman_to_int(cand)
            if 0 < v <= 999 and minr[v] == cand:
                nxt[r][i] = v
                
    E = [0.0] * 1000
    for r in range(999, 0, -1):
        rejected = 0
        sum_next = 0.0
        for i in range(7):
            v = nxt[r][i]
            if v == r:
                rejected += 1
            else:
                sum_next += E[v]
        denom = 1.0 - p_letter * rejected
        E[r] = (p_stop * r + p_letter * sum_next) / denom
        
    S_other = E[1] + E[5] + E[10] + E[50] + E[100] + E[500]
    E0 = (140.0 + 0.14 * S_other) / 0.86
    return f"{E0:.8f}"

if __name__ == '__main__':
    print(solve())
