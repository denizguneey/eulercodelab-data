kMod = 1000000007
inv2 = (kMod + 1) // 2

def mod_add(a, b):
    s = a + b
    if s >= kMod:
        s -= kMod
    return s

def mod_mul(a, b):
    return (a * b) % kMod

def range_sum_mod(start, length):
    if length == 0:
        return 0
    t1 = length % kMod
    t2 = (2 * (start % kMod) + (length - 1) % kMod) % kMod
    return mod_mul(mod_mul(t1, t2), inv2)

def full_block_sum(a, b, c, size):
    s = 0
    s = mod_add(s, range_sum_mod(a, size))
    s = mod_add(s, range_sum_mod(b, size))
    s = mod_add(s, range_sum_mod(c, size))
    return s

def partial_block_sum(length, a, b, c, size):
    if length == 0:
        return 0
    if length == size:
        return full_block_sum(a, b, c, size)
    if size == 1:
        return (a + b + c) % kMod
        
    s = size // 4
    ans = 0
    
    l1 = min(length, s)
    ans = mod_add(ans, partial_block_sum(l1, a, b, c, s))
    
    rem = length - s if length > s else 0
    l2 = min(rem, s)
    ans = mod_add(ans, partial_block_sum(l2, a + s, b + 2 * s, c + 3 * s, s))
    
    rem = length - 2 * s if length > 2 * s else 0
    l3 = min(rem, s)
    ans = mod_add(ans, partial_block_sum(l3, a + 2 * s, b + 3 * s, c + s, s))
    
    rem = length - 3 * s if length > 3 * s else 0
    l4 = min(rem, s)
    ans = mod_add(ans, partial_block_sum(l4, a + 3 * s, b + s, c + 2 * s, s))
    
    return ans

def M_fast(n):
    if n == 0:
        return 0
        
    a, b, c = 1, 2, 3
    size = 1
    left = n
    ans = 0
    
    while left > size:
        ans = mod_add(ans, full_block_sum(a, b, c, size))
        left -= size
        a *= 4
        b *= 4
        c *= 4
        size *= 4
        
    ans = mod_add(ans, partial_block_sum(left, a, b, c, size))
    return ans

def solve():
    return str(M_fast(1000000000000000000))

if __name__ == "__main__":
    print(solve())
