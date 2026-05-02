def next_alive_after(mask, chef):
    higher_bits = mask & ~((1 << (chef + 1)) - 1)
    if higher_bits != 0:
        return (higher_bits & -higher_bits).bit_length() - 1
    return (mask & -mask).bit_length() - 1

def solve_competition(skills):
    n = len(skills)
    total_masks = 1 << n
    
    # wins[mask][turn][chef] 
    wins = [[[0.0] * n for _ in range(n)] for __ in range(total_masks)]
    dishes = [[0.0] * n for _ in range(total_masks)]
    
    masks_by_size = [[] for _ in range(n + 1)]
    for mask in range(1, total_masks):
        bits = bin(mask).count('1')
        masks_by_size[bits].append(mask)
        
    for size in range(1, n + 1):
        for mask in masks_by_size[size]:
            # find members
            members = []
            temp = mask
            while temp != 0:
                chef = (temp & -temp).bit_length() - 1
                members.append(chef)
                temp &= temp - 1
                
            m = len(members)
            if m == 1:
                chef = members[0]
                wins[mask][chef][chef] = 1.0
                dishes[mask][chef] = 0.0
                continue
                
            a_win = [[0.0] * n for _ in range(m)]
            b_array = [0.0] * m
            a_dish = [0.0] * m
            
            for t in range(m):
                current = members[t]
                p = skills[current]
                b_array[t] = 1.0 - p
                
                best_self_win = -1.0
                best_target_pos = 0
                best_distance = float('inf')
                
                for u in range(m):
                    if u == t:
                        continue
                    target = members[u]
                    next_mask = mask & ~(1 << target)
                    next_turn = next_alive_after(next_mask, current)
                    
                    self_win = wins[next_mask][next_turn][current]
                    distance = (u + m - t) % m
                    
                    if self_win > best_self_win + 1e-15 or (abs(self_win - best_self_win) <= 1e-15 and distance < best_distance):
                        best_self_win = self_win
                        best_target_pos = u
                        best_distance = distance
                        
                target = members[best_target_pos]
                next_mask = mask & ~(1 << target)
                next_turn = next_alive_after(next_mask, current)
                
                succ_row = wins[next_mask][next_turn]
                for k in range(n):
                    a_win[t][k] = p * succ_row[k]
                a_dish[t] = 1.0 + p * dishes[next_mask][next_turn]
                
            x0 = [0.0] * n
            acc = [0.0] * n
            B = b_array[0]
            
            for k in range(n):
                acc[k] = a_win[0][k]
                
            for t in range(1, m):
                for k in range(n):
                    acc[k] += B * a_win[t][k]
                B *= b_array[t]
                
            den = 1.0 - B
            for k in range(n):
                x0[k] = acc[k] / den
                
            state_wins = [[0.0] * n for _ in range(m)]
            for k in range(n):
                state_wins[0][k] = x0[k]
                state_wins[m - 1][k] = a_win[m - 1][k] + b_array[m - 1] * x0[k]
                
            for t in range(m - 2, 0, -1):
                for k in range(n):
                    state_wins[t][k] = a_win[t][k] + b_array[t] * state_wins[t + 1][k]
                    
            B_d = b_array[0]
            A_d = a_dish[0]
            for t in range(1, m):
                A_d += B_d * a_dish[t]
                B_d *= b_array[t]
            d0 = A_d / (1.0 - B_d)
            
            state_dishes = [0.0] * m
            state_dishes[0] = d0
            state_dishes[m - 1] = a_dish[m - 1] + b_array[m - 1] * d0
            for t in range(m - 2, 0, -1):
                state_dishes[t] = a_dish[t] + b_array[t] * state_dishes[t + 1]
                
            for t in range(m):
                turn = members[t]
                for k in range(n):
                    wins[mask][turn][k] = state_wins[t][k]
                dishes[mask][turn] = state_dishes[t]
                
    full_mask = total_masks - 1
    return dishes[full_mask][0]

def fibonacci_skills(n):
    fib = [0.0] * (n + 2)
    fib[1] = 1.0
    fib[2] = 1.0
    for i in range(3, n + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    skills = [0.0] * n
    for k in range(1, n + 1):
        skills[k - 1] = fib[k] / fib[n + 1]
    return skills

def solve():
    n = 14
    skills = fibonacci_skills(n)
    ans = solve_competition(skills)
    return f"{ans:.8f}"

if __name__ == '__main__':
    print(solve())
