def solve():
    PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    LIMIT = 10000000000000
    total = 0

    def is_smooth(x):
        for p in PRIMES:
            while x % p == 0: x //= p
        return x == 1

    def dfs(idx, cur):
        nonlocal total
        if idx == len(PRIMES):
            x = cur
            if is_smooth(2*x+1): total += 2*x
            if is_smooth(2*x-1): total += 2*x-1
            return
        p = PRIMES[idx]; v = cur
        while v <= LIMIT:
            dfs(idx+1, v)
            if v > LIMIT // p: break
            v *= p

    dfs(0, 1)
    return str(total)

if __name__ == '__main__':
    print(solve())
