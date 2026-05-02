def solve():
    colors = 7
    balls_per_color = 10
    draws = 20

    total = colors * balls_per_color
    without = (colors - 1) * balls_per_color

    # C(without, draws) / C(total, draws)
    ratio = 1.0
    for i in range(draws):
        ratio *= (without - i) / (total - i)

    ans = colors * (1.0 - ratio)
    return f"{ans:.9f}"

if __name__ == '__main__':
    print(solve())
