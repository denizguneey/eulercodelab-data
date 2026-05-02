def exact_score_probability(shots, target_score, q):
    dp = [0.0] * 64
    dp[0] = 1.0
    for x in range(1, shots + 1):
        hit = 1.0 - float(x) / q
        miss = 1.0 - hit
        for s in range(x, 0, -1):
            dp[s] = dp[s] * miss + dp[s - 1] * hit
        dp[0] *= miss
    return dp[target_score]

def solve(shots=50, target_score=20, target_probability=0.02):
    low = 50.0
    high = 100.0
    while exact_score_probability(shots, target_score, high) > target_probability:
        high *= 2.0
        
    for _ in range(220):
        mid = (low + high) / 2.0
        if exact_score_probability(shots, target_score, mid) > target_probability:
            low = mid
        else:
            high = mid
            
    return f"{(low + high) / 2.0:.10f}"

if __name__ == '__main__':
    print(solve())
