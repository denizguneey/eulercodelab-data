def day_k_q(day):
    if day == 0:
        return 2, 2
        
    if (day & 1) == 0:
        t = ((1 << day) - 1) // 3
        t2 = t * t
        t3 = t2 * t
        t4 = t2 * t2
        k = 3 * t2 + 5 * t + 2
        q = (21 * t4 + 70 * t3 + 87 * t2 + 46 * t + 8) // 4
        return k, q
        
    t = ((1 << day) - 2) // 3
    t2 = t * t
    t3 = t2 * t
    t4 = t2 * t2
    k = 3 * t2 + 7 * t + 4
    q = (21 * t4 + 98 * t3 + 171 * t2 + 134 * t + 40) // 4
    return k, q

def g_formula(n):
    if n == 0:
        return 2
    k, q = day_k_q(n - 1)
    return 3 * k * k - 2 * q

def solve():
    return str(g_formula(16))

if __name__ == "__main__":
    assert g_formula(1) == 8
    assert g_formula(2) == 28
    print(solve())
