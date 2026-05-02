# Problem 219: Skew-cost Coding
# Minimum cost prefix-free code for 10^9 symbols.
# Costs: 1 for bit '1', 4 for bit '0'.
# Greedy: expand cheapest leaf, adding children at cost c+1 and c+4.
# Formula: Cost(n) = 5*(n-1) + sum of (n-1) smallest internal node costs.
# Internal node costs follow recurrence: multiplicity[c] = multiplicity[c-1] + multiplicity[c-4]

def solve():
    n = 1000000000
    if n <= 1:
        print(0)
        return
    
    internal_nodes = n - 1
    
    # Count how many nodes have each cost level
    # multiplicity[c] = multiplicity[c-1] + multiplicity[c-4], multiplicity[0] = 1
    used = 0
    total_cost = 0
    multiplicity = [0] * 200  # grow as needed
    multiplicity[0] = 1
    
    cost = 0
    while used < internal_nodes:
        if cost >= len(multiplicity):
            multiplicity.extend([0] * 100)
        if cost == 0:
            multiplicity[0] = 1
        else:
            multiplicity[cost] = multiplicity[cost - 1]
            if cost >= 4:
                multiplicity[cost] += multiplicity[cost - 4]
        
        remaining = internal_nodes - used
        take = min(multiplicity[cost], remaining)
        total_cost += take * cost
        used += take
        cost += 1
    
    answer = 5 * internal_nodes + total_cost
    print(answer)

solve()
