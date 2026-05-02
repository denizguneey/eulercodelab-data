import math

def solve():
    digits_count = 10
    odd_slots = digits_count
    even_slots = digits_count

    fact = [1] * (2 * digits_count + 1)
    for i in range(2, 2 * digits_count + 1):
        fact[i] = fact[i-1] * i

    odd_take = [0] * digits_count
    answer = 0

    def dfs(digit, used, weighted):
        nonlocal answer
        if digit == digits_count:
            if used != odd_slots: return
            total_digit_sum = digits_count * (digits_count - 1) // 2
            if (weighted - total_digit_sum) % 11 != 0: return

            odd_all = fact[odd_slots]
            odd_zero_lead = 0
            even_all = fact[even_slots]

            for d in range(digits_count):
                odd_all //= fact[odd_take[d]]
                even_all //= fact[2 - odd_take[d]]

            if odd_take[0] > 0:
                odd_zero_lead = fact[odd_slots - 1]
                odd_zero_lead //= fact[odd_take[0] - 1]
                for d in range(1, digits_count):
                    odd_zero_lead //= fact[odd_take[d]]

            answer += (odd_all - odd_zero_lead) * even_all
            return

        for take in range(3):
            if used + take > odd_slots: continue
            odd_take[digit] = take
            dfs(digit + 1, used + take, weighted + digit * take)

    dfs(0, 0, 0)
    return str(answer)

if __name__ == '__main__':
    print(solve())
