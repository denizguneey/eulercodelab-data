import math

def solve():
    M = 100

    g = [[0]*(M+1) for _ in range(M+1)]
    for a in range(1, M+1):
        for b in range(1, M+1):
            g[a][b] = math.gcd(a, b)

    max_i = 2 * M * M + 1
    is_sq = set(x*x for x in range(int(max_i**0.5)+1))

    count = 0
    for a in range(1, M+1):
        for b in range(1, M+1):
            gab = g[a][b]
            for c in range(1, M+1):
                gbc = g[b][c]
                ac = a + c
                for d in range(1, M+1):
                    num = ac * (b + d) - gab - gbc - g[c][d] - g[d][a]
                    interior = num // 2 + 1
                    if interior in is_sq:
                        count += 1

    return str(count)

if __name__ == '__main__':
    print(solve())
