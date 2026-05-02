def solve():
    order = 100_000_000

    memo = {0: 0, 1: 1}

    def totient_sum(n):
        if n in memo:
            return memo[n]
        total = n * (n + 1) // 2
        left = 2
        while left <= n:
            q = n // left
            right = n // q
            total -= (right - left + 1) * totient_sum(q)
            left = right + 1
        memo[n] = total
        return total

    triangle = order * (order + 1) // 2
    visible = totient_sum(order)
    hidden = triangle - visible
    return str(hidden * 6)

if __name__ == '__main__':
    print(solve())
