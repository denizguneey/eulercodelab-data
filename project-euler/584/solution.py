import math
from itertools import product

def solve():
    N = 365; k = 4; D = 7; W = D+1; L = W-1
    n_max = (k-1)*N//W

    inv_fact = [1.0]*k
    f = 1.0
    for i in range(1, k):
        f *= i; inv_fact[i] = 1.0/f

    # Build states: tuples of L non-negative ints summing to <= k-1
    states = []; state_id = {}
    def gen(pos, rem, cur):
        if pos == L:
            s = tuple(cur); state_id[s] = len(states); states.append(s)
            return
        for v in range(rem+1):
            cur.append(v); gen(pos+1, rem-v, cur); cur.pop()
    if L == 0:
        states.append(()); state_id[()] = 0
    else:
        gen(0, k-1, [])

    S = len(states)
    # Build transitions
    transitions = [[] for _ in range(S)]
    for i, st in enumerate(states):
        sm = sum(st)
        for c in range(k-1-sm+1):
            nxt = st[1:] + (c,) if L > 0 else ()
            transitions[i].append((state_id[nxt], c, inv_fact[c]))

    # DP: for each starting state, run N days
    totals = [0.0]*(n_max+1)
    for s0 in range(S):
        dp = [[0.0]*(n_max+1) for _ in range(S)]
        dp[s0][0] = 1.0
        for day in range(N):
            nxt = [[0.0]*(n_max+1) for _ in range(S)]
            for u in range(S):
                row = dp[u]
                for ns, add, w in transitions[u]:
                    dest = nxt[ns]; lim = n_max - add
                    for n in range(lim+1):
                        v = row[n]
                        if v != 0.0: dest[n+add] += v*w
            dp = nxt
        row = dp[s0]
        for n in range(n_max+1): totals[n] += row[n]

    expected = 0.0; fact = 1.0; invN = 1.0/N; invNpow = 1.0
    for n in range(n_max+1):
        if n > 0: fact *= n; invNpow *= invN
        expected += totals[n] * fact * invNpow
    return f"{expected:.8f}"

if __name__ == '__main__':
    print(solve())
