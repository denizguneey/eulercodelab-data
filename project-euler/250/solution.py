def solve():
    limit = 250250
    divisor = 250
    modulo = 10**16

    dp = [0] * divisor
    dp[0] = 1

    for i in range(1, limit + 1):
        residue = pow(i, i, divisor)
        new_dp = list(dp)
        for r in range(divisor):
            to = (r + residue) % divisor
            new_dp[to] = (new_dp[to] + dp[r]) % modulo
        dp = new_dp

    return str((dp[0] + modulo - 1) % modulo)

if __name__ == '__main__':
    print(solve())
