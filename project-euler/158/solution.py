# Problem 158: Exploring strings for which only one character comes lexicographically after its neighbour

from math import comb

def solve():
    alphabet = 26
    best = 0
    for n in range(1, alphabet + 1):
        # Eulerian number for exactly 1 descent in permutation of n distinct elements
        eulerian = 2**n - n - 1
        p = comb(alphabet, n) * eulerian
        best = max(best, p)
    print(best)

solve()
