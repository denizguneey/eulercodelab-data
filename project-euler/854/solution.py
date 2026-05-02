MOD = 1234567891

def mul_mod(a, b):
    return (a * b) % MOD

def compute_P(n):
    ans = 1
    if n >= 3:
        ans = mul_mod(ans, 2)

    half = n // 2
    f_prev = 0
    f_cur = 1
    l_prev = 2
    l_cur = 1

    for k in range(1, half + 1):
        fk = 1 if k == 1 else 0
        lk = 1 if k == 1 else 0

        if k >= 2:
            fn = (f_prev + f_cur) % MOD
            f_prev = f_cur
            f_cur = fn
            fk = f_cur

            ln = (l_prev + l_cur) % MOD
            l_prev = l_cur
            l_cur = ln
            lk = l_cur

        if k >= 2:
            ans = mul_mod(ans, lk if (k & 1) else fk)

    return ans

def solve():
    return str(compute_P(1000000))

if __name__ == "__main__":
    print(solve())
