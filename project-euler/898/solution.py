import math
from collections import defaultdict
import bisect

def collect_primes_for_pairs():
    primes = set()
    
    def add_factor(x):
        t = x
        for p in range(2, int(math.sqrt(t)) + 1):
            if t % p != 0:
                continue
            primes.add(p)
            while t % p == 0:
                t //= p
        if t > 1:
            primes.add(t)

    for k in range(25, 50):
        add_factor(k)
        add_factor(100 - k)
        
    return sorted(list(primes))

def exponent_vector(num, den, primes):
    e = [0] * len(primes)
    a = num
    b = den
    for i, p in enumerate(primes):
        cn = 0
        cd = 0
        while a % p == 0:
            a //= p
            cn += 1
        while b % p == 0:
            b //= p
            cd += 1
        e[i] = 2 * (cn - cd)
    return tuple(e)

def build_pairs(primes):
    pairs = []
    for k in range(25, 50):
        q = k / 100.0
        w = 2.0 * math.log((1.0 - q) / q)
        
        p_pos = (1.0 - q) * (1.0 - q)
        p_zero = 2.0 * q * (1.0 - q)
        p_neg = q * q
        exp = exponent_vector(100 - k, k, primes)
        pairs.append({
            'weight': w,
            'p_pos': p_pos,
            'p_zero': p_zero,
            'p_neg': p_neg,
            'exp': exp
        })
    return pairs

def enumerate_states(pairs, begin, end):
    states = [{'score': 0.0, 'prob': 1.0, 'exp': tuple([0]*len(pairs[0]['exp']))}]
    
    for i in range(begin, end):
        pair = pairs[i]
        next_states = []
        
        for st in states:
            next_states.append({
                'score': st['score'] + pair['weight'],
                'prob': st['prob'] * pair['p_pos'],
                'exp': tuple(st['exp'][j] + pair['exp'][j] for j in range(len(st['exp'])))
            })
            next_states.append({
                'score': st['score'],
                'prob': st['prob'] * pair['p_zero'],
                'exp': st['exp']
            })
            next_states.append({
                'score': st['score'] - pair['weight'],
                'prob': st['prob'] * pair['p_neg'],
                'exp': tuple(st['exp'][j] - pair['exp'][j] for j in range(len(st['exp'])))
            })
        states = next_states
    return states

def compare_exact_product(a, b, primes):
    c = [a[i] + b[i] for i in range(len(primes))]
    if all(x == 0 for x in c):
        return 0
        
    num = 1
    den = 1
    
    for i, e in enumerate(c):
        if e > 0:
            num *= (primes[i] ** e)
        elif e < 0:
            den *= (primes[i] ** (-e))
            
    if num > den:
        return 1
    if num < den:
        return -1
    return 0

def solve_pairs(pairs, primes):
    split = len(pairs) // 2
    left = enumerate_states(pairs, 0, split)
    right = enumerate_states(pairs, split, len(pairs))
    
    right.sort(key=lambda st: st['score'])
    
    right_scores = [st['score'] for st in right]
    right_prefix = [0.0] * (len(right) + 1)
    for i in range(len(right)):
        right_prefix[i + 1] = right_prefix[i] + right[i]['prob']
        
    total_right = right_prefix[-1]
    
    eps = 1e-12
    answer = 0.0
    
    for ls in left:
        threshold = -ls['score']
        
        lo = bisect.bisect_left(right_scores, threshold - eps)
        hi = bisect.bisect_right(right_scores, threshold + eps)
        
        p_correct = total_right - right_prefix[hi]
        
        for i in range(lo, hi):
            cmp = compare_exact_product(ls['exp'], right[i]['exp'], primes)
            if cmp > 0:
                p_correct += right[i]['prob']
            elif cmp == 0:
                p_correct += 0.5 * right[i]['prob']
                
        answer += ls['prob'] * p_correct
        
    return answer

def solve():
    primes = collect_primes_for_pairs()
    pairs = build_pairs(primes)
    ans = solve_pairs(pairs, primes)
    return f"{ans:.10f}"

if __name__ == "__main__":
    print(solve())
