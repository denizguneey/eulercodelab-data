def clmul(x, y):
    r = 0
    while y > 0:
        if y & 1:
            r ^= x
        x <<= 1
        y >>= 1
    return r

def value_f(a, b):
    return clmul(a, a) ^ clmul(clmul(2, a), b) ^ clmul(b, b)

def seed_bound(m):
    if m == 0:
        return 1
    bits = 0
    t = m
    while t > 0:
        bits += 1
        t >>= 1
    return 1 << ((bits + 2) // 2)

def count_fast(n, m):
    if m == 0:
        return 1

    bmax = seed_bound(m)
    total = 0

    for b in range(bmax):
        for a in range(b + 1):
            k = value_f(a, b)
            if k > m:
                continue

            if a == 0 and b == 0:
                total += 1
                continue

            prev = b ^ (a << 1)
            if prev <= a:
                continue

            aa = a
            bb = b
            while bb <= n:
                total += 1
                next_val = (bb << 1) ^ aa
                aa = bb
                bb = next_val

    return total

def solve():
    return str(count_fast(100000000000000000, 1000000))

if __name__ == "__main__":
    print(solve())
