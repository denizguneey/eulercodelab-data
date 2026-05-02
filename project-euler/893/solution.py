def solve():
    DIGIT_COST = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    N = 1000000

    m = [0]*(N+1)
    for n in range(1, N+1):
        m[n] = m[n//10] + DIGIT_COST[n%10]

    # Improve via multiplication
    changed = True
    while changed:
        changed = False
        for x in range(1, N+1):
            cx = m[x]; maxy = N // x
            if maxy < x: break
            for y in range(x, maxy+1):
                prod = x * y; cand = cx + m[y] + 2
                if cand < m[prod]:
                    m[prod] = cand; changed = True

    # Improve via addition
    changed = True
    while changed:
        changed = False
        maxm = max(m[1:N+1])
        by_cost = [[] for _ in range(maxm+1)]
        for n in range(1, N+1): by_cost[m[n]].append(n)
        for ca in range(maxm+1):
            A = by_cost[ca]
            if not A: continue
            for cb in range(ca, maxm+1):
                B = by_cost[cb]
                if not B: continue
                cand = ca + cb + 2
                if cand >= maxm: break
                if ca == cb:
                    for i, x in enumerate(A):
                        for j in range(i, len(A)):
                            s = x + A[j]
                            if s > N: break
                            if cand < m[s]: m[s] = cand; changed = True
                else:
                    P, Q = (A, B) if len(A) <= len(B) else (B, A)
                    for x in P:
                        for y in Q:
                            s = x + y
                            if s > N: break
                            if cand < m[s]: m[s] = cand; changed = True

    return str(sum(m[1:N+1]))

if __name__ == '__main__':
    print(solve())
