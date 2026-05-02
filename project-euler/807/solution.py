import decimal

def compute_probability(n):
    decimal.getcontext().prec = 60
    BigFloat = decimal.Decimal
    
    m = n - 1
    max_deg = 2 * m
    offset = m
    
    def make_zero_poly():
        return [BigFloat(0) for _ in range(max_deg + 1)]
        
    curr = [make_zero_poly() for _ in range(2 * m + 1)]
    curr[offset][0] = BigFloat(1)
    
    for step in range(1, m + 1):
        next_poly = [make_zero_poly() for _ in range(2 * m + 1)]
        
        for s in range(-(step - 1), step):
            P = curr[offset + s]
            
            total = BigFloat(0)
            total_r = BigFloat(0)
            
            for i in range(max_deg + 1):
                if P[i] == 0: continue
                total += P[i] / BigFloat(i + 1)
                total_r += P[i] / BigFloat(i + 2)
                
            A = make_zero_poly()
            B = make_zero_poly()
            
            for i in range(max_deg + 1):
                if P[i] == 0: continue
                if i + 1 <= max_deg: A[i + 1] = P[i] / BigFloat(i + 1)
                if i + 2 <= max_deg: B[i + 2] = P[i] / BigFloat(i + 2)
                
            TminusA = make_zero_poly()
            TminusA[0] = total
            for i in range(1, max_deg + 1):
                TminusA[i] = -A[i]
                
            same = next_poly[offset + s]
            plus = next_poly[offset + s + 1]
            minus = next_poly[offset + s - 1]
            
            for i in range(max_deg + 1):
                i1 = A[i] + B[i]
                if i > 0: i1 -= A[i - 1]
                
                i2 = TminusA[i] + B[i]
                if i > 0: i2 += TminusA[i - 1]
                if i == 0: i2 -= total_r
                
                same[i] += i1 + i2
                
                jplus = -B[i]
                if i > 0: jplus += A[i - 1]
                plus[i] += jplus
                
                jminus = -B[i]
                if i == 0: jminus += total_r
                if i > 0: jminus -= TminusA[i - 1]
                minus[i] += jminus
                
        curr = next_poly
        
    def integrate_0_1(P):
        res = BigFloat(0)
        for i in range(max_deg + 1):
            if P[i] == 0: continue
            res += P[i] / BigFloat(i + 1)
        return res
        
    prob_zero = integrate_0_1(curr[offset])
    return prob_zero

def solve():
    ans = compute_probability(80)
    # The precision required is 10 decimal places
    return "{:.10f}".format(ans)

if __name__ == "__main__":
    print(solve())
