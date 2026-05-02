MOD = 989898989

def norm_mod(x):
    return x % MOD

def add_mod(a, b):
    return (a + b) % MOD

def sub_mod(a, b):
    return (a - b) % MOD

def mul_mod(a, b):
    return (a * b) % MOD

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def mod_inv(a):
    return pow(a, MOD - 2, MOD)

def g8(n, inv3):
    if n <= 0: return 0
    if n == 1: return 1
    coeff = 14 if n % 2 == 0 else 20
    term1 = mul_mod(coeff, mul_mod(mod_pow(2, n // 2), inv3))
    term2 = norm_mod(6 * n - 15)
    return add_mod(term1, term2)

def compute_G(n):
    if n <= 1: return 0

    inv3 = mod_inv(3)
    pow2 = mod_pow(2, n // 2)
    pref = 35 if n % 2 == 0 else 50
    counter = mul_mod(pref, mul_mod(pow2, inv3))
    counter = sub_mod(counter, norm_mod(6 * n))
    counter = sub_mod(counter, mul_mod(35, inv3))

    lim = (n - 1) // 2
    nums = [0] * (lim + 1)
    nums[0] = 1
    if lim >= 1:
        nums[1] = 10

    for i in range(2, lim + 1):
        a = mul_mod(norm_mod(20 * i - 10), nums[i - 1])
        b = mul_mod(norm_mod(64 * i - 64), nums[i - 2])
        val = sub_mod(a, b)
        nums[i] = mul_mod(val, mod_inv(i))

    for i in range(lim + 1):
        counter = add_mod(counter, mul_mod(nums[i], g8(n - 2 * i, inv3)))
        
    return counter % MOD

def solve():
    return str(compute_G(9898))

if __name__ == "__main__":
    print(solve())
