import sys
from multiprocessing import Pool, cpu_count
import math

def subset_best_profits_integer_costs(mask, d, max_cost):
    values = []
    for bit in range(d):
        if (mask >> bit) & 1:
            values.append(bit + 1)
            
    k = len(values)
    output = [0.0] * (max_cost + 1)
    if k == 0:
        return output
        
    max_value = values[-1]
    output[0] = float(max_value)
    
    t_limit = d
    h_prev = 0.0
    for t in range(1, t_limit + 1):
        s = 0.0
        for x in values:
            if x > h_prev:
                s += x
            else:
                s += h_prev
                
        h_cur = s / k
        for c in range(1, max_cost + 1):
            candidate = h_cur - c * t
            if candidate > output[c]:
                output[c] = candidate
        h_prev = h_cur
        
    return output

def compute_average(args):
    begin, end, d, max_cost = args
    table_size = (d + 1) * (max_cost + 1)
    partial_sum = [0.0] * table_size
    partial_count = [0] * (d + 1)
    
    for mask in range(begin, end):
        k = mask.bit_count()
        profits = subset_best_profits_integer_costs(mask, d, max_cost)
        partial_count[k] += 1
        base = k * (max_cost + 1)
        for c in range(max_cost + 1):
            partial_sum[base + c] += profits[c]
            
    return (partial_sum, partial_count)

def compute_average_reward_by_level(d, max_cost):
    total_masks = 1 << d
    threads = max(1, cpu_count())
    
    tasks = []
    chunk = (total_masks - 1 + threads - 1) // threads
    for t in range(threads):
        begin = 1 + t * chunk
        end = 1 + min(total_masks - 1, (t + 1) * chunk)
        if begin < end:
            tasks.append((begin, end, d, max_cost))
            
    with Pool(len(tasks)) as pool:
        results = pool.map(compute_average, tasks)
        
    table_size = (d + 1) * (max_cost + 1)
    global_sum = [0.0] * table_size
    global_count = [0] * (d + 1)
    
    for p_sum, p_count in results:
        for k in range(1, d + 1):
            global_count[k] += p_count[k]
        for i in range(table_size):
            global_sum[i] += p_sum[i]
            
    average = [0.0] * table_size
    for k in range(1, d + 1):
        cnt = global_count[k]
        if cnt == 0: continue
        inv_cnt = 1.0 / cnt
        base = k * (max_cost + 1)
        for c in range(max_cost + 1):
            average[base + c] = global_sum[base + c] * inv_cnt
            
    return average

def solve_super_by_cost(d, max_cost, average_reward_by_level):
    stride = max_cost + 1
    s_by_cost = [0.0] * (max_cost + 1)
    
    for c in range(max_cost + 1):
        lower = [0.0] * d
        diag = [0.0] * d
        upper = [0.0] * d
        rhs = [0.0] * d
        
        for k in range(1, d + 1):
            idx = k - 1
            a_k = average_reward_by_level[k * stride + c]
            
            if k == d:
                lower[idx] = -1.0
                diag[idx] = 1.0
                upper[idx] = 0.0
                rhs[idx] = a_k
                continue
                
            p = float(k) / float(d)
            q = 1.0 - p
            
            lower[idx] = 0.0 if k == 1 else -p
            diag[idx] = 1.0
            upper[idx] = -q
            rhs[idx] = a_k
            
        for i in range(1, d):
            factor = lower[i] / diag[i - 1]
            diag[i] -= factor * upper[i - 1]
            rhs[i] -= factor * rhs[i - 1]
            
        x = [0.0] * d
        x[d - 1] = rhs[d - 1] / diag[d - 1]
        for i in range(d - 2, -1, -1):
            x[i] = (rhs[i] - upper[i] * x[i + 1]) / diag[i]
            
        s_by_cost[c] = x[d - 1]
        
    return s_by_cost

def compute_f(n):
    total = 0.0
    for d in range(4, n + 1):
        avg = compute_average_reward_by_level(d, n)
        s = solve_super_by_cost(d, n, avg)
        for c in range(n + 1):
            total += s[c]
    return total

def solve():
    n = 20
    ans = compute_f(n)
    return str(round(ans))

if __name__ == '__main__':
    print(solve())
