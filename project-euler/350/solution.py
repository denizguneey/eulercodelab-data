MOD = 104060401

def mod_pow(base, exp):
    return pow(base, exp, MOD)

def build_spf(n):
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def solve_350(G, L, N):
    K = L // G
    spf = build_spf(K)
    
    max_exp = 0
    x = K
    while x > 0:
        x //= 2
        max_exp += 1
        
    pows = [0] * (max_exp + 2)
    for b in range(max_exp + 2):
        if b == 0:
            pows[b] = 0
        else:
            pows[b] = mod_pow(b, N)
            
    local = [0] * (max_exp + 1)
    for a in range(1, max_exp + 1):
        val = (pows[a + 1] - 2 * pows[a] + pows[a - 1]) % MOD
        local[a] = (val + MOD) % MOD
        
    h = [0] * (K + 1)
    h[1] = 1
    
    for n in range(2, K + 1):
        x = n
        value = 1
        while x > 1:
            p = spf[x]
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            value = (value * local[e]) % MOD
        h[n] = value
        
    answer = 0
    for m in range(1, K + 1):
        weight = L // m - G + 1
        w = weight % MOD
        answer = (answer + h[m] * w) % MOD
        
    return answer

def solve():
    G = 1000000
    L = 1000000000000
    N = 1000000000000000000
    ans = solve_350(G, L, N)
    return str(ans)

if __name__ == '__main__':
    print(solve())
