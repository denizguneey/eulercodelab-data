def sum_prefix(bit, idx):
    s = 0
    idx += 1
    while idx > 0:
        s += bit[idx]
        idx -= idx & -idx
    return s

def add(bit, idx, delta):
    idx += 1
    while idx < len(bit):
        bit[idx] += delta
        idx += idx & -idx

def first_sort_steps_fast(perm):
    n = len(perm)
    if n <= 1: return 0
    pos = [0] * (n + 1)
    for i in range(n): 
        pos[perm[i]] = i
    
    insertion_pos = [0] * (n + 1)
    bit = [0] * (n + 1)
    add(bit, pos[1], 1)
    
    for v in range(2, n + 1):
        insertion_pos[v] = sum_prefix(bit, pos[v]) + 1
        add(bit, pos[v], 1)
        
    steps = 0
    B = 1
    for m in range(1, n):
        p = insertion_pos[m + 1]
        low_mask = 0 if p == 1 else (1 << (p - 1)) - 1
        suffix = B & ~low_mask
        steps += suffix
        B = (B & low_mask) | (1 << (p - 1))
    return steps

def lex_index_1based_big(perm):
    n = len(perm)
    fact = [1] * (n + 1)
    for i in range(2, n + 1): 
        fact[i] = fact[i - 1] * i
    
    rem = list(range(1, n + 1))
    rank = 1
    import bisect
    for i in range(n):
        it = bisect.bisect_left(rem, perm[i])
        rank += it * fact[n - 1 - i]
        rem.pop(it)
    return rank

def solve():
    best = [
        1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 25, 27, 28, 30, 32,
        34, 36, 38, 40, 39, 42, 45, 43, 41, 37, 35, 33, 31, 29, 44
    ]
    if first_sort_steps_fast(best) != 8916100448256:
        raise ValueError("Validation Failed")
    
    return str(lex_index_1based_big(best))

if __name__ == '__main__':
    print(solve())
