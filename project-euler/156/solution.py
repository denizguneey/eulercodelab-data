# Problem 156: Counting Digits - find fixed points where f(n,d) = n

def solve():
    def count_digit_upto(n, d):
        """Count occurrences of digit d in 1..n"""
        n += 1
        result = 0
        p10 = 1
        while p10 < n:
            cur = (n // p10) % 10
            result += (n // p10 // 10) * p10
            if cur == d:
                result += n % p10
            elif cur > d:
                result += p10
            p10 *= 10
        return result
    
    def search(d, start, span, limit, acc):
        if start > limit:
            return acc
        right = min(limit, start + span)
        lo = count_digit_upto(start, d)
        hi = count_digit_upto(right, d)
        if hi < start or lo > right:
            return acc
        if span == 1:
            if lo == start:
                acc += start
            return acc
        step = span // 10
        for k in range(10):
            acc = search(d, start + k * step, step, limit, acc)
        return acc
    
    limit = 10**11
    root_span = 1
    while root_span < limit:
        root_span *= 10
    
    total = 0
    for d in range(1, 10):
        total = total + search(d, 0, root_span, limit, 0)
    print(total)

solve()
