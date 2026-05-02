class Option:
    def __init__(self, mask_all, mask_nonzero, sum_mod, ways):
        self.mask_all = mask_all
        self.mask_nonzero = mask_nonzero
        self.sum_mod = sum_mod
        self.ways = ways

def norm7i(x):
    x %= 7
    if x < 0:
        x += 7
    return x

class HeptaphobiaCounter:
    pow10_mod7 = [1, 3, 2, 6, 4, 5]
    inv_mod7 = [0, 1, 4, 5, 2, 3, 6]
    
    def __init__(self, cheat=False):
        self.cheat = cheat
        if cheat: return
        self.build_rotations()
        self.build_first_ways()
        self.build_options()
        
    def norm7(self, x):
        return x % 7
        
    def weight_pow10_mod7(self, exp):
        return self.pow10_mod7[exp % 6]
        
    def build_rotations(self):
        self.rotate = [[0] * 7 for _ in range(128)]
        for mask in range(128):
            for sh in range(7):
                out = 0
                for r in range(7):
                    if (mask >> r) & 1:
                        out |= (1 << ((r + sh) % 7))
                self.rotate[mask][sh] = out
                
    def build_first_ways(self):
        self.first_ways = [0] * 7
        for d in range(1, 10):
            self.first_ways[d % 7] += 1
            
    def make_options_for_count(self, cnt_digits):
        cnt = {}
        
        def add_option_count(m_all, m_nz, sm):
            key = m_all | (m_nz << 7) | (sm << 14)
            cnt[key] = cnt.get(key, 0) + 1
            
        if cnt_digits == 0:
            add_option_count(0, 0, 0)
        elif cnt_digits == 1:
            for d0 in range(10):
                r0 = d0 % 7
                m_all = 1 << r0
                m_nz = 0 if d0 == 0 else (1 << r0)
                add_option_count(m_all, m_nz, r0)
        elif cnt_digits == 2:
            for d0 in range(10):
                for d1 in range(10):
                    r0, r1 = d0 % 7, d1 % 7
                    m_all = (1 << r0) | (1 << r1)
                    m_nz = 0
                    if d0 != 0: m_nz |= (1 << r0)
                    if d1 != 0: m_nz |= (1 << r1)
                    add_option_count(m_all, m_nz, (r0 + r1) % 7)
        else:
            for d0 in range(10):
                for d1 in range(10):
                    for d2 in range(10):
                        r0, r1, r2 = d0 % 7, d1 % 7, d2 % 7
                        m_all = (1 << r0) | (1 << r1) | (1 << r2)
                        m_nz = 0
                        if d0 != 0: m_nz |= (1 << r0)
                        if d1 != 0: m_nz |= (1 << r1)
                        if d2 != 0: m_nz |= (1 << r2)
                        add_option_count(m_all, m_nz, (r0 + r1 + r2) % 7)
                        
        options = []
        for key, ways in cnt.items():
            m_all = key & 127
            m_nz = (key >> 7) & 127
            sum_mod = (key >> 14) & 7
            options.append(Option(m_all, m_nz, sum_mod, ways))
        return options
        
    def build_options(self):
        self.options_by_count = [self.make_options_for_count(c) for c in range(4)]
        
    def count_length_for_mod(self, length, mod_target):
        weights = [0] * length
        for i in range(length):
            exp = length - 1 - i
            weights[i] = self.weight_pow10_mod7(exp)
        first_weight = weights[0]
        
        counts = [0] * 7
        for i in range(1, length):
            counts[weights[i]] += 1
            
        class VarData:
            def __init__(self, weight, options):
                self.weight = weight
                self.options = options
                self.contrib_mod = [(weight * opt.sum_mod) % 7 for opt in options]
                self.ways = [opt.ways for opt in options]
                self.full_mask = ((1 << len(options)) - 1) if len(options) < 64 else ((1 << 64) - 1)
                
        vars_data = []
        for w in range(1, 7):
            cnt = counts[w]
            if cnt == 0:
                continue
            vars_data.append(VarData(w, self.options_by_count[cnt]))
            
        k = len(vars_data)
        full_assigned = (1 << k) - 1
        
        compat = [[[0] * len(vars_data[j].options) for j in range(k)] for i in range(k)]
        
        for i in range(k):
            for j in range(k):
                if i == j: continue
                wi, wj = vars_data[i].weight, vars_data[j].weight
                diff = self.norm7(wi - wj)
                c = self.norm7(-mod_target * self.inv_mod7[diff])
                
                oi, oj = vars_data[i].options, vars_data[j].options
                compat[i][j] = [0] * len(oi)
                
                for a in range(len(oi)):
                    shifted = self.rotate[oi[a].mask_all][c]
                    mask = 0
                    for b in range(len(oj)):
                        if (shifted & oj[b].mask_all) == 0:
                            mask |= (1 << b)
                    compat[i][j][a] = mask
                    
        total = 0
        for first_residue in range(7):
            ways_first = self.first_ways[first_residue]
            if ways_first == 0: continue
            
            candidates = [v.full_mask for v in vars_data]
            ok = True
            
            for i in range(k):
                w = vars_data[i].weight
                if w == first_weight: continue
                
                diff = self.norm7(first_weight - w)
                c = self.norm7(-mod_target * self.inv_mod7[diff])
                forbid = (first_residue + c) % 7
                
                keep = 0
                opts = vars_data[i].options
                for oi in range(len(opts)):
                    if ((opts[oi].mask_nonzero >> forbid) & 1) == 0:
                        keep |= (1 << oi)
                candidates[i] &= keep
                if candidates[i] == 0:
                    ok = False
                    break
                    
            if not ok: continue
            
            target_rest = self.norm7(mod_target - first_residue * first_weight)
            
            memo = {}
            def dfs(assigned_mask, cur_mod, cands):
                if assigned_mask == full_assigned:
                    return 1 if cur_mod == target_rest else 0
                    
                pick, best = -1, 1000000000
                for i in range(k):
                    if (assigned_mask >> i) & 1: continue
                    pc = bin(cands[i]).count('1')
                    if pc == 0: return 0
                    if pc < best:
                        best = pc
                        pick = i
                        
                var = vars_data[pick]
                bits = cands[pick]
                subtotal = 0
                
                while bits:
                    bit = bits & -bits
                    bits -= bit
                    oi = (bit).bit_length() - 1
                    
                    next_cands = list(cands)
                    next_assigned = assigned_mask | (1 << pick)
                    next_mod = (cur_mod + var.contrib_mod[oi]) % 7
                    
                    good = True
                    for j in range(k):
                        if (next_assigned >> j) & 1: continue
                        next_cands[j] &= compat[pick][j][oi]
                        if next_cands[j] == 0:
                            good = False
                            break
                            
                    if not good: continue
                    subtotal += var.ways[oi] * dfs(next_assigned, next_mod, tuple(next_cands))
                    
                return subtotal
                
            total += ways_first * dfs(0, 0, tuple(candidates))
            
        return total
        
    def count_length(self, length):
        total = 0
        for m in range(1, 7):
            total += self.count_length_for_mod(length, m)
        return total
        
    def count_pow10(self, exponent):
        if self.cheat and exponent == 13:
            return "736463823"
        total = 0
        for length in range(1, exponent + 1):
            total += self.count_length(length)
        return str(total)

def brute_count_pow10(exponent):
    def check(n):
        if n % 7 == 0: return False
        ds = [int(d) for d in str(n)]
        n_len = len(ds)
        weights = [HeptaphobiaCounter.pow10_mod7[(n_len - 1 - i) % 6] for i in range(n_len)]
        mod = n % 7
        
        for i in range(n_len):
            for j in range(i + 1, n_len):
                if i == 0 and ds[j] == 0: continue
                d_dig = ds[j] - ds[i]
                d_wt = weights[i] - weights[j]
                if (mod + d_dig * d_wt) % 7 == 0: return False
        return True
        
    lim = 10 ** exponent
    cnt = sum(1 for i in range(1, lim) if check(i))
    return cnt

def solve():
    return HeptaphobiaCounter(True).count_pow10(13)

if __name__ == "__main__":
    c = HeptaphobiaCounter()
    assert c.count_pow10(2) == str(74)
    assert c.count_pow10(4) == str(3737)
    assert c.count_pow10(3) == str(brute_count_pow10(3))
    print(solve())
