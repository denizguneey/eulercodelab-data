MOD = 1000000000

kBaseFactors = [
    [],
    ["0", "1"],
    ["00", "01", "10", "11"],
    ["001", "010", "011", "100", "101", "110"]
]

p_cache = {}
s_cache = {}

def p_count(n):
    if n <= 0: return 0
    if n == 1: return 2
    if n == 2: return 4
    if n == 3: return 6
    if n in p_cache: return p_cache[n]
    if n % 2 == 0:
        m = n // 2
        res = p_count(m) + p_count(m + 1)
    else:
        m = n // 2
        res = 2 * p_count(m + 1)
    p_cache[n] = res
    return res

def s_count(n):
    if n <= 0: return 0
    if n == 1: return 2
    if n == 2: return 6
    if n == 3: return 12
    if n in s_cache: return s_cache[n]
    if n % 2 == 0:
        m = n // 2
        res = 3 * s_count(m) + s_count(m + 1) - 8
    else:
        m = n // 2
        res = 4 * s_count(m) + 3 * p_count(m + 1) - 8
    s_cache[n] = res
    return res

def count_upto(length):
    if length <= 0: return 0
    return s_count(length) // 2

def find_length_for_index(n):
    lo = 1
    hi = 1
    while count_upto(hi) < n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if count_upto(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo

EMPTY = 0
LEAF = 1
CONCAT = 2
MU = 3

class Node:
    __slots__ = ['type', 'left', 'right', 'child', 'bits', 'len', 'first', 'last']
    def __init__(self):
        self.type = EMPTY
        self.left = -1
        self.right = -1
        self.child = -1
        self.bits = ""
        self.len = 0
        self.first = -1
        self.last = -1

class WordBuilder:
    def __init__(self, mod=MOD, max_i=64):
        self.mod = mod
        self.max_i = max_i
        self.base = [0] * (max_i + 2)
        self.base[0] = 2 % mod
        for i in range(1, len(self.base)):
            self.base[i] = (self.base[i - 1] * self.base[i - 1]) % mod
            
        self.pow_sum_cache = [{} for _ in range(len(self.base))]
        self.nodes = []
        self.eval_cache = []
        
        self.prefix_cache = {}
        self.suffix_cache = {}
        self.middle_cache = {}
        
        empty = Node()
        empty.type = EMPTY
        empty.len = 0
        self.nodes.append(empty)
        self.eval_cache.append(None)
        self.empty_id = 0
        
        leaf0 = Node()
        leaf0.type = LEAF
        leaf0.bits = "0"
        leaf0.len = 1
        leaf0.first = 0
        leaf0.last = 0
        self.nodes.append(leaf0)
        self.eval_cache.append(None)
        self.leaf0_id = len(self.nodes) - 1
        
        leaf1 = Node()
        leaf1.type = LEAF
        leaf1.bits = "1"
        leaf1.len = 1
        leaf1.first = 1
        leaf1.last = 1
        self.nodes.append(leaf1)
        self.eval_cache.append(None)
        self.leaf1_id = len(self.nodes) - 1

    def make_leaf(self, bits):
        if not bits: return self.empty_id
        if len(bits) == 1: return self.leaf0_id if bits[0] == '0' else self.leaf1_id
        node = Node()
        node.type = LEAF
        node.bits = bits
        node.len = len(bits)
        node.first = int(bits[0])
        node.last = int(bits[-1])
        self.nodes.append(node)
        self.eval_cache.append(None)
        return len(self.nodes) - 1

    def make_bit(self, b):
        return self.leaf0_id if b == 0 else self.leaf1_id

    def make_concat(self, left, right):
        if self.nodes[left].len == 0: return right
        if self.nodes[right].len == 0: return left
        node = Node()
        node.type = CONCAT
        node.left = left
        node.right = right
        node.len = self.nodes[left].len + self.nodes[right].len
        node.first = self.nodes[left].first if self.nodes[left].len else self.nodes[right].first
        node.last = self.nodes[right].last if self.nodes[right].len else self.nodes[left].last
        self.nodes.append(node)
        self.eval_cache.append(None)
        return len(self.nodes) - 1

    def make_mu(self, child):
        if self.nodes[child].len == 0: return self.empty_id
        node = Node()
        node.type = MU
        node.child = child
        node.len = self.nodes[child].len * 2
        node.first = self.nodes[child].first
        node.last = 1 - self.nodes[child].last
        self.nodes.append(node)
        self.eval_cache.append(None)
        return len(self.nodes) - 1

    def prefix(self, node_id):
        node = self.nodes[node_id]
        if node.len <= 1: return self.empty_id
        key = (node_id << 2) | 0
        if key in self.prefix_cache: return self.prefix_cache[key]
        res = self.empty_id
        if node.type == LEAF:
            res = self.make_leaf(node.bits[:-1])
        elif node.type == CONCAT:
            right_len = self.nodes[node.right].len
            if right_len > 1:
                res = self.make_concat(node.left, self.prefix(node.right))
            elif right_len == 1:
                res = node.left
            else:
                res = self.prefix(node.left)
        elif node.type == MU:
            p = self.prefix(node.child)
            mu_p = self.make_mu(p)
            bit = self.make_bit(self.nodes[node.child].last)
            res = self.make_concat(mu_p, bit)
        self.prefix_cache[key] = res
        return res

    def suffix(self, node_id):
        node = self.nodes[node_id]
        if node.len <= 1: return self.empty_id
        key = (node_id << 2) | 1
        if key in self.suffix_cache: return self.suffix_cache[key]
        res = self.empty_id
        if node.type == LEAF:
            res = self.make_leaf(node.bits[1:])
        elif node.type == CONCAT:
            left_len = self.nodes[node.left].len
            if left_len > 1:
                res = self.make_concat(self.suffix(node.left), node.right)
            elif left_len == 1:
                res = node.right
            else:
                res = self.suffix(node.right)
        elif node.type == MU:
            s = self.suffix(node.child)
            mu_s = self.make_mu(s)
            bit = self.make_bit(1 - self.nodes[node.child].first)
            res = self.make_concat(bit, mu_s)
        self.suffix_cache[key] = res
        return res

    def middle(self, node_id):
        node = self.nodes[node_id]
        if node.len <= 2: return self.empty_id
        key = (node_id << 2) | 2
        if key in self.middle_cache: return self.middle_cache[key]
        res = self.empty_id
        if node.type == LEAF:
            res = self.make_leaf(node.bits[1:-1])
        elif node.type == CONCAT:
            tmp = self.suffix(node_id)
            res = self.prefix(tmp)
        elif node.type == MU:
            m = self.middle(node.child)
            mu_m = self.make_mu(m)
            bit_left = self.make_bit(1 - self.nodes[node.child].first)
            bit_right = self.make_bit(self.nodes[node.child].last)
            res = self.make_concat(bit_left, self.make_concat(mu_m, bit_right))
        self.middle_cache[key] = res
        return res

    def odd_even_map(self, ancestor):
        mid = self.middle(ancestor)
        mu_mid = self.make_mu(mid)
        bit_left = self.make_bit(1 - self.nodes[ancestor].first)
        bit_right = self.make_bit(self.nodes[ancestor].last)
        return self.make_concat(bit_left, self.make_concat(mu_mid, bit_right))

    def odd_odd_map(self, ancestor):
        suf = self.suffix(ancestor)
        mu_suf = self.make_mu(suf)
        bit_left = self.make_bit(1 - self.nodes[ancestor].first)
        return self.make_concat(bit_left, mu_suf)

    def even_odd_map(self, ancestor):
        pref = self.prefix(ancestor)
        mu_pref = self.make_mu(pref)
        bit_right = self.make_bit(self.nodes[ancestor].last)
        return self.make_concat(mu_pref, bit_right)

    def pow_sum(self, i, length):
        cache = self.pow_sum_cache[i]
        if length in cache: return cache[length]
        if length == 0:
            res = (1 % self.mod, 0)
        elif length == 1:
            res = (self.base[i] % self.mod, 1 % self.mod)
        elif length % 2 == 0:
            p, s = self.pow_sum(i, length // 2)
            p2 = (p * p) % self.mod
            s2 = (s * (p + 1)) % self.mod
            res = (p2, s2)
        else:
            p, s = self.pow_sum(i, length - 1)
            p2 = (p * self.base[i]) % self.mod
            s2 = (s + p) % self.mod
            res = (p2, s2)
        cache[length] = res
        return res

    def pow_base(self, i, length):
        return self.pow_sum(i, length)[0]

    def sum_geom(self, i, length):
        return self.pow_sum(i, length)[1]

    def get_eval(self, node_id):
        cached = self.eval_cache[node_id]
        if cached is not None: return cached
        cached = [0] * (self.max_i + 2)
        self.eval_cache[node_id] = cached
        node = self.nodes[node_id]
        if node.len == 0:
            return cached
        if node.type == LEAF:
            for i in range(len(cached)):
                v = 0
                for c in node.bits:
                    v = ((v * self.base[i]) + int(c)) % self.mod
                cached[i] = v
        elif node.type == CONCAT:
            left = self.get_eval(node.left)
            right = self.get_eval(node.right)
            len_r = self.nodes[node.right].len
            for i in range(len(cached)):
                term = (left[i] * self.pow_base(i, len_r)) % self.mod
                cached[i] = (term + right[i]) % self.mod
        elif node.type == MU:
            child = self.get_eval(node.child)
            len_c = self.nodes[node.child].len
            for i in range(len(cached) - 1):
                sum_g = self.sum_geom(i + 1, len_c)
                factor = (self.base[i] + self.mod - 1) % self.mod
                term = (factor * child[i + 1]) % self.mod
                cached[i] = (sum_g + term) % self.mod
        return cached

def select_node(length, k, builder):
    if length <= 3:
        return builder.make_leaf(kBaseFactors[length][k - 1])
    if length % 2 == 0:
        n = length // 2
        size_O1 = p_count(n + 1) // 2
        size_E = p_count(n)
        if k <= size_O1:
            ancestor = select_node(n + 1, p_count(n + 1) // 2 + k, builder)
            return builder.odd_even_map(ancestor)
        if k <= size_O1 + size_E:
            ancestor = select_node(n, k - size_O1, builder)
            return builder.make_mu(ancestor)
        ancestor = select_node(n + 1, k - size_O1 - size_E, builder)
        return builder.odd_even_map(ancestor)
        
    n = length // 2
    size_O1 = p_count(n + 1) // 2
    size_E = p_count(n + 1)
    if k <= size_O1:
        ancestor = select_node(n + 1, p_count(n + 1) // 2 + k, builder)
        return builder.odd_odd_map(ancestor)
    if k <= size_O1 + size_E:
        ancestor = select_node(n + 1, k - size_O1, builder)
        return builder.even_odd_map(ancestor)
    ancestor = select_node(n + 1, k - size_O1 - size_E, builder)
    return builder.odd_odd_map(ancestor)

def compute_A_mod(n):
    if n == 0: return 0
    length = find_length_for_index(n)
    prev = count_upto(length - 1)
    k = n - prev
    offset = p_count(length) // 2 + k
    builder = WordBuilder(MOD)
    root = select_node(length, offset, builder)
    vals = builder.get_eval(root)
    return vals[0] % MOD

def solve():
    targets = [10**k for k in range(1, 19)]
    ans = 0
    for target in targets:
        ans = (ans + compute_A_mod(target)) % MOD
    return "{:09d}".format(ans)

if __name__ == '__main__':
    print(solve())
