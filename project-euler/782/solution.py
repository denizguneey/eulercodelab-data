def solve():
    n = 10000

    # Build valid 3x3 coefficient templates
    coeffs = set()
    for bits in range(512):
        B = [[(bits >> (i*3+j)) & 1 for j in range(3)] for i in range(3)]
        rows = [B[i][0] | B[i][1]<<1 | B[i][2]<<2 for i in range(3)]
        cols = [B[0][j] | B[1][j]<<1 | B[2][j]<<2 for j in range(3)]
        if len(set(rows)) != 3 or len(set(cols)) != 3: continue
        if sorted(rows) != sorted(cols): continue
        c00, c11, c22 = B[0][0], B[1][1], B[2][2]
        cab = B[0][1]+B[1][0]; cac = B[0][2]+B[2][0]; cbc = B[1][2]+B[2][1]
        coeffs.add((c00, c11, c22, cab, cac, cbc))
    coeffs = list(coeffs)

    n2 = n*n; nbits = n2+1
    # Use bytearray as bitset
    le3 = bytearray(nbits); s2 = bytearray(nbits)

    for a in range(n+1):
        for b in range(n+1):
            k = a*b
            le3[k] = 1; le3[n2-k] = 1

    sq = [i*i for i in range(n+1)]
    for a in range(n+1):
        bmax = (n-a)//2
        if bmax < a: continue
        for b in range(a, bmax+1):
            c = n-a-b; aa = sq[a]; bb = sq[b]; cc = sq[c]
            ab = a*b; ac = a*c; bc = b*c
            for c00, c11, c22, cab, cac, cbc in coeffs:
                k = c00*aa + c11*bb + c22*cc + cab*ab + cac*ac + cbc*bc
                le3[k] = 1

    for a in range(n+1):
        b = n-a; w1 = sq[a]; w2 = sq[b]; w3 = 2*a*b
        for v in (w1, w2, w3, w1+w2, w1+w3, w2+w3, w1+w2+w3):
            if v != 0 and v != n2: s2[v] = 1

    cnt_le3 = sum(le3); cnt_s2 = sum(s2); total = n2+1
    n4 = total - cnt_le3
    return str(3*total - 4 - cnt_s2 + n4)

if __name__ == '__main__':
    print(solve())
