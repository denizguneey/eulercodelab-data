def reverse_suffix(s, idx):
    return s[:idx] + s[idx:][::-1]

def generate_maximix_arrangements(n):
    start = "".join(chr(ord('A') + i) for i in range(n))
    states = [start]
    
    states = [reverse_suffix(s, n - 2) for s in states]
    
    for i in range(n - 3, -1, -1):
        nxt = []
        for after in states:
            after_ri = reverse_suffix(after, i)
            for p in range(i + 1, n - 1):
                before = reverse_suffix(after_ri, p)
                nxt.append(before)
        states = nxt
        
    states.sort()
    return states

def solve():
    mm11 = generate_maximix_arrangements(11)
    if len(mm11) > 2010:
        return mm11[2010]
    return ""

if __name__ == '__main__':
    print(solve())
