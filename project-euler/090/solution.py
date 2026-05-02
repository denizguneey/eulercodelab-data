# Problem 90: Cube digit pairs
# How many distinct arrangements of two cubes allow all square numbers to be displayed?

from itertools import combinations

def solve():
    squares = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]
    
    def has_digit(die, d):
        if d == 6 or d == 9:
            return 6 in die or 9 in die
        return d in die
    
    def can_display(d1, d2):
        for a, b in squares:
            if not ((has_digit(d1, a) and has_digit(d2, b)) or
                    (has_digit(d1, b) and has_digit(d2, a))):
                return False
        return True
    
    dice = list(combinations(range(10), 6))
    count = 0
    for i in range(len(dice)):
        for j in range(i, len(dice)):
            if can_display(dice[i], dice[j]):
                count += 1
    print(count)

solve()
