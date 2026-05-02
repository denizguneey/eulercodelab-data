def strong_repunits_below(limit):
    values = set()
    if limit > 1:
        values.add(1)
        
    base = 2
    while True:
        square = base * base
        if 1 + base + square >= limit:
            break
            
        repunit = 1 + base + square
        while repunit < limit:
            values.add(repunit)
            if repunit > (limit - 1) // base:
                break
            repunit = repunit * base + 1
            
        base += 1
        
    return sorted(list(values))

def solve():
    limit = 1000000000000
    values = strong_repunits_below(limit)
    ans = sum(values)
    return str(ans)

if __name__ == '__main__':
    print(solve())
