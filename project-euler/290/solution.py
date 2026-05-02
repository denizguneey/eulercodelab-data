def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def solve(digits=18, multiplier=137):
    kOffset = 500
    dp = {0 * 1000 + kOffset: 1}
    
    for _ in range(digits):
        nxt = {}
        for key, ways in dp.items():
            carry = key // 1000
            diff = (key % 1000) - kOffset
            for d in range(10):
                t = multiplier * d + carry
                out_digit = t % 10
                next_carry = t // 10
                next_diff = diff + d - out_digit
                next_key = next_carry * 1000 + (next_diff + kOffset)
                nxt[next_key] = nxt.get(next_key, 0) + ways
        dp = nxt
        
    answer = 0
    for key, ways in dp.items():
        carry = key // 1000
        diff = (key % 1000) - kOffset
        if diff == digit_sum(carry):
            answer += ways
            
    return str(answer)

if __name__ == '__main__':
    print(solve())
