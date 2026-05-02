import os

kMod = 1005075251

def min_score_for_target(target, nums):
    n = len(nums)
    all_masks = 1 << n
    
    subset_sum = [0] * all_masks
    for mask in range(1, all_masks):
        bit = (mask & -mask).bit_length() - 1
        subset_sum[mask] = subset_sum[mask & (mask - 1)] + nums[bit]
        
    vals = [set() for _ in range(all_masks)]
    
    for mask in range(1, all_masks):
        if (mask & (mask - 1)) == 0:
            bit = (mask & -mask).bit_length() - 1
            vals[mask].add(nums[bit])
            continue
            
        sub = (mask - 1) & mask
        while sub > 0:
            other = mask ^ sub
            if sub > other:
                sub = (sub - 1) & mask
                continue
                
            for a in vals[sub]:
                for b in vals[other]:
                    vals[mask].add(a + b)
                    vals[mask].add(a * b)
                    if a > b: vals[mask].add(a - b)
                    if b > a: vals[mask].add(b - a)
                    if b != 0 and a % b == 0: vals[mask].add(a // b)
                    if a != 0 and b % a == 0: vals[mask].add(b // a)
                    
            sub = (sub - 1) & mask
            
    best = float('inf')
    for mask in range(1, all_masks):
        if target in vals[mask]:
            if subset_sum[mask] < best:
                best = subset_sum[mask]
                
    if best == float('inf'):
        return 0
    return best

def solve():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, "..", "resources", "documents", "0828_number_challenges.txt")
    
    ans = 0
    p3 = 1
    
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line: continue
            col = line.find(':')
            if col == -1: continue
            
            target = int(line[:col])
            nums = [int(x) for x in line[col + 1:].split(',')]
            
            p3 = (p3 * 3) % kMod
            s = min_score_for_target(target, nums)
            ans = (ans + p3 * (s % kMod)) % kMod
            
    return str(ans)

if __name__ == "__main__":
    print(solve())
