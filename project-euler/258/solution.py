def solve():
    K = 2000
    index = 1_000_000_000_000_000_000
    mod = 20092010

    def multiply_mod(a, b, m):
        tmp = [0] * (2 * K)
        for i in range(K):
            if a[i] == 0:
                continue
            for j in range(K):
                if b[j] == 0:
                    continue
                tmp[i + j] = (tmp[i + j] + a[i] * b[j]) % m
        for i in range(2 * K - 1, K - 1, -1):
            v = tmp[i] % m
            if v == 0:
                continue
            tmp[i - K] = (tmp[i - K] + v) % m
            tmp[i - K + 1] = (tmp[i - K + 1] + v) % m
        return [tmp[i] % m for i in range(K)]

    if index < K:
        return str(1 % mod)

    acc = [0] * K
    acc[0] = 1
    base = [0] * K
    base[1] = 1

    exp = index
    while exp > 0:
        if exp & 1:
            acc = multiply_mod(acc, base, mod)
        exp >>= 1
        if exp != 0:
            base = multiply_mod(base, base, mod)

    answer = sum(acc) % mod
    return str(answer)

if __name__ == '__main__':
    print(solve())
