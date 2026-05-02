MOD = 100000007
CELLS = 9
FULL_MASK = (1 << CELLS) - 1
STATE_COUNT = 1 << CELLS

def add_mod(a, b):
    return (a + b) % MOD

def sub_mod(a, b):
    return (a - b) % MOD

def mul_mod(a, b):
    return (a * b) % MOD

def pow_mod(base, exp):
    return pow(base, exp, MOD)

def inv_mod(a):
    return pow_mod(a, MOD - 2)

def dfs_layer_fill(filled_mask, next_mask, ways):
    if filled_mask == FULL_MASK:
        ways[next_mask] += 1
        return
        
    free_bits = (~filled_mask) & FULL_MASK
    bit = (free_bits & -free_bits).bit_length() - 1
    
    dfs_layer_fill(filled_mask | (1 << bit), next_mask | (1 << bit), ways)
    
    r = bit // 3
    c = bit % 3
    
    if c < 2 and (filled_mask & (1 << (bit + 1))) == 0:
        dfs_layer_fill(filled_mask | (1 << bit) | (1 << (bit + 1)), next_mask, ways)
        
    if r < 2 and (filled_mask & (1 << (bit + 3))) == 0:
        dfs_layer_fill(filled_mask | (1 << bit) | (1 << (bit + 3)), next_mask, ways)

def build_transitions():
    transitions = [[] for _ in range(STATE_COUNT)]
    for mask in range(STATE_COUNT):
        ways = [0] * STATE_COUNT
        dfs_layer_fill(mask, 0, ways)
        for nxt in range(STATE_COUNT):
            if ways[nxt] > 0:
                transitions[mask].append((nxt, ways[nxt] % MOD))
    return transitions

def generate_sequence(terms, transitions):
    seq = [0] * (terms + 1)
    current = [0] * STATE_COUNT
    current[0] = 1
    seq[0] = 1
    
    for step in range(1, terms + 1):
        nxt = [0] * STATE_COUNT
        for mask in range(STATE_COUNT):
            if current[mask] == 0:
                continue
            val = current[mask]
            for nx, cnt in transitions[mask]:
                nxt[nx] = (nxt[nx] + val * cnt) % MOD
        current = nxt
        seq[step] = current[0]
        
    return seq

def berlekamp_massey(sequence):
    C = [1]
    B = [1]
    L = 0
    m = 1
    b = 1
    
    for n in range(len(sequence)):
        d = sequence[n]
        for i in range(1, L + 1):
            d = (d + C[i] * sequence[n - i]) % MOD
            
        if d == 0:
            m += 1
            continue
            
        T = list(C)
        coef = (d * inv_mod(b)) % MOD
        
        if len(C) < len(B) + m:
            C.extend([0] * (len(B) + m - len(C)))
            
        for i in range(len(B)):
            C[i + m] = (C[i + m] - coef * B[i]) % MOD
            
        if 2 * L <= n:
            L = n + 1 - L
            B = T
            b = d
            m = 1
        else:
            m += 1
            
    recurrence = [0] * L
    for i in range(1, L + 1):
        recurrence[i - 1] = (MOD - C[i]) % MOD
    return recurrence

def combine_polynomials(a, b, recurrence):
    k = len(recurrence)
    prod = [0] * (2 * k)
    
    for i in range(k):
        if a[i] == 0:
            continue
        for j in range(k):
            if b[j] == 0:
                continue
            prod[i + j] = (prod[i + j] + a[i] * b[j]) % MOD
            
    for i in range(2 * k - 2, k - 1, -1):
        coef = prod[i]
        if coef == 0:
            continue
        for j in range(1, k + 1):
            prod[i - j] = (prod[i - j] + coef * recurrence[j - 1]) % MOD
            
    return prod[:k]

def linear_recurrence_nth(initial, recurrence, bits_lsb_first):
    k = len(recurrence)
    result = [0] * k
    result[0] = 1
    
    x_poly = [0] * k
    if k == 1:
        x_poly[0] = recurrence[0]
    else:
        x_poly[1] = 1
        
    for bit in bits_lsb_first:
        if bit != 0:
            result = combine_polynomials(result, x_poly, recurrence)
        x_poly = combine_polynomials(x_poly, x_poly, recurrence)
        
    ans = 0
    for i in range(k):
        ans = (ans + result[i] * initial[i]) % MOD
    return ans

def bits_from_decimal(value_str):
    value_int = int(value_str)
    if value_int == 0:
        return [0]
    bits = []
    while value_int > 0:
        bits.append(value_int & 1)
        value_int >>= 1
    return bits

def solve():
    transitions = build_transitions()
    seq = generate_sequence(1300, transitions)
    recurrence = berlekamp_massey(seq)
    
    initial = seq[:len(recurrence)]
    
    exponent = "1" + "0" * 10000
    bits = bits_from_decimal(exponent)
    ans = linear_recurrence_nth(initial, recurrence, bits)
    return str(ans)

if __name__ == '__main__':
    import sys
    sys.set_int_max_str_digits(20000)
    print(solve())
