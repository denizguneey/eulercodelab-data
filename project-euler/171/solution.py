# Problem 171: Finding numbers for which the sum of squares of digits is a perfect square.
# Sum (mod 10^9) of all 20-digit numbers (including leading zeros) with square digit-square-sum.

def solve():
    length = 20
    MOD = 10**9
    max_sq = length * 81
    # DP: count[len][s] and sum_val[len][s]
    count = [[0]*(max_sq+1) for _ in range(length+1)]
    sum_val = [[0]*(max_sq+1) for _ in range(length+1)]
    pow10 = [1]*(length+1)
    for i in range(1, length+1):
        pow10[i] = pow10[i-1]*10 % MOD
    count[0][0] = 1
    for ln in range(1, length+1):
        for d in range(10):
            sq = d*d
            for s in range(sq, max_sq+1):
                cp = count[ln-1][s-sq]
                sp = sum_val[ln-1][s-sq]
                if cp == 0 and sp == 0: continue
                count[ln][s] = (count[ln][s] + cp) % MOD
                add = (sp + pow10[ln-1]*d%MOD*cp) % MOD
                sum_val[ln][s] = (sum_val[ln][s] + add) % MOD
    ans = 0
    r = 1
    while r*r <= max_sq:
        ans = (ans + sum_val[length][r*r]) % MOD
        r += 1
    print(ans)

solve()
