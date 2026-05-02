def solve():
    kMod = 1000000007
    n_power = 12345678
    
    ans = 0
    c_k = 1
    s_k = 0
    pow4_k = 1
    odd_pow4 = 4
    
    for m in range(n_power):
        if (m & 1) == 0:
            ans = (ans + c_k * pow4_k + s_k) % kMod
            next_s = (2 * s_k + (c_k + 2) * pow4_k) % kMod
            s_k = next_s
            c_k = (2 * c_k) % kMod
            pow4_k = (4 * pow4_k) % kMod
        else:
            ans = (ans + odd_pow4 - 1) % kMod
            odd_pow4 = (4 * odd_pow4) % kMod
            
    if (n_power & 1) == 0:
        ans = (ans + pow(2, n_power, kMod)) % kMod
        
    return str(ans)

if __name__ == "__main__":
    print(solve())
