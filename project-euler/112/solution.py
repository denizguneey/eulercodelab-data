# Problem 112: Bouncy numbers
# Find n where proportion of bouncy numbers is exactly 99%.

def is_bouncy(n):
    s = str(n)
    inc = dec = False
    for i in range(1, len(s)):
        if s[i] > s[i-1]: inc = True
        elif s[i] < s[i-1]: dec = True
        if inc and dec: return True
    return False

def solve():
    bouncy = 0
    for n in range(1, 10000000):
        if is_bouncy(n):
            bouncy += 1
        if bouncy * 100 == n * 99:
            print(n)
            return

solve()
