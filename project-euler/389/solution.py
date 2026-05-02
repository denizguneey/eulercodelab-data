def uniform_die_stats(sides):
    s = float(sides)
    return ((s + 1.0) / 2.0, (s * s - 1.0) / 12.0)

def transition_sum(count_mean, count_var, sides):
    per_mean, per_var = uniform_die_stats(sides)
    mean = per_mean * count_mean
    var = per_var * count_mean + per_mean * per_mean * count_var
    return (mean, var)

def solve():
    mean, var = uniform_die_stats(4)
    for sides in [6, 8, 12, 20]:
        mean, var = transition_sum(mean, var, sides)
    return "{:.4f}".format(var)

if __name__ == '__main__':
    print(solve())
