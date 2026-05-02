def solve():
    n = 100
    choose = 50
    values = [i * i for i in range(1, n + 1)]

    max_sum = sum(values[n - choose:])
    width = max_sum + 1

    dp = bytearray((choose + 1) * width)
    dp[0] = 1

    low = [0] * (choose + 1)
    high = [-1] * (choose + 1)
    high[0] = 0

    for i in range(n):
        x = values[i]
        up = min(choose, i + 1)
        for k in range(up, 0, -1):
            if high[k - 1] < 0:
                continue
            start = low[k - 1] + x
            end = high[k - 1] + x
            for s in range(end, start - 1, -1):
                add = dp[(k - 1) * width + (s - x)]
                if add == 0:
                    continue
                p = k * width + s
                total = dp[p] + add
                dp[p] = 2 if total >= 2 else total
            if high[k] < 0:
                low[k] = start
                high[k] = end
            else:
                low[k] = min(low[k], start)
                high[k] = max(high[k], end)

    answer = 0
    for s in range(low[choose], high[choose] + 1):
        if dp[choose * width + s] == 1:
            answer += s
    return str(answer)

if __name__ == '__main__':
    print(solve())
