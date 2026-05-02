# Problem 186: Connectedness of a network.
# Union-Find with Lagged Fibonacci generator.

def solve():
    subscribers = 1000000
    pm = 524287
    threshold = 99  # percent

    # Lagged Fibonacci
    s = [0]*(56)
    for k in range(1, 56):
        s[k] = (100003 - 200003*k + 300007*k*k*k) % 1000000
    buf = s[1:]
    idx = 0
    def next_val():
        nonlocal idx, buf
        if idx < 55:
            v = buf[idx]
        else:
            buf.append((buf[-24] + buf[-55]) % 1000000)
            v = buf[idx]
        idx += 1
        return v

    # Union-Find
    parent = list(range(subscribers))
    size = [1]*subscribers
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def unite(a, b):
        a, b = find(a), find(b)
        if a == b: return
        if size[a] < size[b]: a, b = b, a
        parent[b] = a
        size[a] += size[b]

    target_size = subscribers * threshold // 100
    successful = 0
    while size[find(pm)] < target_size:
        caller = next_val()
        called = next_val()
        if caller == called: continue
        successful += 1
        unite(caller, called)
    print(successful)

solve()
