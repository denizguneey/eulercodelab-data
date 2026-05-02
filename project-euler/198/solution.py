def solve():
    T_NUM = 1
    T_DEN = 100
    TARGET_Q = 100_000_000

    def count_subtree(seed_a, seed_b, seed_c, seed_d, max_product):
        stack = [(seed_a, seed_b, seed_c, seed_d)]
        count = 0
        while stack:
            a, b, c, d = stack.pop()
            if b > max_product // d if d > 0 else True:
                continue
            if a * T_DEN >= T_NUM * b:
                continue
            ad_bc = a * d + b * c
            if ad_bc * T_DEN < 2 * T_NUM * b * d:
                count += 1
            mn = a + c
            md = b + d
            stack.append((a, b, mn, md))
            stack.append((mn, md, c, d))
        return count

    max_product = TARGET_Q // 2
    answer = count_subtree(0, 1, 1, 1, max_product)
    return str(answer)

if __name__ == '__main__':
    print(solve())
