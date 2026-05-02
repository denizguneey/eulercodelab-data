def solve():
    limit = 50000000
    count = bytearray(limit)
    for u in range(1, limit):
        vmax = (limit - 1) // u
        upper = min(vmax, 3 * u - 1)
        if upper < 1:
            continue
        v = (-u) % 4
        if v == 0:
            v = 4
        while v <= upper:
            n = u * v
            if count[n] < 2:
                count[n] += 1
            v += 4
    answer = 0
    for n in range(1, limit):
        if count[n] == 1:
            answer += 1
    return str(answer)

if __name__ == '__main__':
    print(solve())
