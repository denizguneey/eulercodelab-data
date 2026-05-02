import sys

MOD = 912491249

def mod_add(a, b):
    return (a + b) % MOD

def compute_grundy(max_n):
    g = [0] * (max_n + 1)
    max_g = 0
    moves = [1, 2, 4, 9]

    for n in range(1, max_n + 1):
        mask = 0
        for mv in moves:
            if n >= mv:
                mask |= (1 << g[n - mv])
        
        half = n // 2
        for a in range(1, half + 1):
            mask |= (1 << (g[a] ^ g[n - a]))
            
        mex = 0
        while mask & (1 << mex):
            mex += 1
            
        g[n] = mex
        if mex > max_g:
            max_g = mex
            
    return g, max_g

def detect_period(seq, max_period=300, min_reps=6):
    n = len(seq)
    for p in range(1, max_period + 1):
        L = p * min_reps
        if L + p > n:
            continue
        start_tail = n - L
        
        ok = True
        for i in range(start_tail, n - p):
            if seq[i] != seq[i + p]:
                ok = False
                break
        if not ok:
            continue
            
        for s in range(0, n - p):
            good = True
            for i in range(s, n - p):
                if seq[i] != seq[i + p]:
                    good = False
                    break
            if good:
                return {'period': p, 'start': s, 'seq': seq}
    return None

def build_grundy_data(max_n):
    g, max_g = compute_grundy(max_n)
    even = [g[2 * k] for k in range(1, max_n // 2 + 1)]
    odd = [g[2 * k - 1] for k in range(1, (max_n + 1) // 2 + 1)]

    even_info = detect_period(even)
    odd_info = detect_period(odd)
    
    return {'g': g, 'max_g': max_g, 'even': even_info, 'odd': odd_info}

def add_counts(info, total, counts):
    if total <= 0:
        return
    seq = info['seq']
    start = info['start']
    period = info['period']

    if total <= start:
        for i in range(total):
            counts[seq[i]] += 1
        return

    for i in range(start):
        counts[seq[i]] += 1

    rem = total - start
    freq = [0] * len(counts)
    for i in range(period):
        freq[seq[start + i]] += 1
        
    cycles = rem // period
    tail = rem % period
    
    for gidx in range(len(counts)):
        counts[gidx] += freq[gidx] * cycles
        
    for i in range(tail):
        counts[seq[start + i]] += 1

def grundy_counts(N, data):
    counts = [0] * (data['max_g'] + 1)
    total_even = N // 2
    total_odd = (N + 1) // 2
    
    add_counts(data['even'], total_even, counts)
    add_counts(data['odd'], total_odd, counts)
    return counts

def build_comb(c, m):
    comb = [0] * (m + 1)
    val = 1
    comb[0] = 1
    for k in range(1, m + 1):
        val = (val * (c + k - 1)) // k
        comb[k] = val % MOD
    return comb

def compute_S(N, m, data):
    counts = grundy_counts(N, data)
    
    max_g = data['max_g']
    bits = 0
    while (1 << bits) <= max_g:
        bits += 1
    states = 1 << bits

    dp = [[0] * (m + 1) for _ in range(states)]
    dp[0][0] = 1

    for gval in range(max_g + 1):
        c = counts[gval]
        if c == 0:
            continue

        comb = build_comb(c, m)
        even_terms = []
        odd_terms = []
        
        for k in range(m + 1):
            v = comb[k]
            if v == 0:
                continue
            if k & 1:
                odd_terms.append((k, v))
            else:
                even_terms.append((k, v))

        next_dp = [[0] * (m + 1) for _ in range(states)]
        
        for mask in range(states):
            cur = dp[mask]
            dest_same = next_dp[mask]
            dest_xor = next_dp[mask ^ gval]
            
            for i in range(m + 1):
                curv = cur[i]
                if curv == 0:
                    continue
                    
                for j, v in even_terms:
                    if i + j > m:
                        break
                    dest_same[i + j] = (dest_same[i + j] + curv * v) % MOD
                    
                for j, v in odd_terms:
                    if i + j > m:
                        break
                    dest_xor[i + j] = (dest_xor[i + j] + curv * v) % MOD
                    
        dp = next_dp

    return dp[0][m]

def solve():
    max_n = 20000
    data = build_grundy_data(max_n)
    
    N = 12491249
    m = 1249
    return str(compute_S(N, m, data))

if __name__ == "__main__":
    print(solve())
