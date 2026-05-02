import sys

# Increase recursion depth just in case (though it's iterative here)
sys.setrecursionlimit(2000)

def path_max(w, l, r):
    if l > r:
        return 0
    a = 0
    b = 0
    for i in range(l, r + 1):
        c = max(b, a + w[i])
        a = b
        b = c
    return b

def D_value(n):
    to = [0] * n
    indeg = [0] * n
    preds = [[] for _ in range(n)]

    for x in range(n):
        v = (pow(x, 3, n) + x + 1) % n
        to[x] = v
        indeg[v] += 1
        preds[v].append(x)

    q = [i for i in range(n) if indeg[i] == 0]
    
    order = []
    # iterative approach for q
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        order.append(u)

        v = to[u]
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

    dp0 = [0] * n
    dp1 = [0] * n

    for u in order:
        base = 0
        best = 0
        for c in preds[u]:
            if indeg[c] == 0:
                base += dp0[c]
                best = max(best, dp1[c] - dp0[c])
        dp0[u] = base + max(0, best)
        dp1[u] = base + 1

    vis = bytearray(n)
    ans = 0

    for s in range(n):
        if indeg[s] == 0 or vis[s]:
            continue

        cyc = []
        u = s
        while not vis[u]:
            vis[u] = 1
            cyc.append(u)
            u = to[u]

        k = len(cyc)
        base_arr = [0] * k
        gain = [0] * k

        for i in range(k):
            x = cyc[i]
            b = 0
            g = 0
            for c in preds[x]:
                if indeg[c] == 0:
                    b += dp0[c]
                    g = max(g, dp1[c] - dp0[c])
            base_arr[i] = b
            gain[i] = max(0, g)

        comp = sum(base_arr) + sum(gain)

        if k == 1:
            ans += comp
            continue

        w = [0] * k
        for i in range(k):
            j = 0 if i + 1 == k else i + 1
            w[i] = 1 - gain[i] - gain[j]

        bestA = path_max(w, 1, k - 1)
        bestB = w[0] + path_max(w, 2, k - 2)
        best = max(0, bestA, bestB)

        ans += comp + best

    return ans

def solve():
    sum_val = 0
    for i in range(1, 101):
        sum_val += D_value(100000 + i)
    return str(sum_val)

if __name__ == "__main__":
    print(solve())
