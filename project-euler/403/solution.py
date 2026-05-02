def F1(n):
    return (n * n - n + 6) * (n + 1) // 6

def F2(n):
    return (n * n - n + 12) * (n + 1) * (n + 2) // 24

def F3(n):
    return (n * n - n + 20) * (n + 1) * (n + 2) * (n + 3) // 120

def solve():
    n = 1000000000000
    ans = F2(n) + F2(n + 1) + F2(n - 2) + F1(n) + F1(n + 1)
    
    x = 2
    while x < n:
        c = n // x
        next_x = min(n // c + 1, n)
        ans += F3(next_x - 1 + c) - F3(x - 1 + c)
        if x > c:
            ans -= F3(next_x - c - 2) - F3(x - c - 2)
        else:
            ans += F3(c - x) - F3(c - next_x)
        x = next_x
        
    ans %= 100000000
    if ans < 0:
        ans += 100000000
    return str(ans)

if __name__ == '__main__':
    print(solve())
