def solve():
    limit = 10000000
    div_count = [0] * (limit + 2)
    for d in range(1, limit + 2):
        for m in range(d, limit + 2, d):
            div_count[m] += 1
    answer = 0
    for n in range(2, limit):
        if div_count[n] == div_count[n + 1]:
            answer += 1
    return str(answer)

if __name__ == '__main__':
    print(solve())
