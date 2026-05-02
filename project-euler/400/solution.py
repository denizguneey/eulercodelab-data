def solve():
    MOD = 10**18
    K = 10000
    sg = [0] * (K + 1)
    if K >= 2: sg[2] = 1
    for i in range(3, K + 1):
        sg[i] = (1 + sg[i-1]) ^ (1 + sg[i-2])

    cache = [dict() for _ in range(K + 1)]

    def prune(ts, target):
        if target == -1: return 1
        if target < -1: return 0
        if ts == 1: return 0
        if ts == 2: return 1 if target == 0 else 0
        if target in cache[ts]: return cache[ts][target]
        rt = ((sg[ts-1] + 1) ^ target) - 1
        lt = ((sg[ts-2] + 1) ^ target) - 1
        res = (prune(ts-2, rt) + prune(ts-1, lt)) % MOD
        cache[ts][target] = res
        return res

    import sys
    sys.setrecursionlimit(50000)
    ans = prune(K, 0)
    return str(ans).zfill(18)

if __name__ == '__main__':
    print(solve())
