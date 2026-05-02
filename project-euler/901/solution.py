import math

MAX_STEPS = 200
STOP_DEPTH = 80.0

def is_increasing(d1):
    prev = 0.0
    curr = d1
    min_diff = float('inf')
    for _ in range(MAX_STEPS):
        diff = curr - prev
        if diff <= 0.0:
            return False, diff
        if diff < min_diff:
            min_diff = diff
        if curr > STOP_DEPTH:
            break
        next_val = math.exp(curr - prev)
        prev = curr
        curr = next_val
    return True, min_diff

def is_increasing_bool(d1):
    return is_increasing(d1)[0]

def expected_cost(d1):
    prev = 0.0
    curr = d1
    sum_cost = 0.0
    for _ in range(MAX_STEPS):
        sum_cost += curr * math.exp(-prev)
        if curr > STOP_DEPTH:
            break
        next_val = math.exp(curr - prev)
        prev = curr
        curr = next_val
    return sum_cost

def find_high_threshold():
    scan_start = 0.6
    scan_end = 1.5
    scan_step = 0.01

    prev_inc = is_increasing_bool(scan_start)
    low = scan_start
    high = scan_start
    
    d = scan_start + scan_step
    while d <= scan_end + 1e-9:
        inc = is_increasing_bool(d)
        if not prev_inc and inc:
            low = d - scan_step
            high = d
            break
        prev_inc = inc
        d += scan_step

    if high == scan_start:
        return -1.0

    for _ in range(90):
        mid = (low + high) * 0.5
        if is_increasing_bool(mid):
            high = mid
        else:
            low = mid
    return high

def solve():
    d1 = find_high_threshold()
    if d1 <= 0.0:
        return "Failed"
    answer = expected_cost(d1)
    return f"{answer:.9f}"

if __name__ == "__main__":
    print(solve())
