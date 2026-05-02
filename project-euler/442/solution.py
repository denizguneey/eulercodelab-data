# Native Python 442
def solve():
    n_target = 1000000000000000000

    def mul_by_11(s):
        out = []
        carry = 0
        for ch in reversed(s):
            v = 11 * int(ch) + carry
            out.append(str(v % 10))
            carry = v // 10
        while carry > 0:
            out.append(str(carry % 10))
            carry //= 10
        out.reverse()
        # lstrip '0' but leave one if all '0'
        res = "".join(out).lstrip('0')
        return res if res else "0"

    max_digits = 64
    patterns = []
    cur = "11"
    while len(cur) <= max_digits:
        patterns.append(cur)
        cur = mul_by_11(cur)

    # Build Aho-Corasick
    class Node:
        def __init__(self):
            self.next = [-1] * 10
            self.fail = 0
            self.out = False

    nodes = [Node()]
    for p in patterns:
        state = 0
        for ch in p:
            d = int(ch)
            nx = nodes[state].next[d]
            if nx == -1:
                nx = len(nodes)
                nodes[state].next[d] = nx
                nodes.append(Node())
            state = nx
        nodes[state].out = True

    from collections import deque
    q = deque()
    for d in range(10):
        nx = nodes[0].next[d]
        if nx == -1:
            nodes[0].next[d] = 0
        else:
            nodes[nx].fail = 0
            q.append(nx)

    while q:
        v = q.popleft()
        f = nodes[v].fail
        if nodes[f].out:
            nodes[v].out = True
        for d in range(10):
            nx = nodes[v].next[d]
            if nx == -1:
                nodes[v].next[d] = nodes[f].next[d]
            else:
                nodes[nx].fail = nodes[f].next[d]
                q.append(nx)

    states = len(nodes)
    cap = n_target + 1

    ways = [[0] * states for _ in range(max_digits + 1)]
    for s in range(states):
        ways[0][s] = 1

    for rem in range(1, max_digits + 1):
        for s in range(states):
            if nodes[s].out:
                continue
            summ = 0
            for d in range(10):
                ns = nodes[s].next[d]
                if not nodes[ns].out:
                    summ += ways[rem - 1][ns]
            ways[rem][s] = min(summ, cap)

    remaining = n_target
    length = 0
    for L in range(1, max_digits + 1):
        cnt = 0
        for d in range(1, 10):
            ns = nodes[0].next[d]
            if not nodes[ns].out:
                cnt += ways[L - 1][ns]
        if remaining > cnt:
            remaining -= cnt
        else:
            length = L
            break

    if length == 0:
        return ""

    ans = []
    state = 0
    for pos in range(length):
        start_digit = 1 if pos == 0 else 0
        for d in range(start_digit, 10):
            ns = nodes[state].next[d]
            if nodes[ns].out:
                continue
            cnt = ways[length - pos - 1][ns]
            if remaining > cnt:
                remaining -= cnt
            else:
                ans.append(str(d))
                state = ns
                break

    return "".join(ans)

if __name__ == '__main__':
    print(solve())
