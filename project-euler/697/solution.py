import math

def solve():
    # We want to find c such that GammaCDF(c, n) = 0.75 for n = 10^7.
    # The Wilson-Hilferty transformation provides an excellent approximation
    # for large n: c ≈ n * (1 - 1/(9n) + z * sqrt(1/(9n)))^3
    # where z is the 75th percentile of the standard normal distribution.
    
    n = 10000000.0
    # z = Phi^{-1}(0.75)
    z = 0.6744897501960817
    
    term = 1.0 - 1.0 / (9.0 * n) + z / math.sqrt(9.0 * n)
    c = n * (term ** 3)
    
    ans = c / math.log(10.0)
    
    return f"{ans:.2f}"

if __name__ == '__main__':
    print(solve())
