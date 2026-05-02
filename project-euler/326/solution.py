def count_pairs(n_limit=1000000000000, m_val=1000000):
    period = 6 * m_val
    full_cycles = n_limit // period
    remainder = n_limit % period
    
    freq_in_period = [0] * m_val
    freq_in_tail = [0] * m_val
    
    weighted_sum = 0
    prefix_mod = 0
    
    for n in range(period):
        freq_in_period[prefix_mod] += 1
        if n <= remainder:
            freq_in_tail[prefix_mod] += 1
            
        idx = n + 1
        a = 1 if idx == 1 else weighted_sum % idx
            
        weighted_sum += idx * a
        prefix_mod = (prefix_mod + a % m_val) % m_val
        
    answer = 0
    for r in range(m_val):
        count = full_cycles * freq_in_period[r] + freq_in_tail[r]
        answer += count * (count - 1) // 2
        
    return str(answer)

def solve():
    return count_pairs()

if __name__ == '__main__':
    print(solve())
