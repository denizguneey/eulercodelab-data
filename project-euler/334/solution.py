def generate_beans(count):
    beans = []
    t = 123456
    for i in range(count):
        if (t & 1) == 0:
            t //= 2
        else:
            t = (t // 2) ^ 926252
        b = (t & ((1 << 11) - 1)) + 1
        beans.append(b)
    return beans

def sum_squares_arith(first, n):
    if n <= 0:
        return 0
    sum_k = n * (n - 1) // 2
    sum_k2 = n * (n - 1) * (2 * n - 1) // 6
    return n * first * first + 2 * first * sum_k + sum_k2

def moves_needed(beans):
    total = 0
    first_moment = 0
    second_moment = 0

    for i, b in enumerate(beans):
        total += b
        first_moment += i * b
        second_moment += i * i * b

    B = total
    target_shift = first_moment - B * (B - 1) // 2

    q = target_shift // B
    r = target_shift % B

    n1 = B - r
    n2 = r

    q_final = sum_squares_arith(q, n1) + sum_squares_arith(q + n1 + 1, n2)

    diff = q_final - second_moment
    return diff // 2

def solve():
    beans = generate_beans(1500)
    ans = moves_needed(beans)
    return str(ans)

if __name__ == '__main__':
    print(solve())
