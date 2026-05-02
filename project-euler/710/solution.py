def solve():
    kDiv = 1000000
    a_mod = [1, 1, 1, 2, 2, 3, 4]
    
    pow2 = 1
    n = 1
    while True:
        if (n & 1) == 0:
            pow2 = (pow2 * 2) % kDiv
            
        if n >= 7:
            next_val = (a_mod[(n - 1) % 7] +
                        2 * a_mod[(n - 2) % 7] -
                        2 * a_mod[(n - 3) % 7] -
                        a_mod[(n - 4) % 7] +
                        a_mod[(n - 5) % 7] +
                        a_mod[(n - 6) % 7] -
                        a_mod[(n - 7) % 7])
            a_mod[n % 7] = next_val % kDiv
            
        t_mod = (pow2 - a_mod[n % 7]) % kDiv
        if n > 42 and t_mod == 0:
            return str(n)
        n += 1

if __name__ == "__main__":
    print(solve())
