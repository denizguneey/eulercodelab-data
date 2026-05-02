import math

def solve():
    CYCLE = 43200; speeds = [1, 12, 720]
    from itertools import permutations

    def egcd(a, b):
        if b == 0: return a, 1, 0
        g, x1, y1 = egcd(b, a%b)
        return g, y1, x1-(a//b)*y1

    moments = set()
    for perm in permutations([0,1,2]):
        if list(perm) == [0,1,2]: continue
        pa, pb, pc = speeds[perm[0]], speeds[perm[1]], speeds[perm[2]]
        A = pb-pa; B = pc-pa; det = 719*A - 11*B
        if det == 0: continue
        D = abs(det)
        absA, absB = abs(A), abs(B)
        g, x, y = egcd(absB, absA)
        u = x*(1 if B>=0 else -1); v = y*(1 if A>=0 else -1)
        C = (11*v + 719*u) % D
        if C < 0: C += D
        g1 = math.gcd(CYCLE, D); nb = CYCLE//g1; db = D//g1
        for n in range(D):
            n2 = n*C%D
            if n2 == n: continue
            g2 = math.gcd(n, db)
            num = nb*(n//g2); den = db//g2
            moments.add((num, den))

    return str(len(moments))

if __name__ == '__main__':
    print(solve())
