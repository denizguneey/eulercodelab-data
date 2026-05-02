# Problem 217: Balanced Numbers
# Sum of all balanced numbers < 10^47, mod 3^15.
# A number is balanced if sum of first half digits = sum of second half digits.

def solve():
    n = 47
    mod = 3**15  # 14348907

    def add_mod(a, b):
        s = a + b
        return s - mod if s >= mod else s

    def mul_mod(a, b):
        return (a * b) % mod

    # Build DP for left/right halves
    def build_dp(max_len, leading_nonzero):
        max_sum = 9 * max_len
        count = [[0] * (max_sum + 1) for _ in range(max_len + 1)]
        sumv = [[0] * (max_sum + 1) for _ in range(max_len + 1)]
        count[0][0] = 1
        for l in range(max_len):
            for s in range(9 * l + 1):
                cnt = count[l][s]
                sm = sumv[l][s]
                if cnt == 0 and sm == 0:
                    continue
                d_start = 1 if (leading_nonzero and l == 0) else 0
                for d in range(d_start, 10):
                    ns = s + d
                    count[l+1][ns] = add_mod(count[l+1][ns], cnt)
                    val = add_mod(mul_mod(sm, 10), mul_mod(d, cnt))
                    sumv[l+1][ns] = add_mod(sumv[l+1][ns], val)
        return count, sumv

    max_half = (n + 1) // 2
    cnt_left, sum_left = build_dp(max_half, True)
    cnt_right, sum_right = build_dp(max_half, False)

    pow10 = [1 % mod] * (n + 2)
    for i in range(1, n + 2):
        pow10[i] = mul_mod(pow10[i-1], 10)

    total = 0
    for length in range(1, n + 1):
        half = length // 2
        odd = length % 2 == 1
        max_sum = 9 * half

        cl = cnt_left[half]
        sl = sum_left[half]
        cr = cnt_right[half]
        sr = sum_right[half]

        if not odd:
            shift = pow10[half]
            for s in range(max_sum + 1):
                if cl[s] == 0 or cr[s] == 0:
                    continue
                part_l = mul_mod(mul_mod(sl[s], shift), cr[s])
                part_r = mul_mod(sr[s], cl[s])
                total = add_mod(total, add_mod(part_l, part_r))
        else:
            shift_l = pow10[half + 1]
            shift_m = pow10[half]
            for s in range(max_sum + 1):
                if cl[s] == 0 or cr[s] == 0:
                    continue
                part_l = mul_mod(mul_mod(sl[s], shift_l), mul_mod(cr[s], 10))
                part_m = mul_mod(mul_mod(45, shift_m), mul_mod(cl[s], cr[s]))
                part_r = mul_mod(mul_mod(sr[s], cl[s]), 10)
                total = add_mod(total, add_mod(add_mod(part_l, part_m), part_r))

    print(total)

solve()
