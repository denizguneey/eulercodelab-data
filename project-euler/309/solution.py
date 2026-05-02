import math

def solve():
    limit = 1000000
    lmt = limit - 1

    by_width = [[] for _ in range(lmt + 1)]
    root = int(math.sqrt(lmt)) + 2

    for i in range(root + 1):
        for j in range(1, i):
            if math.gcd(i, j) != 1:
                continue
            a = i*i - j*j
            b = 2*i*j
            c = i*i + j*j
            if a > b:
                a, b = b, a
            scale = 1
            while scale * c <= lmt:
                by_width[a * scale].append((b * scale, c * scale))
                by_width[b * scale].append((a * scale, c * scale))
                scale += 1

    uniq = set()
    for w in range(1, lmt + 1):
        vec = by_width[w]
        if not vec:
            continue
        vec.sort()
        for pi in range(len(vec)):
            for qi in range(len(vec)):
                if vec[pi][0] == vec[qi][0]:
                    break
                h1 = vec[pi][0]
                h2 = vec[qi][0]
                if (h1 * h2) % (h1 + h2) == 0:
                    uniq.add((h1, h2, w))

    return str(len(uniq))

if __name__ == '__main__':
    print(solve())
