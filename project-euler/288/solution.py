def solve(p=61, q=10000000, exponent=10):
    mod = p ** exponent
    first_len = min(exponent, q + 1)
    prefix = [0] * (first_len + 1)

    s = 290797
    total = 0
    for n in range(q + 1):
        t = s % p
        total += t
        if n < first_len:
            prefix[n + 1] = prefix[n] + t
        s = (s * s) % 50515093

    answer = 0
    p_pow = 1
    for j in range(exponent):
        pref = 0
        if j + 1 <= first_len:
            pref = prefix[j + 1]
        elif first_len == q + 1:
            pref = total
        else:
            pref = prefix[first_len]
            
        suffix = total - pref
        answer = (answer + p_pow * (suffix % mod)) % mod
        p_pow = (p_pow * p) % mod

    return str(answer)

if __name__ == '__main__':
    print(solve())
