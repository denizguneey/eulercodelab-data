# Problem 105: Special subset sums: testing
# Sum all set values that satisfy the special subset sum conditions.

import os
from itertools import combinations

def is_special_sum_set(s):
    s = sorted(s)
    n = len(s)
    for k in range(1, n):
        if k + 1 <= n:
            if sum(s[:k+1]) <= sum(s[n-k:]):
                return False
    sums = {}
    for size in range(1, n+1):
        for combo in combinations(range(n), size):
            total = sum(s[i] for i in combo)
            mask = sum(1 << i for i in combo)
            for prev_mask, prev_sum in list(sums.items()):
                if prev_mask & mask == 0 and prev_sum == total:
                    return False
            sums[mask] = total
    return True

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0105_sets.txt')
    total = 0
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            values = list(map(int, line.split(',')))
            if is_special_sum_set(values):
                total += sum(values)
    print(total)

solve()
