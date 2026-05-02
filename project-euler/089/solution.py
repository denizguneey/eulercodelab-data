# Problem 89: Roman numerals
# Find the number of characters saved by writing the Roman numerals in minimal form.

import os

def roman_to_int(s):
    vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and vals[s[i]] < vals[s[i+1]]:
            total -= vals[s[i]]
        else:
            total += vals[s[i]]
    return total

def int_to_roman(n):
    pairs = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
             (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
    result = ''
    for val, sym in pairs:
        while n >= val:
            result += sym
            n -= val
    return result

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0089_roman.txt')
    with open(file_path) as f:
        lines = [line.strip() for line in f if line.strip()]
    saved = 0
    for line in lines:
        val = roman_to_int(line)
        minimal = int_to_roman(val)
        saved += len(line) - len(minimal)
    print(saved)

solve()
