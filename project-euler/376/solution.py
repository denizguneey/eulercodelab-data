def solve():
    transitions = [[] for _ in range(343)]
    for used_a in range(7):
        for used_b in range(7):
            for used_c in range(7):
                idx = (used_a * 7 + used_b) * 7 + used_c
                for add_a in range(7 - used_a):
                    new_a = used_a + add_a
                    for add_b in range(7 - used_b):
                        new_b = used_b + add_b
                        for add_c in range(7 - used_c):
                            transitions[idx].append((
                                new_a, new_b, used_c + add_c,
                                add_b * used_a,
                                add_c * used_b,
                                add_a * used_c
                            ))
                            
    n = 30
    current = {0: 1}
    
    for value in range(1, n + 1):
        next_states = {}
        values_left_after = n - value
        
        for key, ways in current.items():
            used_a = key & 7
            used_b = (key >> 3) & 7
            used_c = (key >> 6) & 7
            w_ba = (key >> 9) & 31
            w_cb = (key >> 14) & 31
            w_ac = (key >> 19) & 31
            
            idx = (used_a * 7 + used_b) * 7 + used_c
            
            for tr in transitions[idx]:
                n_a, n_b, n_c, ad_ba, ad_cb, ad_ac = tr
                
                if values_left_after == 0 and (n_a != 6 or n_b != 6 or n_c != 6):
                    continue
                    
                nw_ba = w_ba + ad_ba
                nw_cb = w_cb + ad_cb
                nw_ac = w_ac + ad_ac
                
                if nw_ba > 19: nw_ba = 19
                if nw_cb > 19: nw_cb = 19
                if nw_ac > 19: nw_ac = 19
                
                if nw_ba + (6 - n_b) * 6 < 19: continue
                if nw_cb + (6 - n_c) * 6 < 19: continue
                if nw_ac + (6 - n_a) * 6 < 19: continue
                
                nkey = n_a | (n_b << 3) | (n_c << 6) | (nw_ba << 9) | (nw_cb << 14) | (nw_ac << 19)
                next_states[nkey] = next_states.get(nkey, 0) + ways
                
        current = next_states
        
    terminal = 6 | (6 << 3) | (6 << 6) | (19 << 9) | (19 << 14) | (19 << 19)
    ans = current.get(terminal, 0) // 3
    return str(ans)

if __name__ == '__main__':
    print(solve())
