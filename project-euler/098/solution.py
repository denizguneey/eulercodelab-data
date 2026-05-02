# Problem 98: Anagramic squares
# Find the largest square number formed by anagram word pairs.

import os
from collections import defaultdict
from itertools import permutations
import math

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0098_words.txt')
    with open(file_path) as f:
        content = f.read().strip()
    words = [w.strip('"') for w in content.split(',')]
    
    # Group anagrams
    groups = defaultdict(list)
    for w in words:
        key = ''.join(sorted(w))
        groups[key].append(w)
    
    anagram_pairs = []
    for key, ws in groups.items():
        if len(ws) >= 2:
            for i in range(len(ws)):
                for j in range(i+1, len(ws)):
                    anagram_pairs.append((ws[i], ws[j]))
    
    # Generate squares by digit count
    max_len = max(len(w) for pair in anagram_pairs for w in pair)
    squares_by_len = defaultdict(list)
    n = 1
    while len(str(n*n)) <= max_len:
        s = str(n*n)
        squares_by_len[len(s)].append(s)
        n += 1
    
    best = 0
    for w1, w2 in anagram_pairs:
        length = len(w1)
        for sq in squares_by_len[length]:
            # Try mapping w1 -> sq
            mapping = {}
            reverse = {}
            valid = True
            for c, d in zip(w1, sq):
                if c in mapping:
                    if mapping[c] != d:
                        valid = False; break
                else:
                    if d in reverse:
                        if reverse[d] != c:
                            valid = False; break
                    mapping[c] = d
                    reverse[d] = c
            if not valid:
                continue
            # Apply mapping to w2
            mapped = ''.join(mapping[c] for c in w2)
            if mapped[0] == '0':
                continue
            val = int(mapped)
            r = int(math.isqrt(val))
            if r * r == val:
                best = max(best, int(sq), val)
    
    print(best)

solve()
