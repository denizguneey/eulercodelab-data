MOD = 1000000007
MAX_BITS = 64

class Aggregates:
    def __init__(self):
        self.cnt = [0] * (MAX_BITS + 1)
        self.sx = [0] * (MAX_BITS + 1)
        self.sx2 = [0] * (MAX_BITS + 1)
        self.sc = [0] * (MAX_BITS + 1)
        self.sc2 = [0] * (MAX_BITS + 1)
        self.sxc = [0] * (MAX_BITS + 1)
        self.sxc2 = [0] * (MAX_BITS + 1)
        self.sx2c = [0] * (MAX_BITS + 1)
        self.sx2c2 = [0] * (MAX_BITS + 1)

def build_aggregates():
    ag = Aggregates()
    ag.cnt[0] = 1
    
    for m in range(MAX_BITS):
        n = ag.cnt[m]
        sx = ag.sx[m]
        sx2 = ag.sx2[m]
        sc = ag.sc[m]
        sc2 = ag.sc2[m]
        sxc = ag.sxc[m]
        sxc2 = ag.sxc2[m]
        sx2c = ag.sx2c[m]
        sx2c2 = ag.sx2c2[m]
        
        two_sx = (2 * sx) % MOD
        four_sx = (4 * sx) % MOD
        four_sx2 = (4 * sx2) % MOD
        two_sc = (2 * sc) % MOD
        
        e_cnt = n
        e_sx = two_sx
        e_sx2 = four_sx2
        e_sc = sc
        e_sc2 = sc2
        e_sxc = (2 * sxc) % MOD
        e_sxc2 = (2 * sxc2) % MOD
        e_sx2c = (4 * sx2c) % MOD
        e_sx2c2 = (4 * sx2c2) % MOD
        
        o_cnt = n
        o_sx = (two_sx + n) % MOD
        o_sx2 = (four_sx2 + four_sx + n) % MOD
        o_sc = (sc + n) % MOD
        o_sc2 = (sc2 + two_sc + n) % MOD
        
        o_sxc = (2 * sxc + sc + two_sx + n) % MOD
        o_sxc2 = (2 * sxc2 + sc2 + 4 * sxc + 2 * sc + two_sx + n) % MOD
        o_sx2c = (4 * sx2c + 4 * sxc + sc + four_sx2 + four_sx + n) % MOD
        o_sx2c2 = (4 * sx2c2 + 4 * sxc2 + sc2 + 8 * sx2c + 8 * sxc + 2 * sc + four_sx2 + four_sx + n) % MOD
        
        ag.cnt[m + 1] = (e_cnt + o_cnt) % MOD
        ag.sx[m + 1] = (e_sx + o_sx) % MOD
        ag.sx2[m + 1] = (e_sx2 + o_sx2) % MOD
        ag.sc[m + 1] = (e_sc + o_sc) % MOD
        ag.sc2[m + 1] = (e_sc2 + o_sc2) % MOD
        ag.sxc[m + 1] = (e_sxc + o_sxc) % MOD
        ag.sxc2[m + 1] = (e_sxc2 + o_sxc2) % MOD
        ag.sx2c[m + 1] = (e_sx2c + o_sx2c) % MOD
        ag.sx2c2[m + 1] = (e_sx2c2 + o_sx2c2) % MOD
        
    return ag

def block_sum(prefix_value_mod, prefix_popcount, lower_bits, ag):
    p = prefix_value_mod % MOD
    c = prefix_popcount % MOD
    p2 = (p * p) % MOD
    c2 = (c * c) % MOD
    
    ans = 0
    ans = (ans + ag.cnt[lower_bits] * p2 % MOD * c2) % MOD
    ans = (ans + ag.sc[lower_bits] * p2 % MOD * 2 % MOD * c) % MOD
    ans = (ans + ag.sc2[lower_bits] * p2) % MOD
    ans = (ans + ag.sx[lower_bits] * p % MOD * 2 % MOD * c2) % MOD
    ans = (ans + ag.sxc[lower_bits] * p % MOD * 4 % MOD * c) % MOD
    ans = (ans + ag.sxc2[lower_bits] * p % MOD * 2) % MOD
    ans = (ans + ag.sx2[lower_bits] * c2) % MOD
    ans = (ans + ag.sx2c[lower_bits] * 2 % MOD * c) % MOD
    ans = (ans + ag.sx2c2[lower_bits]) % MOD
    
    return ans

def S(n, ag, pow2_mod):
    ans = 0
    prefix_value_mod = 0
    prefix_popcount = 0
    
    for bit in range(MAX_BITS - 1, -1, -1):
        if ((n >> bit) & 1) == 0:
            continue
            
        ans = (ans + block_sum(prefix_value_mod, prefix_popcount, bit, ag)) % MOD
        prefix_value_mod = (prefix_value_mod + pow2_mod[bit]) % MOD
        prefix_popcount += 1
        
    p2 = (prefix_value_mod * prefix_value_mod) % MOD
    c = prefix_popcount % MOD
    c2 = (c * c) % MOD
    ans = (ans + p2 * c2) % MOD
    
    return ans

def solve():
    ag = build_aggregates()
    pow2_mod = [0] * (MAX_BITS + 1)
    pow2_mod[0] = 1
    for i in range(1, MAX_BITS + 1):
        pow2_mod[i] = (pow2_mod[i-1] * 2) % MOD
        
    return str(S(10000000000000000, ag, pow2_mod))

if __name__ == "__main__":
    print(solve())
