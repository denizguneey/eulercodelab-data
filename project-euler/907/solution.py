def S_mod(n):
    MOD = 1000000007
    if n <= 0:
        return 0
    base = [0, 2, 2, 6, 12, 16, 22, 36, 58, 82]
    if n <= 9:
        return base[n] % MOD
        
    a = base[:]
    for i in range(10, n + 1):
        v = 0
        v = (v + 2 * a[9]) % MOD
        v = (v - 3 * a[8]) % MOD
        v = (v + 5 * a[7]) % MOD
        v = (v - 4 * a[6]) % MOD
        v = (v + 4 * a[5]) % MOD
        v = (v - 3 * a[4]) % MOD
        v = (v + a[3]) % MOD
        v = (v - a[2]) % MOD
        if v < 0:
            v += MOD
            
        for j in range(2, 10):
            a[j - 1] = a[j]
        a[9] = v
        
    return a[9]

def solve():
    return str(S_mod(10000000))

if __name__ == "__main__":
    print(solve())
