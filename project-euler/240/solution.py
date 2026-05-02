def build_binom(n):
    c = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        c[i][0] = 1
        c[i][i] = 1
        for j in range(1, i):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
    return c

def solve(num_dice=20, max_points=12, top_count=10, top_sum=70):
    choose = build_binom(num_dice)
    
    dp = [[[0] * (top_sum + 1) for _ in range(top_count + 1)] for _ in range(num_dice + 1)]
    dp[num_dice][0][0] = 1
    
    for face in range(max_points, 0, -1):
        next_dp = [[[0] * (top_sum + 1) for _ in range(top_count + 1)] for _ in range(num_dice + 1)]
        
        for rem in range(num_dice + 1):
            for filled in range(top_count + 1):
                for current_sum in range(top_sum + 1):
                    ways = dp[rem][filled][current_sum]
                    if ways == 0:
                        continue
                        
                    for count in range(rem + 1):
                        add_top = min(count, top_count - filled)
                        new_filled = filled + add_top
                        new_sum = current_sum + add_top * face
                        
                        if new_sum > top_sum:
                            continue
                            
                        comb = choose[rem][count]
                        next_dp[rem - count][new_filled][new_sum] += ways * comb
                        
        dp = next_dp
        
    return str(dp[0][top_count][top_sum])

if __name__ == '__main__':
    print(solve())
