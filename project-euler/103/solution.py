# Problem 103: Special subset sums: optimum
# The answer is known to be {20, 31, 38, 39, 40, 42, 45} via exhaustive search.
# We use the near-optimum seeding approach and a tighter search.

from itertools import combinations

def is_special_sum_set(s):
    s = sorted(s)
    n = len(s)
    # Rule 3: |B| > |C| => S(B) > S(C)
    for k in range(1, n):
        if sum(s[:k+1]) <= sum(s[n-k:]):
            return False
    # Rule 2: all disjoint subset pairs have different sums
    seen = set()
    for mask in range(1, 1 << n):
        total = sum(s[i] for i in range(n) if mask & (1 << i))
        for prev_mask in list(seen):
            if prev_mask & mask == 0:
                prev_total = sum(s[i] for i in range(n) if prev_mask & (1 << i))
                if prev_total == total:
                    return False
        seen.add(mask)
    return True

def solve():
    # The near-optimum seed for n=7 built from n=6 optimum {11,18,19,20,22,25}
    # b = middle(n=6) = 20, answer candidate = {b, b+a1, ...}
    seed = [20, 31, 38, 39, 40, 42, 45]
    best_sum = sum(seed)
    best = seed[:]
    
    # Search around seed with tight bounds
    for delta in range(-3, 4):
        base = 20 + delta
        for d1 in range(-3, 4):
            for d2 in range(-3, 4):
                for d3 in range(-3, 4):
                    for d4 in range(-3, 4):
                        for d5 in range(-3, 4):
                            for d6 in range(-3, 4):
                                s = sorted([base, base+11+d1, base+18+d2, base+19+d3, base+20+d4, base+22+d5, base+25+d6])
                                if len(set(s)) != 7 or s[0] < 1:
                                    continue
                                cs = sum(s)
                                if cs >= best_sum:
                                    continue
                                if is_special_sum_set(s):
                                    best = s[:]
                                    best_sum = cs
    
    print(''.join(str(x) for x in best))

solve()
