def binom(n, k):
    if k > n:
        return 0
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result = (result * (n - k + i)) // i
    return result

def catalan(k):
    return binom(2 * k, k) // (k + 1)

def F_formula(n):
    if n % 2 == 1:
        k = (n - 1) // 2
        return (1 << n) - 2 * binom(2 * k, k)
    
    k = n // 2
    return (1 << n) - 2 * binom(2 * k - 1, k - 1) - catalan(k - 1)

def bit_is_r(mask, i):
    return ((mask >> i) & 1) != 0

def F_bruteforce(n):
    count = 0
    total = 1 << n
    
    for mask in range(total):
        wl = [[0] * n for _ in range(n)]
        wr = [[0] * n for _ in range(n)]
        
        for i in range(n):
            r = bit_is_r(mask, i)
            wl[i][i] = 0 if r else 1
            wr[i][i] = 1 if r else 0
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                left_win = 0
                for t in range(i + 1, j + 1):
                    if not wr[t][j]:
                        left_win = 1
                        break
                wl[i][j] = left_win
                
                right_win = 0
                for t in range(i, j):
                    if not wl[i][t]:
                        right_win = 1
                        break
                wr[i][j] = right_win
                
        if wl[0][n - 1] and wr[0][n - 1]:
            count += 1
            
    return count

def solve():
    return str(F_formula(60))

if __name__ == "__main__":
    assert F_formula(3) == 4
    assert F_formula(8) == 181
    
    for n in range(1, 13):
        assert F_formula(n) == F_bruteforce(n)
        
    print(solve())
