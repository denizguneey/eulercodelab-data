def g_value(n):
    s = str(n)
    d = len(s)
    pi = [0] * d
    for i in range(1, d):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
        
    expected_end = 0
    k = d
    while k > 0:
        expected_end += 10 ** k
        k = pi[k - 1]
        
    return expected_end - d + 1

def solve(numerator=10000000000000000, max_n=999999):
    total = 0
    for n in range(2, max_n + 1):
        total += g_value(numerator // n)
    return str(total)

if __name__ == '__main__':
    print(solve())
