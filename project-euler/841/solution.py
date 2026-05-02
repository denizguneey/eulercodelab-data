import math

def area_A(p, q):
    dp = float(p)
    delta = math.pi / dp
    sd = math.sin(delta)
    cd = math.cos(delta)
    tan_delta = sd / cd
    
    sum_diff = 0.0
    if q >= 2:
        k = 2
        sin_k = sd
        cos_k = cd
        sign = 1.0
        corr = 0.0  # Kahan compensation
        while k <= q:
            sin_next = sin_k * cd + cos_k * sd
            cos_next = cos_k * cd - sin_k * sd
            diff = sd / (cos_k * cos_next)
            term = sign * diff
            
            y = term - corr
            t = sum_diff + y
            corr = (t - sum_diff) - y
            sum_diff = t
            
            sin_k = sin_next
            cos_k = cos_next
            sign = -sign
            k += 1
            
    inner = sum_diff - tan_delta
    outside_sign = 1.0 if (q % 2) == 0 else -1.0
    return dp * outside_sign * inner

def fibonacci_sequence(count):
    fibs = [1, 1]
    for i in range(2, count):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs

def solve():
    fibs = fibonacci_sequence(36)
    ans = 0.0
    corr = 0.0
    for n in range(3, 35):
        p = fibs[n]
        q = fibs[n - 2]
        term = area_A(p, q)
        y = term - corr
        t = ans + y
        corr = (t - ans) - y
        ans = t
        
    ans = round(ans * 10**10) / 10**10
    return f"{ans:.10f}"

if __name__ == "__main__":
    print(solve())
