import math

def solve():
    def compute_moments(n):
        a0, a1 = 0, 1; c0, c1 = 0, 1
        if n == 0: return a0, c0
        if n == 1: return a1, c1
        for _ in range(2, n+1):
            a0, a1 = a1, a1+a0; c0, c1 = c1, c1+3*c0
        return a1, c1

    def skewness(n):
        a, c = compute_moments(n)
        var = a - 1.0
        if var <= 0: return 0.0
        m3 = c - 3.0*a + 2.0
        sigma = math.sqrt(var)
        return m3 / (sigma**3)

    return f"{skewness(50):.8f}"

if __name__ == '__main__':
    print(solve())
