def solve(n=10):
    bit_mask = (1 << n) - 1
    dp = {0: 1}
    transition_cache = {}
    
    def options_for_cell(c, occ, last_row):
        options = []
        bit = 1 << c
        if occ & bit:
            options.append((0, 0, 0))
            return options
            
        if c + 1 < n and (occ & (1 << (c + 1))) == 0:
            options.append((1, bit | (1 << (c + 1)), 0))
            
        if not last_row:
            options.append((2, bit, bit))
            
        return options
        
    def get_transitions(in1, in2, last_row):
        key = in1 | (in2 << n) | (int(last_row) << 24)
        if key in transition_cache:
            return transition_cache[key]
            
        accum = {}
        
        def dfs(c, occ1, occ2, out1, out2):
            if c == n:
                out_state = out1 | (out2 << n)
                accum[out_state] = accum.get(out_state, 0) + 1
                return
                
            ops1 = options_for_cell(c, occ1, last_row)
            ops2 = options_for_cell(c, occ2, last_row)
            
            for mt1, m1_occ, m1_out in ops1:
                for mt2, m2_occ, m2_out in ops2:
                    if mt1 == 1 and mt2 == 1: continue
                    if mt1 == 2 and mt2 == 2: continue
                    
                    dfs(c + 1, occ1 | m1_occ, occ2 | m2_occ, out1 | m1_out, out2 | m2_out)
                    
        dfs(0, in1, in2, 0, 0)
        items = list(accum.items())
        transition_cache[key] = items
        return items

    for row in range(n):
        last_row = (row == n - 1)
        next_dp = {}
        for state, ways in dp.items():
            in1 = state & bit_mask
            in2 = (state >> n) & bit_mask
            transitions = get_transitions(in1, in2, last_row)
            
            for out_state, ways_add in transitions:
                next_dp[out_state] = next_dp.get(out_state, 0) + ways * ways_add
                
        dp = next_dp
        
    return str(dp.get(0, 0))

if __name__ == '__main__':
    print(solve())
