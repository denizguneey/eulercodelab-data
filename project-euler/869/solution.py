import math

def solve():
    limit = 100000000

    class Node:
        __slots__ = ['child', 'cnt', 'term']
        def __init__(self):
            self.child = [-1, -1]; self.cnt = 0; self.term = 0

    nodes = [Node()]

    def insert(p):
        u = 0; nodes[u].cnt += 1
        l = p.bit_length()
        for d in range(l):
            b = (p >> d) & 1
            v = nodes[u].child[b]
            if v == -1:
                v = len(nodes); nodes[u].child[b] = v; nodes.append(Node())
            u = v; nodes[u].cnt += 1
        nodes[u].term = 1

    # Sieve and insert primes
    if limit >= 2: insert(2)
    m = (limit >> 1) + 1
    is_prime = bytearray(b'\x01' * m); is_prime[0] = 0
    r = int(math.isqrt(limit))
    for p in range(3, r+1, 2):
        if not is_prime[p >> 1]: continue
        for x in range(p*p, limit+1, 2*p): is_prime[x >> 1] = 0
    for p in range(3, limit+1, 2):
        if is_prime[p >> 1]: insert(p)

    def dfs(u):
        cur = nodes[u]
        cont = cur.cnt - cur.term
        if cont == 0: return 0.0
        c0 = c1 = n0 = n1 = 0; v0 = v1 = 0.0
        ch0 = cur.child[0]
        if ch0 != -1:
            c0 = nodes[ch0].cnt; n0 = c0 - nodes[ch0].term
            if n0 > 0: v0 = dfs(ch0)
        ch1 = cur.child[1]
        if ch1 != -1:
            c1 = nodes[ch1].cnt; n1 = c1 - nodes[ch1].term
            if n1 > 0: v1 = dfs(ch1)
        d = cont
        return max(c0, c1) / d + n0 / d * v0 + n1 / d * v1

    return f'{dfs(0):.8f}'

if __name__ == '__main__':
    print(solve())
