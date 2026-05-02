import sys
import math

DIGITS = [1, 3, 5, 7, 9]
pow10mod7 = [1] * 50
for i in range(1, 50):
    pow10mod7[i] = (pow10mod7[i-1] * 10) % 7

memo = {}

def get_rem_counts(counts):
    total_len = sum(counts)
    if total_len == 0:
        res = [0]*7
        res[0] = 1
        return res
        
    if counts in memo:
        return memo[counts]
        
    total_res = [0]*7
    power = pow10mod7[total_len - 1]
    
    for i in range(5):
        if counts[i] > 0:
            next_counts = list(counts)
            next_counts[i] -= 1
            next_tuple = tuple(next_counts)
            
            sub_res = get_rem_counts(next_tuple)
            
            digit = DIGITS[i]
            cur_rem = (digit * power) % 7
            
            for r in range(7):
                if sub_res[r] > 0:
                    new_rem = (cur_rem + r) % 7
                    total_res[new_rem] += sub_res[r]
                    
    memo[counts] = total_res
    return total_res

def process_tuples(chunk):
    count = 0
    for c in chunk:
        sum_digits = sum(c[i] * DIGITS[i] for i in range(5))
        if sum_digits % 3 != 0:
            continue
            
        if c[2] < 1:
            continue
            
        remaining = list(c)
        remaining[2] -= 1
        
        rems = get_rem_counts(tuple(remaining))
        count += rems[3]
        
    return count

def generate_partitions(index, remaining_len, current, result):
    if index == 5:
        if remaining_len == 0:
            result.append(tuple(current))
        return
        
    for k in range(1, remaining_len + 1, 2):
        current[index] = k
        if remaining_len - k >= (4 - index):
            generate_partitions(index + 1, remaining_len - k, current, result)

def find_nth(N):
    current_count = 0
    L = 5
    while True:
        all_tuples = []
        generate_partitions(0, L, [0]*5, all_tuples)
        
        # We can just process locally since it's fast enough in Python using DP
        count_for_L = process_tuples(all_tuples)
        
        if current_count + count_for_L >= N:
            res = ""
            target_in_L = N - current_count
            current_used = [0]*5
            current_rem = 0
            
            for pos in range(L - 1):
                power = pow10mod7[L - 1 - pos]
                
                accepted = False
                for d_idx in range(5):
                    d = DIGITS[d_idx]
                    ways = 0
                    
                    current_used[d_idx] += 1
                    next_rem = (current_rem + d * power) % 7
                    
                    term = (next_rem + 5) % 7
                    needed_suffix_rem = (-term * 5) % 7
                    if needed_suffix_rem < 0:
                        needed_suffix_rem += 7
                        
                    for T in all_tuples:
                        s = sum(T[k]*DIGITS[k] for k in range(5))
                        if s % 3 != 0:
                            continue
                            
                        possible = True
                        suffix_counts = [0]*5
                        for k in range(5):
                            needed = T[k] - current_used[k]
                            if k == 2:
                                needed -= 1
                            if needed < 0:
                                possible = False
                                break
                            suffix_counts[k] = needed
                            
                        if not possible:
                            continue
                            
                        c_rems = get_rem_counts(tuple(suffix_counts))
                        ways += c_rems[needed_suffix_rem]
                        
                    if target_in_L <= ways:
                        res += str(d)
                        current_rem = next_rem
                        accepted = True
                        break
                    else:
                        target_in_L -= ways
                        current_used[d_idx] -= 1
                        
                if not accepted:
                    return "ERROR"
            
            res += "5"
            return res
            
        else:
            current_count += count_for_L
            L += 2

def solve():
    return find_nth(10000000000000000)

if __name__ == "__main__":
    assert find_nth(1) == "1117935"
    print(solve())
