def multiset_weighted_count(counts_by_size, child_count, size_sum):
    dp = [[0] * (size_sum + 1) for _ in range(child_count + 1)]
    dp[0][0] = 1
    
    for s in range(1, size_sum + 1):
        c = counts_by_size[s]
        if c == 0:
            continue
            
        q_max = min(child_count, size_sum // s)
        choose = [0] * (q_max + 1)
        choose[0] = 1
        for q in range(1, q_max + 1):
            choose[q] = choose[q - 1] * (c + q - 1) // q
            
        nxt = [row[:] for row in dp]
        for used in range(child_count + 1):
            for w in range(size_sum + 1):
                base = dp[used][w]
                if base == 0:
                    continue
                for q in range(1, q_max + 1):
                    n_used = used + q
                    n_w = w + q * s
                    if n_used > child_count or n_w > size_sum:
                        break
                    nxt[n_used][n_w] += base * choose[q]
        dp = nxt
        
    return dp[child_count][size_sum]

def compute_peerless_unrooted(N):
    planted = [[0] * (N + 1) for _ in range(N + 1)]
    planted_total_by_size = [0] * (N + 1)
    
    for n in range(1, N + 1):
        for d in range(1, n + 1):
            child_count = d - 1
            child_size_sum = n - 1
            if child_count > child_size_sum:
                continue
                
            allowed_by_size = [0] * n
            for s in range(1, n):
                allowed_by_size[s] = planted_total_by_size[s] - planted[d][s]
            planted[d][n] = multiset_weighted_count(allowed_by_size, child_count, child_size_sum)
            
        total = 0
        for d in range(1, n + 1):
            total += planted[d][n]
        planted_total_by_size[n] = total
        
    vertex_rooted = [0] * (N + 1)
    for n in range(1, N + 1):
        total = 0
        for d in range(1, n + 1):
            child_count = d
            child_size_sum = n - 1
            if child_count > child_size_sum:
                continue
                
            allowed_by_size = [0] * n
            for s in range(1, n):
                allowed_by_size[s] = planted_total_by_size[s] - planted[d][s]
            total += multiset_weighted_count(allowed_by_size, child_count, child_size_sum)
        vertex_rooted[n] = total
        
    peerless_unrooted = [0] * (N + 1)
    for n in range(1, N + 1):
        directed_edge_rooted = 0
        for left in range(1, n):
            right = n - left
            directed_edge_rooted += planted_total_by_size[left] * planted_total_by_size[right]
            
        same_degree = 0
        for d in range(1, N + 1):
            for left in range(1, n):
                right = n - left
                same_degree += planted[d][left] * planted[d][right]
                
        directed_edge_rooted -= same_degree
        peerless_unrooted[n] = vertex_rooted[n] - directed_edge_rooted // 2
        
    return peerless_unrooted

def prefix_sum_from_3(values, N):
    total = 0
    for n in range(3, N + 1):
        total += values[n]
    return total

def solve():
    peerless = compute_peerless_unrooted(50)
    ans = prefix_sum_from_3(peerless, 50)
    return str(ans)

if __name__ == "__main__":
    print(solve())
