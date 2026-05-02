# Problem 99: Largest exponential
# Determine which line number has the greatest numerical value (base^exp).

import os, math

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0099_base_exp.txt')
    with open(file_path) as f:
        lines = [line.strip() for line in f if line.strip()]
    
    best_line, best_val = 0, 0
    for i, line in enumerate(lines):
        base, exp = map(int, line.split(','))
        val = exp * math.log(base)
        if val > best_val:
            best_val = val
            best_line = i + 1
    print(best_line)

solve()
