# Problem 93: Arithmetic expressions
# Find the set of four digits which can generate the longest consecutive run
# of positive integers using +, -, *, / and parentheses.

from itertools import permutations, product

def solve():
    def evaluate(a, b, op):
        if op == 0: return a + b
        if op == 1: return a - b
        if op == 2: return a * b
        if op == 3: return a / b if b != 0 else None
        return None
    
    def all_results(nums):
        results = set()
        for perm in permutations(nums):
            a, b, c, d = [float(x) for x in perm]
            for o1, o2, o3 in product(range(4), repeat=3):
                # ((a o1 b) o2 c) o3 d
                r = evaluate(a, b, o1)
                if r is not None:
                    r = evaluate(r, c, o2)
                    if r is not None:
                        r = evaluate(r, d, o3)
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
                # (a o1 (b o2 c)) o3 d
                r = evaluate(b, c, o2)
                if r is not None:
                    r = evaluate(a, r, o1)
                    if r is not None:
                        r = evaluate(r, d, o3)
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
                # (a o1 b) o2 (c o3 d)
                r1 = evaluate(a, b, o1)
                r2 = evaluate(c, d, o3)
                if r1 is not None and r2 is not None:
                    r = evaluate(r1, r2, o2)
                    if r is not None and r > 0 and r == int(r):
                        results.add(int(r))
                # a o1 ((b o2 c) o3 d)
                r = evaluate(b, c, o2)
                if r is not None:
                    r = evaluate(r, d, o3)
                    if r is not None:
                        r = evaluate(a, r, o1)
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
                # a o1 (b o2 (c o3 d))
                r = evaluate(c, d, o3)
                if r is not None:
                    r = evaluate(b, r, o2)
                    if r is not None:
                        r = evaluate(a, r, o1)
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
        return results
    
    def consecutive_length(s):
        n = 1
        while n in s:
            n += 1
        return n - 1
    
    best_len, best_digits = 0, ''
    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    results = all_results([a, b, c, d])
                    length = consecutive_length(results)
                    if length > best_len:
                        best_len = length
                        best_digits = f"{a}{b}{c}{d}"
    print(best_digits)

solve()
