import sys

def polygonal(type_, n):
    if type_ == 3:
        return n * (n + 1) // 2
    elif type_ == 4:
        return n * n
    elif type_ == 5:
        return n * (3 * n - 1) // 2
    elif type_ == 6:
        return n * (2 * n - 1)
    elif type_ == 7:
        return n * (5 * n - 3) // 2
    elif type_ == 8:
        return n * (3 * n - 2)
    else:
        return -1

def generate_four_digit_values(type_):
    values = []
    n = 1
    while True:
        x = polygonal(type_, n)
        if x > 9999:
            break
        if x >= 1000:
            value = int(x)
            prefix = value // 100
            suffix = value % 100
            if prefix >= 10 and suffix >= 10:
                values.append(value)
        n += 1
    return values

def solve():
    types = [3, 4, 5, 6, 7, 8]
    nums = [generate_four_digit_values(t) for t in types]
    
    chosen_values = []
    chosen_types = []
    answer = -1
    
    def dfs(suffix_needed, used_mask, first_prefix, current_sum):
        nonlocal answer
        if answer != -1:
            return
        if len(chosen_values) == 6:
            if suffix_needed == first_prefix:
                answer = current_sum
            return
        
        for t in range(6):
            if (used_mask >> t) & 1:
                continue
            
            for value in nums[t]:
                prefix = value // 100
                suffix = value % 100
                
                if chosen_values and prefix != suffix_needed:
                    continue
                
                chosen_values.append(value)
                chosen_types.append(t)
                
                next_first_prefix = prefix if len(chosen_values) == 1 else first_prefix
                dfs(suffix, used_mask | (1 << t), next_first_prefix, current_sum + value)
                
                chosen_types.pop()
                chosen_values.pop()
    
    dfs(-1, 0, -1, 0)
    return answer

def main():
    args = sys.argv[1:]
    run_checkpoints_flag = True
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if run_checkpoints_flag:
        # Checkpoint validation
        if polygonal(3, 45) != 1035 or polygonal(8, 19) != 1045:
            print("Checkpoint failed for polygonal formulas", file=sys.stderr)
            sys.exit(2)
    
    print(solve())

if __name__ == "__main__":
    main()
