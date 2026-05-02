def sum_H_up_to(N):
    ans = 0
    s = 1
    while 3 * s <= N:
        M = N - 3 * s + 1
        ans += s * M * (M + 1) * (M + 2) // 6
        s += 1
    return ans

def solve():
    N = 12345
    return str(sum_H_up_to(N))

if __name__ == '__main__':
    print(solve())
