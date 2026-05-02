def solve():
    MOD = 1000000007
    exp = 25

    if exp == 1: return '1'
    if exp == 2: return '3'

    perm = [1, 3, 2, 4]
    lehmer = [0, 1, 0, 0]
    n = 4; target = 1 << exp

    while n < target:
        perm = perm + [0]*n; lehmer = lehmer + [0]*n
        for i in range(n-1, 0, -1):
            perm[n+i] = 2*perm[i]; lehmer[n+i] = lehmer[i]
        perm[n] = 2*perm[n-1]-1; lehmer[n] = n-2
        perm[n-1] = 2*perm[0]; lehmer[n-1] = 0
        for i in range(n-2, -1, -1):
            lehmer[i] = perm[i]-1+lehmer[i]; perm[i] = 2*perm[i]-1
        n *= 2

    rank = 1; fact = 1
    k = 0
    for i in range(target-1, -1, -1):
        rank = (rank + lehmer[i] * fact) % MOD
        k += 1; fact = fact * k % MOD

    return str(rank)

if __name__ == '__main__':
    print(solve())
