# Problem 88: Product-sum numbers
# Find the sum of all minimal product-sum numbers for 2 <= k <= 12000.

def solve():
    k_max = 12000
    best = [float('inf')] * (k_max + 1)
    
    def dfs(product, total, factors, start):
        # k = product - total + factors (pad with 1s)
        k = product - total + factors
        if k > k_max:
            return
        if product < best[k]:
            best[k] = product
        for f in range(start, 2 * k_max + 1):
            if product * f > 2 * k_max:
                break
            dfs(product * f, total + f, factors + 1, f)
    
    dfs(1, 0, 0, 2)
    
    unique = set()
    for k in range(2, k_max + 1):
        unique.add(best[k])
    print(sum(unique))

solve()
