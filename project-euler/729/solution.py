import math
import multiprocessing

class KahanSum:
    def __init__(self):
        self.sum = 0.0
        self.c = 0.0

    def add(self, x):
        y = x - self.c
        t = self.sum + y
        self.c = (t - self.sum) - y
        self.sum = t

def apply_inverse_word(y, bits, m):
    for i in range(m):
        d = math.sqrt(y * y + 4.0)
        if (bits >> i) & 1:
            y = 0.5 * (y + d)
        else:
            y = 0.5 * (y - d)
    return y

def solve_fixed_point(bits, m):
    y = 0.0
    for it in range(80):
        ny = apply_inverse_word(y, bits, m)
        if abs(ny - y) < 1e-15:
            return ny
        y = ny
        
    for it in range(16):
        v = y
        deriv = 1.0
        for i in range(m):
            d = math.sqrt(v * v + 4.0)
            s = 1 if (bits >> i) & 1 else -1
            deriv *= 0.5 * (1.0 + s * (v / d))
            v = 0.5 * (v + s * d)
            
        phi = v - y
        dphi = deriv - 1.0
        if abs(dphi) < 1e-15:
            break
            
        step = phi / dphi
        y -= step
        if abs(step) < 1e-15:
            break
            
    return y

def orbit_range_from_inverse_word(x0, bits, m):
    mn = x0
    mx = x0
    y = x0
    
    for i in range(m - 1):
        d = math.sqrt(y * y + 4.0)
        if (bits >> i) & 1:
            y = 0.5 * (y + d)
        else:
            y = 0.5 * (y - d)
        if y < mn: mn = y
        if y > mx: mx = y
        
    return mx - mn

def mobius(n):
    x = n
    prime_count = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            exp = 0
            while x % p == 0:
                x //= p
                exp += 1
            if exp > 1: return 0
            prime_count += 1
        p += 1
    if x > 1:
        prime_count += 1
    return 1 if prime_count % 2 == 0 else -1

def expected_primitive_necklaces(n):
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            mu = mobius(d)
            if mu == 0: continue
            total += mu * (1 << (n // d))
    return total // n

def generate_primitive_necklaces(n):
    out = []
    a = [0] * (n + 1)
    
    def gen(t, p):
        if t > n:
            if n % p == 0 and p == n:
                bits = 0
                for i in range(1, n + 1):
                    bits |= (a[i] << (i - 1))
                out.append(bits)
            return
            
        a[t] = a[t - p]
        gen(t + 1, p)
        
        for j in range(a[t - p] + 1, 2):
            a[t] = j
            gen(t + 1, t)
            
    gen(1, 1)
    return out

def worker(m, necklaces):
    total = KahanSum()
    for bits in necklaces:
        x0 = solve_fixed_point(bits, m)
        r = orbit_range_from_inverse_word(x0, bits, m)
        total.add(m * r)
    return total.sum

def solve():
    p = 25
    total = KahanSum()
    
    threads = max(1, multiprocessing.cpu_count())
    pool = multiprocessing.Pool(threads)
    
    for m in range(2, p + 1):
        necklaces = generate_primitive_necklaces(m)
        
        chunk_size = max(1, len(necklaces) // threads)
        chunks = [necklaces[i:i + chunk_size] for i in range(0, len(necklaces), chunk_size)]
        
        results = pool.starmap(worker, [(m, chunk) for chunk in chunks])
        for val in results:
            total.add(val)
            
    pool.close()
    
    return f"{total.sum:.10f}"

if __name__ == "__main__":
    print(solve())
