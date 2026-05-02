def solve():
    update_memo = {}
    def get_update(rmask, t):
        key = (rmask << 4) | t
        if key in update_memo: return update_memo[key]
        
        next_mask = rmask
        for matched in range(16):
            if (rmask & (1 << matched)) == 0: continue
            available = t & (~matched)
            b = available
            while b != 0:
                isolate = b & -b
                suit_bit = isolate.bit_length() - 1
                b &= b - 1
                new_subset = matched | (1 << suit_bit)
                next_mask |= (1 << new_subset)
                
        update_memo[key] = next_mask
        return next_mask

    popcounts = [int.bit_count(t) for t in range(16)]
    
    curr = [{} for _ in range(14)]
    curr[0][1] = 1
    
    for rank in range(13):
        nxt = [{} for _ in range(14)]
        for n in range(14):
            if not curr[n]: continue
            for rmask, ways in curr[n].items():
                for t in range(16):
                    nn = n + popcounts[t]
                    if nn > 13: continue
                    nr = get_update(rmask, t)
                    nxt[nn][nr] = nxt[nn].get(nr, 0) + ways
        curr = nxt
        
    ans = 0
    for n in range(4, 14):
        total_for_n = 0
        for rmask, ways in curr[n].items():
            if (rmask & (1 << 15)) != 0:
                total_for_n += ways
        ans += total_for_n
        
    return str(ans)

if __name__ == '__main__':
    print(solve())
