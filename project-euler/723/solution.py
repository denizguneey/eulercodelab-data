def solve():
    exps = [6, 3, 2, 1, 1, 1, 1, 1]
    
    def prod(term_func):
        out = 1
        for e in exps:
            out *= term_func(e)
        return out
        
    t1 = 7 * prod(lambda e: (e + 1) * (e + 2) // 2)
    t2 = 14 * prod(lambda e: (e + 1) * (e + 2) * (2 * e + 3) // 6)
    
    def term3(e):
        a = (e + 1) * (e + 2) * (2 * e + 3) // 6
        b = e // 2 + 1
        return (a + b) // 2
    t3 = 4 * prod(term3)
    
    def term4(e):
        x = (e + 1) * (e + 2) // 2
        return x * x
    t4 = 8 * prod(term4)
    
    t5 = 4 * prod(lambda e: (e + 1) * (e + 2) * (e * e + 3 * e + 3) // 6)
    
    ans = t1 - t2 - t3 + t4 + t5
    return str(ans)

if __name__ == "__main__":
    print(solve())
