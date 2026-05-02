def solve():
    limit = 1000000000000
    
    # Precompute powers of 3
    pow3 = [1] * 65
    for i in range(1, 65):
        pow3[i] = pow3[i-1] * 3
        
    def weighted_popcount_prefix_sum(n):
        result = 0
        ones_so_far = 0
        
        for bit in range(63, -1, -1):
            if ((n >> bit) & 1) == 0:
                continue
                
            result += (1 << ones_so_far) * pow3[bit]
            ones_so_far += 1
            
        result += (1 << ones_so_far)
        return result
        
    m_max = (limit - 1) // 2
    t_max = m_max // 2
    
    ans = weighted_popcount_prefix_sum(t_max)
    return str(ans)

if __name__ == '__main__':
    print(solve())
