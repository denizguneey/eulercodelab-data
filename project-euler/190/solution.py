# Problem 190: Maximising a weighted product
# For each m, maximize Prod(x_i^i) subject to sum(x_i) = m. Optimal: x_i = 2i/(m+1).

import math

def solve():
    total = 0
    for m in range(2, 16):
        log_sum = 0.0
        for i in range(1, m+1):
            xi = 2.0 * i / (m + 1)
            log_sum += i * math.log(xi)
        total += int(math.exp(log_sum) + 1e-12)
    print(total)

solve()
