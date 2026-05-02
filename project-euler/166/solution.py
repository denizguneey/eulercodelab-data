def solve():
    dmax = 9
    answer = 0
    for a in range(dmax + 1):
        for b in range(dmax + 1):
            for c in range(dmax + 1):
                for g in range(dmax + 1):
                    for j in range(dmax + 1):
                        m = a + b + c - g - j
                        if m < 0 or m > dmax:
                            continue
                        for e in range(dmax + 1):
                            for i in range(dmax + 1):
                                S = a + e + i + m
                                d = S - a - b - c
                                if d < 0 or d > dmax:
                                    continue
                                for f in range(dmax + 1):
                                    h = S - e - f - g
                                    if h < 0 or h > dmax:
                                        continue
                                    n = S - b - f - j
                                    if n < 0 or n > dmax:
                                        continue
                                    for k in range(dmax + 1):
                                        o = S - c - g - k
                                        if o < 0 or o > dmax:
                                            continue
                                        l = S - i - j - k
                                        if l < 0 or l > dmax:
                                            continue
                                        p = S - a - f - k
                                        if p < 0 or p > dmax:
                                            continue
                                        if m + n + o + p != S:
                                            continue
                                        if d + h + l + p != S:
                                            continue
                                        answer += 1
    return str(answer)

if __name__ == '__main__':
    print(solve())
