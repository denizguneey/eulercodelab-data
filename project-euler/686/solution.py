import math

def solve():
    L = 123
    target = 678910

    d = len(str(L))
    lo = math.log10(L) - (d - 1)
    hi = math.log10(L + 1) - (d - 1)
    alpha = math.log10(2.0)

    x = 0.0
    cnt = 0
    j = 0

    while cnt < target:
        j += 1
        x += alpha
        if x >= 1.0:
            x -= 1.0
        if lo <= x < hi:
            cnt += 1

    return str(j)

if __name__ == '__main__':
    print(solve())
