def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inv(a, mod):
    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception("Inverse does not exist")
    return x % mod

class ModEntry:
    def __init__(self, mod, pow2, pow5, period_mod, mod2_part, mod5_part):
        self.mod = mod
        self.pow2 = pow2
        self.pow5 = pow5
        self.period_mod = period_mod
        self.mod2_part = mod2_part
        self.mod5_part = mod5_part
        if pow2 > 0 and pow5 > 0:
            self.inv_mod2_in5 = mod_inv(self.mod2_part % self.mod5_part, self.mod5_part)
        else:
            self.inv_mod2_in5 = 0

def build_mod_chain():
    entries = []
    
    entries.append(ModEntry(10**9, 9, 9, 4 * (5**8), 1 << 9, 5**9))
    
    for e5 in range(8, -1, -1):
        mod = 4 * (5**e5)
        period = 0 if e5 == 0 else 4 * (5**(e5 - 1))
        entries.append(ModEntry(mod, 2, e5, period, 4, 5**e5))
        
    return entries

def pow2_mod_composite(entry, residues, chain, exact_s, exact_known):
    if entry.mod == 1:
        return 0
    if entry.pow5 == 0:
        if entry.pow2 == 0:
            return 0
        if exact_known and exact_s < entry.pow2:
            return (1 << exact_s) % entry.mod
        return 0
        
    exp_mod = 0
    if entry.period_mod > 0:
        idx = next(i for i, c in enumerate(chain) if c.mod == entry.period_mod)
        exp_mod = residues[idx]
        
    p5 = mod_pow(2, exp_mod, entry.mod5_part)
    
    if entry.pow2 == 0:
        return p5
        
    p2 = 0
    if exact_known and exact_s < entry.pow2:
        p2 = (1 << exact_s) % entry.mod2_part
        
    diff = (p5 - p2) % entry.mod5_part
    adjusted = (diff + entry.mod5_part) % entry.mod5_part
    t = (adjusted * entry.inv_mod2_in5) % entry.mod5_part
    x = p2 + entry.mod2_part * t
    return x % entry.mod

def compute_h_mod(s0, m):
    kMod = 1000000000
    chain = build_mod_chain()
    residues = [s0 % c.mod for c in chain]
    
    exact_s = s0
    exact_known = True
    kExactLimit = 1000
    
    sum_mod = 0
    for i in range(m + 1):
        p_main = pow2_mod_composite(chain[0], residues, chain, exact_s, exact_known)
        term = (residues[0] * ((p_main + kMod - 1) % kMod)) % kMod
        sum_mod = (sum_mod + term) % kMod
        
        if i == m:
            break
            
        next_residues = [0] * len(chain)
        for j, c in enumerate(chain):
            p = pow2_mod_composite(c, residues, chain, exact_s, exact_known)
            next_residues[j] = (residues[j] * p) % c.mod
            
        residues = next_residues
        
        if exact_known:
            if exact_s > 20:
                exact_known = False
            else:
                p2 = 1 << exact_s
                if p2 > kExactLimit or exact_s > kExactLimit // max(1, p2):
                    exact_known = False
                else:
                    exact_s *= p2
                    if exact_s > kExactLimit:
                        exact_known = False
                        
    return sum_mod

def goodstein_small(n):
    g = n
    base = 2
    count = 0
    while g > 0:
        count += 1
        digits = []
        x = g
        while x > 0:
            digits.append(x % base)
            x //= base
        if not digits:
            digits.append(0)
            
        next_val = 0
        for d in reversed(digits):
            next_val = next_val * (base + 1) + d
            
        g = next_val - 1
        base += 1
        
    return count

def compute_g_mod(n, g_small):
    kMod = 1000000000
    if n < 8:
        return g_small[n] % kMod
    low = n - 8
    t = g_small[low]
    s = t + 3
    m = int(t + 2)
    h = compute_h_mod(s, m)
    return (t + h) % kMod

def solve():
    g_small = [0] * 8
    for n in range(1, 8):
        g_small[n] = goodstein_small(n)
        
    kMod = 1000000000
    ans = 0
    for n in range(1, 16):
        ans = (ans + compute_g_mod(n, g_small)) % kMod
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
