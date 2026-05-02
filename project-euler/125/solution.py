# Problem 125: Palindromic sums
# Sum of palindromes below 10^8 that are sums of consecutive squares.

def solve():
    limit = 10**8
    max_base = 1
    while max_base * max_base < limit:
        max_base += 1
    
    prefix = [0] * (max_base + 1)
    for i in range(1, max_base + 1):
        prefix[i] = prefix[i-1] + i * i
    
    values = set()
    for start in range(1, max_base + 1):
        for end in range(start + 1, max_base + 1):
            s = prefix[end] - prefix[start - 1]
            if s >= limit: break
            ss = str(s)
            if ss == ss[::-1]:
                values.add(s)
    
    print(sum(values))

solve()
