# Problem 140: Modified Fibonacci golden nuggets
# AG(x) = x*G1 + x^2*G2*... with G=1,4,5,9,14,...
# Golden nuggets from Pell equation seeds, then x=(X-7)/5.

def solve():
    count = 30
    seeds = [(7,1),(8,2),(13,5),(17,7),(32,14),(43,19)]
    nuggets = set()
    for x0, y0 in seeds:
        x, y = x0, y0
        for _ in range(50):
            if x > 7 and (x - 7) % 5 == 0:
                nuggets.add((x - 7) // 5)
            x, y = 9*x + 20*y, 4*x + 9*y
    vals = sorted(nuggets)
    print(sum(vals[:count]))

solve()
