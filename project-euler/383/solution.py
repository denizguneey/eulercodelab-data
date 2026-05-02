def solve():
    memo = {}

    def carry_out(digit, carry_in):
        return (2 * digit + carry_in) // 5

    def count_with_initial_carry(x, k, carry_in):
        if x < 0 or k < 0:
            return 0
        if x == 0:
            return 1

        key = (x, k, carry_in)
        if key in memo:
            return memo[key]

        ways = 0
        for digit in range(5):
            if x < digit:
                break
            q = (x - digit) // 5
            next_carry = carry_out(digit, carry_in)
            ways += count_with_initial_carry(q, k - next_carry, next_carry)

        memo[key] = ways
        return ways

    def count_non_multiples_of_five(x, k):
        if x <= 0 or k < 0:
            return 0
        ways = 0
        for digit in range(1, 5):
            if x < digit:
                break
            q = (x - digit) // 5
            next_carry = carry_out(digit, 0)
            ways += count_with_initial_carry(q, k - next_carry, next_carry)
        return ways

    n = 1000000000000000000
    answer = 0
    power_of_five = 5

    a = 1
    while power_of_five <= n:
        answer += count_non_multiples_of_five(n // power_of_five, a - 1)
        if power_of_five > n // 5:
            break
        power_of_five *= 5
        a += 1

    return str(answer)

if __name__ == '__main__':
    print(solve())
