def solve():
    n = 10000000
    MOD = 1000000007
    a = [0] * (n + 1)
    
    num = [0] * 13
    num[0] = 1
    num[1] = -1
    num[4] = 1
    num[5] = 1
    num[6] = -2
    num[7] = 1
    num[8] = 1
    num[11] = -1
    num[12] = 1
    
    for i in range(13):
        num[i] = (num[i] % MOD + MOD) % MOD
        
    for i in range(n + 1):
        v = num[i] if i <= 12 else 0
        
        if i >= 1: v += a[i - 1]
        if i >= 6: v += a[i - 6]
        if i >= 9: v -= a[i - 9]
        if i >= 10: v += a[i - 10]
        if i >= 11: v -= a[i - 11]
        if i >= 13: v -= a[i - 13]
        if i >= 19: v += a[i - 19]
        if i >= 21: v += a[i - 21]
        if i >= 22: v -= a[i - 22]
        if i >= 23: v += a[i - 23]
        if i >= 26: v -= a[i - 26]
        if i >= 31: v -= a[i - 31]
        if i >= 32: v += a[i - 32]
        
        a[i] = v % MOD
        
    return str(a[n])

if __name__ == '__main__':
    print(solve())
