import math
import random
import heapq
import sys
import bisect

sys.setrecursionlimit(20000)

prime_cache = {}
factor_cache = {}
best_divisor_cache = {}
shape_cache = {}

shapes = [{'left': -1, 'right': -1, 'leaves': 1}]
shape_id_by_children = {}

MAXVAL = 0

class Sequence:
    def __init__(self):
        self.needed = False
        self.leaf = False
        self.started = False
        self.exhausted = False
        self.left = -1
        self.right = -1
        self.next_i = 0
        self.next_prime = 2
        self.values = []
        self.heap = []
        self.in_heap = set()

seqs = []

def mul_mod(a, b, mod):
    return (a * b) % mod

def pow_mod(a, e, mod):
    return pow(a, e, mod)

def is_prime64(n):
    if n in prime_cache: return prime_cache[n]
    if n < 2:
        prime_cache[n] = False
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            prime_cache[n] = (n == p)
            return n == p
    
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
        
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0: continue
        x = pow_mod(a, d, n)
        if x == 1 or x == n - 1: continue
        composite = True
        for r in range(1, s):
            x = mul_mod(x, x, n)
            if x == n - 1:
                composite = False
                break
        if composite:
            prime_cache[n] = False
            return False
            
    prime_cache[n] = True
    return True

def pollard_rho(n):
    if (n & 1) == 0: return 2
    if n % 3 == 0: return 3
    
    while True:
        c = random.randint(2, n - 2)
        x = random.randint(2, n - 2)
        y = x
        d = 1
        
        while d == 1:
            x = (mul_mod(x, x, n) + c) % n
            y = (mul_mod(y, y, n) + c) % n
            y = (mul_mod(y, y, n) + c) % n
            diff = x - y if x > y else y - x
            d = math.gcd(diff, n)
            
        if d != n: return d

