# Problem 145: How many reversible numbers are there below one-billion?
# Digit-pair DFS approach: for n-digit numbers, pair digits from outside in.

def solve():
    # Counts for digit pair sums
    outer = [0] * 19  # first/last digit (1-9 each, no leading zeros)
    inner = [0] * 19  # inner digit pairs (0-9 each)
    for a in range(1, 10):
        for b in range(1, 10):
            outer[a + b] += 1
    for a in range(10):
        for b in range(10):
            inner[a + b] += 1
    
    total = 0
    for length in range(2, 10):  # up to 9 digits (< 10^9)
        half = length // 2
        
        def dfs(idx, weight, sums):
            nonlocal total
            if idx == half:
                # Check all digit sums with carries
                if length % 2 == 0:
                    check(sums, 0, weight, length)
                else:
                    for mid in range(10):
                        check(sums, 2 * mid, weight, length)
                return
            
            cnt = outer if idx == 0 else inner
            for s in range(19):
                if cnt[s] == 0: continue
                dfs(idx + 1, weight * cnt[s], sums + [s])
        
        def check(sums, center_twice, weight, ln):
            nonlocal total
            carry = 0
            for i in range(ln):
                if ln % 2 == 1 and i == half:
                    pair_sum = center_twice
                else:
                    idx = i if i < half else (ln - 1 - i)
                    pair_sum = sums[idx]
                digit = (pair_sum + carry) % 10
                if digit % 2 == 0:
                    return
                carry = (pair_sum + carry) // 10
            if carry > 1:
                return
            total += weight
        
        dfs(0, 1, [])
    
    print(total)

solve()
