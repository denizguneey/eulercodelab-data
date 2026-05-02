def is_palindrome(value):
    s = str(value)
    return s == s[::-1]

def solve(digits=3):
    low = 10 ** (digits - 1)
    high = 10 ** digits - 1
    best = 0
    for a in range(high, low - 1, -1):
        if a * high < best:
            break
        for b in range(a, low - 1, -1):
            prod = a * b
            if prod <= best:
                break
            if is_palindrome(prod):
                best = prod
    return best

if __name__ == "__main__":
    assert solve(2) == 9009, "Checkpoint failed for digits=2"
    print(solve())