def factor_rec(n, fac):
    if n == 1: return
    if is_prime64(n):
        fac[n] = fac.get(n, 0) + 1
        return
    d = pollard_rho(n)
    factor_rec(d, fac)
    factor_rec(n // d, fac)

def factorize(n):
    if n in factor_cache: return factor_cache[n]
    fac = {}
    factor_rec(n, fac)
    factor_cache[n] = fac
    return fac

def gen_divisors_rec(f, idx, cur, out):
    if idx == len(f):
        out.append(cur)
        return
    p, e = f[idx]
    v = 1
    for _ in range(e + 1):
        gen_divisors_rec(f, idx + 1, cur * v, out)
        v *= p

def best_divisor_le_sqrt(n):
    if n in best_divisor_cache: return best_divisor_cache[n]
    
    fac_map = factorize(n)
    f = list(fac_map.items())
    divs = []
    gen_divisors_rec(f, 0, 1, divs)
    
    root = math.isqrt(n)
    best = 1
    for d in divs:
        if d <= root and d > best:
            best = d
            
    best_divisor_cache[n] = best
    return best

def make_shape(l, r):
    key = (l, r)
    if key in shape_id_by_children: return shape_id_by_children[key]
    
    s = {'left': l, 'right': r, 'leaves': shapes[l]['leaves'] + shapes[r]['leaves']}
    idx = len(shapes)
    shapes.append(s)
    shape_id_by_children[key] = idx
    return idx

def shape_of(n):
    if n in shape_cache: return shape_cache[n]
    if is_prime64(n):
        shape_cache[n] = 0
        return 0
        
    d = best_divisor_le_sqrt(n)
    a = d
    b = n // d
    if a > b: a, b = b, a
    
    l = shape_of(a)
    r = shape_of(b)
    idx = make_shape(l, r)
    shape_cache[n] = idx
    return idx

def get_value_maybe(sh, idx):
    seq = seqs[sh]
    while len(seq.values) <= idx:
        nv = next_value(sh)
        if nv is None: return None
        seq.values.append(nv)
    return seq.values[idx]

def ensure_right_ge(right_sh, x):
    rseq = seqs[right_sh]
    if rseq.exhausted and (not rseq.values or rseq.values[-1] < x): return -1
    
    while not rseq.values or rseq.values[-1] < x:
        nv = next_value(right_sh)
        if nv is None:
            rseq.exhausted = True
            break
        rseq.values.append(nv)
        
    if not rseq.values or rseq.values[-1] < x: return -1
    return bisect.bisect_left(rseq.values, x)

def push_pair(sh, i, j):
    seq = seqs[sh]
    key = (i << 32) | j
    if key in seq.in_heap: return
    
    x = get_value_maybe(seq.left, i)
    y = get_value_maybe(seq.right, j)
    if x is None or y is None: return
    if x > y: return
    
    prod = x * y
    if prod > MAXVAL: return
    
    seq.in_heap.add(key)
    heapq.heappush(seq.heap, (prod, i, j))

def start_node(sh):
    seq = seqs[sh]
    if seq.started: return
    seq.started = True
    
    x0 = get_value_maybe(seq.left, 0)
    if x0 is None:
        seq.exhausted = True
        return
    j0 = ensure_right_ge(seq.right, x0)
    if j0 != -1:
        push_pair(sh, 0, j0)
    seq.next_i = 1

def maybe_add_more_i(sh, current_min):
    seq = seqs[sh]
    while True:
        x = get_value_maybe(seq.left, seq.next_i)
        if x is None: return
        
        if seq.heap and x * x > current_min:
            return
            
        j0 = ensure_right_ge(seq.right, x)
        if j0 != -1:
            push_pair(sh, seq.next_i, j0)
        seq.next_i += 1

def next_candidate_product(sh):
    seq = seqs[sh]
    start_node(sh)
    if seq.exhausted: return None
    
    while True:
        if not seq.heap:
            x = get_value_maybe(seq.left, seq.next_i)
            if x is None:
                seq.exhausted = True
                return None
            j0 = ensure_right_ge(seq.right, x)
            if j0 == -1:
                seq.exhausted = True
                return None
            push_pair(sh, seq.next_i, j0)
            seq.next_i += 1
            continue
            
        prod, i, j = heapq.heappop(seq.heap)
        key = (i << 32) | j
        seq.in_heap.remove(key)
        
        maybe_add_more_i(sh, prod)
        push_pair(sh, i, j + 1)
        
        return prod

def next_value(sh):
    seq = seqs[sh]
    if seq.exhausted: return None
    
    if seq.leaf:
        if seq.next_prime == 2:
            seq.next_prime = 3
            return 2
        p = seq.next_prime
        while p <= MAXVAL:
            if is_prime64(p):
                seq.next_prime = p + 2
                return p
            p += 2
        seq.exhausted = True
        return None
        
    while True:
        cand = next_candidate_product(sh)
        if cand is None:
            seq.exhausted = True
            return None
        if seq.values and cand == seq.values[-1]:
            continue
        if shape_of(cand) == sh:
            return cand

def get_value(sh, idx):
    v = get_value_maybe(sh, idx)
    if v is None: raise RuntimeError("sequence exhausted")
    return v

def double_factorial(n):
    r = 1
    for k in range(n, 1, -2):
        r *= k
    return r

def solve():
    global MAXVAL, seqs
    
    max_n = 31
    MAXVAL = double_factorial(max_n)
    
    targets = []
    for n in range(2, max_n + 1):
        targets.append(shape_of(double_factorial(n)))
        
    needed = [False] * len(shapes)
    def collect(sh):
        if needed[sh]: return
        needed[sh] = True
        if sh == 0: return
        collect(shapes[sh]['left'])
        collect(shapes[sh]['right'])
        
    for sh in targets:
        collect(sh)
        
    seqs = [Sequence() for _ in range(len(shapes))]
    for sh in range(len(shapes)):
        if not needed[sh]: continue
        seqs[sh].needed = True
        seqs[sh].leaf = (sh == 0)
        if sh != 0:
            seqs[sh].left = shapes[sh]['left']
            seqs[sh].right = shapes[sh]['right']
            
    M = [0] * (max_n + 1)
    for n in range(2, max_n + 1):
        M[n] = get_value(targets[n - 2], 0)
        
    ans = sum(M[2:])
    return str(ans)

if __name__ == "__main__":
    print(solve())
