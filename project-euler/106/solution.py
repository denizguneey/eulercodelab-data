# Problem 106: Special subset sums: meta-testing
# For n=12, how many subset pairs need testing (not auto-ordered)?

from itertools import combinations
from math import comb

def solve():
    n = 12
    count = 0
    for k in range(2, n // 2 + 1):
        # Number of pairs of disjoint subsets of same size k from {0,...,n-1}
        masks = list(combinations(range(n), k))
        for i in range(len(masks)):
            for j in range(i+1, len(masks)):
                a, b = masks[i], masks[j]
                if any(x in b for x in a):
                    continue
                # Check if auto-ordered: for sorted a and b, can they be interleaved
                # such that one always dominates? If a[i] < b[i] for all i or vice versa
                sa = sorted(a)
                sb = sorted(b)
                if all(sa[m] < sb[m] for m in range(k)) or all(sb[m] < sa[m] for m in range(k)):
                    continue
                count += 1
    print(count)

solve()
