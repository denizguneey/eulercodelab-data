def solve():
    kMod = 10000000000000000
    n = 2020
    answer = 0
    
    for s in range(10):
        target = 2 * s
        cnt = [[0, 0] for _ in range(19)]
        sum_val = [[0, 0] for _ in range(19)]
        
        for d in range(1, 10):
            if d > target:
                break
            has = 1 if d == s else 0
            cnt[d][has] += 1
            sum_val[d][has] += d
            
        for length in range(1, n + 1):
            if target < 19:
                answer = (answer + sum_val[target][1]) % kMod
            if length == n:
                break
                
            next_cnt = [[0, 0] for _ in range(19)]
            next_sum = [[0, 0] for _ in range(19)]
            
            for current_sum in range(target + 1):
                for has in range(2):
                    c = cnt[current_sum][has]
                    if c == 0:
                        continue
                    sv = sum_val[current_sum][has]
                    
                    for d in range(10):
                        ns = current_sum + d
                        if ns > target:
                            break
                        nh = 1 if (has or d == s) else 0
                        
                        next_cnt[ns][nh] = (next_cnt[ns][nh] + c) % kMod
                        appended = (sv * 10 + c * d) % kMod
                        next_sum[ns][nh] = (next_sum[ns][nh] + appended) % kMod
                        
            cnt, sum_val = next_cnt, next_sum
            
    return str(answer)

if __name__ == "__main__":
    print(solve())
