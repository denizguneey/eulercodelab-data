# Problem 168: Number Rotations
# Sum (mod 10^5) of all n (2+ digits, <= 10^100) where the last digit moves to front
# and the result equals n * multiplier for some 1 <= multiplier <= 9.

def solve():
    MOD = 100000
    total = 0
    for digits in range(2, 101):
        for m in range(1, 10):
            for last in range(1, 10):
                # Build the number digit by digit from right
                # n = ...d2 d1 d0, rotated = d0 d_{k-1} ... d1
                # rotated = m * n
                val_mod = last % MOD
                current = last
                carry = 0
                place_mod = 10 % MOD
                for pos in range(1, digits):
                    nxt = m * current + carry
                    carry = nxt // 10
                    current = nxt % 10
                    val_mod = (val_mod + current * place_mod) % MOD
                    place_mod = (place_mod * 10) % MOD
                leading = m * current + carry
                if current == 0 or leading != last:
                    continue
                total = (total + val_mod) % MOD
    print(total)

solve()
