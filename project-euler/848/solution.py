from decimal import Decimal, getcontext

getcontext().prec = 50

def a_value(m, n):
    out = 0
    if n >= 1: out += min(m, 1)
    if n >= 2: out += min(m, 2)
    if n < 3: return out
    
    out += min(m, 3)
    idx = 4
    cnt = 3
    val = 6
    
    while idx <= n:
        take = min(cnt, n - idx + 1)
        out += take * min(m, val)
        idx += take
        cnt <<= 1
        val <<= 1
    return out

def p_value(m, n):
    a = a_value(m, n)
    den = m * n
    return Decimal(a) / Decimal(den)

def solve():
    p7 = [1] * 21
    p5 = [1] * 21
    for i in range(1, 21):
        p7[i] = p7[i - 1] * 7
        p5[i] = p5[i - 1] * 5
        
    ans = Decimal('0')
    for i in range(21):
        for j in range(21):
            ans += p_value(p7[i], p5[j])
            
    return f"{ans:.8f}"

if __name__ == "__main__":
    print(solve())
