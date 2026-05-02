import bisect
import sys

# Increase recursion depth just in case, though max depth is 40.
sys.setrecursionlimit(2000)

def make_next(s, remove_len, add1, add2=0):
    t = list(s)
    t.remove(remove_len) # we know it's there
    if add1 > 0:
        bisect.insort(t, add1)
    if add2 > 0:
        bisect.insort(t, add2)
    return tuple(t)

trans_memo = {}

def get_transitions(s):
    if s in trans_memo:
        return trans_memo[s]
        
    acc = {}
    blocks = len(s)
    i = 0
    while i < blocks:
        j = i
        while j < blocks and s[j] == s[i]:
            j += 1
        cnt = j - i
        length = s[i]
        
        if length == 1:
            t = make_next(s, 1, 0, 0)
            acc[t] = acc.get(t, 0) + cnt
        else:
            endpoint = make_next(s, length, length - 1, 0)
            acc[endpoint] = acc.get(endpoint, 0) + 2 * cnt
            for a in range(1, length - 1):
                b = length - 1 - a
                split = make_next(s, length, a, b)
                acc[split] = acc.get(split, 0) + cnt
        i = j
        
    out = list(acc.items())
    trans_memo[s] = out
    return out

expected_memo = {}

def expected_max(s, current_max):
    if not s:
        return float(current_max)
        
    state_key = (s, current_max)
    if state_key in expected_memo:
        return expected_memo[state_key]
        
    remaining = sum(s)
    tr = get_transitions(s)
    
    ans = 0.0
    for ns, w in tr:
        next_max = max(current_max, len(ns))
        ans += (w / float(remaining)) * expected_max(ns, next_max)
        
    expected_memo[state_key] = ans
    return ans

def solve():
    ans = expected_max((40,), 1)
    return "{:.6f}".format(ans)

if __name__ == '__main__':
    print(solve())
