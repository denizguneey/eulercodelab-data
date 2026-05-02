def solve():
    n = 10000019
    c = 100
    MOD = 1000000000

    cnt = [0] * 8
    buf = [0] * 8
    moves = [2, 3, 5, 7]
    
    for i in range(n):
        g = 0
        if i >= 2:
            seen = [False] * 6
            for d in moves:
                if i >= d:
                    seen[buf[(i - d) & 7]] = True
            while g < 6 and seen[g]:
                g += 1
        buf[i & 7] = g
        cnt[g] += 1

    cnt2 = [0] * 8
    for a in range(8):
        if cnt[a] == 0: continue
        for b in range(8):
            if cnt[b] == 0: continue
            cnt2[a ^ b] += cnt[a] * cnt[b]
            
    cnt2m = [x % MOD for x in cnt2]
    
    dp = [0] * 8
    dp[0] = 1
    
    for _ in range(c):
        ndp = [0] * 8
        for x in range(8):
            vx = dp[x]
            if vx == 0: continue
            for g in range(8):
                ndp[x ^ g] = (ndp[x ^ g] + vx * cnt2m[g]) % MOD
        dp = ndp
        
    n2m = ((n % MOD) * (n % MOD)) % MOD
    total = pow(n2m, c, MOD)
    ans = (total + MOD - dp[0]) % MOD
    return "{:09d}".format(ans)

if __name__ == '__main__':
    print(solve())
