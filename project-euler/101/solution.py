# Problem 101: Optimum polynomial
# Find the sum of FITs for the generating polynomial 1-n+n²-n³+...+n¹⁰.

def solve():
    # Generate values from u(n) = sum((-1)^k * n^k, k=0..10)
    def u(n):
        return sum((-1)**k * n**k for k in range(11))
    
    values = [u(n) for n in range(1, 12)]
    
    total = 0
    for k in range(1, 11):  # use k data points
        # Lagrange interpolation at n = k+1
        xs = list(range(1, k+1))
        ys = values[:k]
        n = k + 1
        predicted = 0
        for i in range(k):
            term = ys[i]
            for j in range(k):
                if i != j:
                    term = term * (n - xs[j]) / (xs[i] - xs[j])
            predicted += term
        predicted = round(predicted)
        actual = values[k]
        if predicted != actual:
            total += predicted
    
    print(total)

solve()
