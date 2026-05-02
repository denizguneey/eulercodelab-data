def solve():
    size = 8

    def build_row_states(length):
        states = []
        def dfs(idx, colors):
            if idx == length:
                odd_code = 0
                even_code = 0
                odd_pow = 1
                even_pow = 1
                for i in range(length):
                    if i % 2 == 0:
                        even_code += colors[i] * even_pow
                        even_pow *= 3
                    else:
                        odd_code += colors[i] * odd_pow
                        odd_pow *= 3
                states.append((odd_code, even_code))
                return
            for c in range(3):
                if idx > 0 and colors[idx - 1] == c:
                    continue
                colors[idx] = c
                dfs(idx + 1, colors)
        dfs(0, [0] * length)
        return states

    states_by_row = [build_row_states(2 * r + 1) for r in range(size)]
    dp_prev = [1] * len(states_by_row[0])

    for r in range(1, size):
        sig_count = 3 ** r
        agg = [0] * sig_count
        for i, (odd_c, even_c) in enumerate(states_by_row[r - 1]):
            agg[even_c] += dp_prev[i]

        memo = {}

        def compatible_sum(req_code):
            if req_code in memo:
                return memo[req_code]
            req_digits = []
            tmp = req_code
            for _ in range(r):
                req_digits.append(tmp % 3)
                tmp //= 3

            total = [0]
            def rec(idx, code, pow3):
                if idx == r:
                    total[0] += agg[code]
                    return
                for color in range(3):
                    if color == req_digits[idx]:
                        continue
                    rec(idx + 1, code + color * pow3, pow3 * 3)
            rec(0, 0, 1)
            memo[req_code] = total[0]
            return total[0]

        dp_curr = [0] * len(states_by_row[r])
        for i, (odd_c, even_c) in enumerate(states_by_row[r]):
            dp_curr[i] = compatible_sum(odd_c)
        dp_prev = dp_curr

    return str(sum(dp_prev))

if __name__ == '__main__':
    print(solve())
