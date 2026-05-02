kMod = 1000000007

def binom_large_n_small_k(n, k, inv_fact):
    if k < 0: return 0
    nm = int(n % kMod)
    if nm < k: return 0
    num = 1
    for i in range(k):
        num = (num * (nm - i)) % kMod
    return (num * inv_fact[k]) % kMod

def S(n, k, b, inv_fact):
    masks = 1 << k
    add = [0] * k
    p = 1
    for m in range(1, k + 1):
        p *= b
        add[m - 1] = p + 1
        
    shift = [0] * masks
    for mask in range(1, masks):
        bit = (mask & -mask).bit_length() - 1
        prev = mask & (mask - 1)
        shift[mask] = shift[prev] + add[bit]
        
    ans = 0
    for mask in range(masks):
        sh = shift[mask]
        if sh > n: continue
        N = (n - sh) + k
        term = binom_large_n_small_k(N, k, inv_fact)
        if (mask.bit_count() & 1) == 0:
            ans = (ans + term) % kMod
        else:
            ans = (ans - term) % kMod
            
    return ans

def solve():
    fact = [1] * 16
    inv_fact = [1] * 16
    for i in range(1, 16):
        fact[i] = (fact[i - 1] * i) % kMod
    inv_fact[15] = pow(fact[15], kMod - 2, kMod)
    for i in range(15, 0, -1):
        inv_fact[i - 1] = (inv_fact[i] * i) % kMod
        
    total = 0
    for k in range(10, 16):
        n = 10**k
        term = S(n, k, k, inv_fact)
        total = (total + term) % kMod
        
    return str(total)

if __name__ == '__main__':
    print(solve())
