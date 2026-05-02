def solve():
    perimeter_limit = 10_000_000

    def all_triangles_with_perimeter(p):
        if p % 2 == 0:
            return (p * p + 24) // 48
        else:
            t = p + 3
            return (t * t + 24) // 48

    def mobius_up_to(n):
        mu = [0] * (n + 1)
        lp = [0] * (n + 1)
        primes = []
        mu[1] = 1
        for i in range(2, n + 1):
            if lp[i] == 0:
                lp[i] = i
                primes.append(i)
                mu[i] = -1
            for p in primes:
                v = i * p
                if v > n or p > lp[i]:
                    break
                lp[v] = p
                if p == lp[i]:
                    mu[v] = 0
                    break
                mu[v] = -mu[i]
        return mu

    mu = mobius_up_to(perimeter_limit)

    prefix_all = [0] * (perimeter_limit + 1)
    for p in range(1, perimeter_limit + 1):
        prefix_all[p] = prefix_all[p - 1] + all_triangles_with_perimeter(p)

    total = 0
    for d in range(1, perimeter_limit + 1):
        if mu[d] == 0:
            continue
        total += mu[d] * prefix_all[perimeter_limit // d]

    return str(total)

if __name__ == '__main__':
    print(solve())
