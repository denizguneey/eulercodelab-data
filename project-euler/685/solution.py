def binom_small(n, k):
    if k < 0 or k > n: return 0
    if k > n - k: k = n - k
    out = 1
    for i in range(1, k + 1):
        out = out * (n - k + i) // i
    return out

def count_0_to_9(digits, sum_val):
    if sum_val > 9 * digits: return 0
    if digits == 0: return 1 if sum_val == 0 else 0
    
    total = 0
    max_j = sum_val // 10
    for j in range(max_j + 1):
        remain = sum_val - 10 * j
        term = binom_small(digits, j) * binom_small(digits + remain - 1, remain)
        if j % 2 == 0:
            total += term
        else:
            total -= term
    return total

def count_len_with_sum(length, sum_val):
    if length == 0 or sum_val == 0: return 0
    if sum_val > 9 * length: return 0
    
    deficit = 9 * length - sum_val
    max_first_deficit = min(8, deficit)
    
    out = 0
    for b0 in range(max_first_deficit + 1):
        out += count_0_to_9(length - 1, deficit - b0)
    return out

MOD = 1000000007

def mod_pow10(exp):
    return pow(10, exp, MOD)

def append_digit_mod(value_mod, digit):
    return (value_mod * 10 + digit) % MOD

def append_nines_mod(value_mod, count):
    if count == 0: return value_mod
    p10 = mod_pow10(count)
    return (value_mod * p10 + p10 - 1) % MOD

def locate_length_and_rank(digit_sum, occurrence_rank):
    target = occurrence_rank
    length = (digit_sum + 8) // 9
    prefix_count = 0
    
    while True:
        cnt_here = count_len_with_sum(length, digit_sum)
        if prefix_count + cnt_here >= target:
            return length, target - prefix_count
        prefix_count += cnt_here
        length += 1

def unrank_mod(length, digit_sum, rank_inside_len):
    initial_deficit = 9 * length - digit_sum
    value_mod = 0
    remaining_digits = length
    remaining_deficit = initial_deficit
    
    max_deficit_here = min(8, remaining_deficit)
    for deficit_digit in range(max_deficit_here, -1, -1):
        cnt = count_0_to_9(remaining_digits - 1, remaining_deficit - deficit_digit)
        if rank_inside_len > cnt:
            rank_inside_len -= cnt
            continue
        value_mod = append_digit_mod(value_mod, 9 - deficit_digit)
        remaining_deficit -= deficit_digit
        remaining_digits -= 1
        break
        
    while remaining_digits > 0:
        if remaining_deficit == 0:
            value_mod = append_nines_mod(value_mod, remaining_digits)
            break
            
        total_here = count_0_to_9(remaining_digits, remaining_deficit)
        zero_branch = count_0_to_9(remaining_digits - 1, remaining_deficit)
        nonzero_prefix = total_here - zero_branch
        
        if rank_inside_len > nonzero_prefix:
            low = 1
            high = remaining_digits
            best = 1
            
            while low <= high:
                mid = low + ((high - low) >> 1)
                suffix = count_0_to_9(remaining_digits - mid, remaining_deficit)
                removed = total_here - suffix
                
                if rank_inside_len > removed:
                    best = mid
                    low = mid + 1
                else:
                    if mid == 0: break
                    high = mid - 1
                    
            suffix = count_0_to_9(remaining_digits - best, remaining_deficit)
            removed = total_here - suffix
            rank_inside_len -= removed
            
            value_mod = append_nines_mod(value_mod, best)
            remaining_digits -= best
            continue
            
        max_deficit_here = min(9, remaining_deficit)
        for deficit_digit in range(max_deficit_here, -1, -1):
            cnt = count_0_to_9(remaining_digits - 1, remaining_deficit - deficit_digit)
            if rank_inside_len > cnt:
                rank_inside_len -= cnt
                continue
            value_mod = append_digit_mod(value_mod, 9 - deficit_digit)
            remaining_deficit -= deficit_digit
            remaining_digits -= 1
            break
            
    return value_mod

def f_mod(digit_sum, occurrence_rank):
    length, rank_inside_len = locate_length_and_rank(digit_sum, occurrence_rank)
    return unrank_mod(length, digit_sum, rank_inside_len)

def solve():
    k = 10000
    ans = 0
    for n in range(1, k + 1):
        s = n * n * n
        m = s * n
        ans = (ans + f_mod(s, m)) % MOD
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
