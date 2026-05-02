def solve():
    max_number = 999
    pair_count = (max_number - 1) // 2
    total_numbers = 2 * pair_count + 2

    e0 = [0.0] * (pair_count + 1)
    e1 = [0.0] * (pair_count + 1)

    for k in range(pair_count, -1, -1):
        den = float(total_numbers - (k + 1))
        grow = float(2 * (pair_count - k))
        if k == pair_count:
            e1[k] = float(total_numbers) / den
            e0[k] = (float(total_numbers) + e1[k]) / den
        else:
            e1[k] = (float(total_numbers) + grow * e1[k + 1]) / den
            e0[k] = (float(total_numbers) + grow * e0[k + 1] + e1[k]) / den

    result = e0[0]
    return f"{result:.8f}"

if __name__ == '__main__':
    print(solve())
