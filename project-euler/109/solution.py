# Problem 109: Darts
# How many distinct ways can a player check out with a score less than 100?

def solve():
    singles = [(f"S{i}", i) for i in range(1, 21)] + [("S25", 25)]
    doubles = [(f"D{i}", 2*i) for i in range(1, 21)] + [("D25", 50)]
    trebles = [(f"T{i}", 3*i) for i in range(1, 21)]
    
    all_throws = singles + doubles + trebles
    limit = 100
    count = 0
    
    # Checkout with just a double
    for _, d in doubles:
        if d < limit:
            count += 1
    
    # One throw + double
    for _, a in all_throws:
        for _, d in doubles:
            if a + d < limit:
                count += 1
    
    # Two throws + double (unordered first two)
    for i in range(len(all_throws)):
        for j in range(i, len(all_throws)):
            for _, d in doubles:
                if all_throws[i][1] + all_throws[j][1] + d < limit:
                    count += 1
    
    print(count)

solve()
