def solve():
    ALPHA = 4
    
    def char_id(ch):
        if ch == 'A': return 0
        if ch == 'E': return 1
        if ch == 'F': return 2
        return 3

    class Node:
        def __init__(self):
            self.next = [-1] * ALPHA
            self.link = 0
            self.out = [0] * 4

    nodes = [Node()]

    def add_pattern(s, pid):
        v = 0
        for ch in s:
            c = char_id(ch)
            if nodes[v].next[c] == -1:
                nodes[v].next[c] = len(nodes)
                nodes.append(Node())
            v = nodes[v].next[c]
        nodes[v].out[pid] += 1

    add_pattern("FREE", 0)
    add_pattern("FARE", 1)
    add_pattern("AREA", 2)
    add_pattern("REEF", 3)

    q = []
    for c in range(ALPHA):
        to = nodes[0].next[c]
        if to == -1:
            nodes[0].next[c] = 0
        else:
            nodes[to].link = 0
            q.append(to)

    while q:
        v = q.pop(0)
        lk = nodes[v].link
        for k in range(4):
            nodes[v].out[k] += nodes[lk].out[k]

        for c in range(ALPHA):
            to = nodes[v].next[c]
            if to == -1:
                nodes[v].next[c] = nodes[lk].next[c]
            else:
                nodes[to].link = nodes[lk].next[c]
                q.append(to)

    states = len(nodes)
    CNT = 81

    def encode_counts(a, b, c, d):
        return ((a * 3 + b) * 3 + c) * 3 + d

    dp = [0] * (states * CNT)
    dp[0] = 1

    for pos in range(30):
        nxt = [0] * (states * CNT)
        for st in range(states):
            for code in range(CNT):
                ways = dp[st * CNT + code]
                if ways == 0:
                    continue

                t = code
                c3 = t % 3
                t //= 3
                c2 = t % 3
                t //= 3
                c1 = t % 3
                t //= 3
                c0 = t

                for ch in range(ALPHA):
                    ns = nodes[st].next[ch]
                    add = nodes[ns].out

                    n0 = 2 if c0 + add[0] >= 2 else c0 + add[0]
                    n1 = 2 if c1 + add[1] >= 2 else c1 + add[1]
                    n2 = 2 if c2 + add[2] >= 2 else c2 + add[2]
                    n3 = 2 if c3 + add[3] >= 2 else c3 + add[3]

                    if n0 == 2 or n1 == 2 or n2 == 2 or n3 == 2:
                        continue

                    ncode = encode_counts(n0, n1, n2, n3)
                    nxt[ns * CNT + ncode] += ways
        dp = nxt

    target = encode_counts(1, 1, 1, 1)
    ans = 0
    for st in range(states):
        ans += dp[st * CNT + target]

    return str(ans)

if __name__ == '__main__':
    print(solve())
