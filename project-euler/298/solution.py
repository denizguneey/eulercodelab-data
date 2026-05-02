from collections import deque

def apply_call_in_place(state, called_label, capacity):
    l_size, r_size, l_arr, r_arr = state
    l_arr = list(l_arr)
    r_arr = list(r_arr)
    
    larry_hit = False
    robin_hit = False
    delta = 0
    
    if called_label in l_arr:
        larry_hit = True
        delta += 1
        l_arr.remove(called_label)
        l_arr.append(called_label)
    else:
        if len(l_arr) < capacity:
            l_arr.append(called_label)
        else:
            l_arr.pop(0)
            l_arr.append(called_label)
            
    if called_label in r_arr:
        robin_hit = True
        delta -= 1
    else:
        if len(r_arr) < capacity:
            r_arr.append(called_label)
        else:
            r_arr.pop(0)
            r_arr.append(called_label)
            
    return (len(l_arr), len(r_arr), tuple(l_arr), tuple(r_arr)), delta

def canonicalize_state(state):
    l_size, r_size, l_arr, r_arr = state
    remap = {}
    next_id = 0
    
    new_l = []
    for x in l_arr:
        if x not in remap:
            remap[x] = next_id
            next_id += 1
        new_l.append(remap[x])
        
    new_r = []
    for x in r_arr:
        if x not in remap:
            remap[x] = next_id
            next_id += 1
        new_r.append(remap[x])
        
    return (l_size, r_size, tuple(new_l), tuple(new_r))

def build_graph(alphabet, capacity):
    states = []
    transitions = []
    id_by_state = {}
    
    initial = (0, 0, (), ())
    canonical_initial = canonicalize_state(initial)
    id_by_state[canonical_initial] = 0
    states.append(canonical_initial)
    transitions.append([])
    
    queue = deque([0])
    
    while queue:
        u = queue.popleft()
        state = states[u]
        l_size, r_size, l_arr, r_arr = state
        
        present = set(l_arr) | set(r_arr)
        known_labels = list(present)
        outside_count = alphabet - len(known_labels)
        
        out_transitions = {}
        
        for called in known_labels:
            next_state, delta = apply_call_in_place(state, called, capacity)
            can = canonicalize_state(next_state)
            
            if can not in id_by_state:
                id_by_state[can] = len(states)
                states.append(can)
                transitions.append([])
                queue.append(id_by_state[can])
                
            nxt_id = id_by_state[can]
            key = (nxt_id, delta)
            out_transitions[key] = out_transitions.get(key, 0) + 1
            
        if outside_count > 0:
            representative = -1
            for x in range(alphabet):
                if x not in present:
                    representative = x
                    break
                    
            next_state, delta = apply_call_in_place(state, representative, capacity)
            can = canonicalize_state(next_state)
            
            if can not in id_by_state:
                id_by_state[can] = len(states)
                states.append(can)
                transitions.append([])
                queue.append(id_by_state[can])
                
            nxt_id = id_by_state[can]
            key = (nxt_id, delta)
            out_transitions[key] = out_transitions.get(key, 0) + outside_count
            
        transitions[u] = [(nxt, delta, weight) for ((nxt, delta), weight) in out_transitions.items()]
        
    return states, transitions

def solve_exact(states, transitions, alphabet, turns):
    state_count = len(states)
    width = 2 * turns + 1
    offset = turns
    
    current = [0.0] * (state_count * width)
    next_probs = [0.0] * (state_count * width)
    
    current[offset] = 1.0
    
    for turn in range(1, turns + 1):
        for i in range(len(next_probs)):
            next_probs[i] = 0.0
            
        d_prev_min = offset - (turn - 1)
        d_prev_max = offset + (turn - 1)
        
        for sid in range(state_count):
            src_base = sid * width
            
            for nxt, delta, weight in transitions[sid]:
                p = weight / float(alphabet)
                dst_base = nxt * width
                
                for d in range(d_prev_min, d_prev_max + 1):
                    prob = current[src_base + d]
                    if prob == 0.0:
                        continue
                        
                    nd = d + delta
                    next_probs[dst_base + nd] += prob * p
                    
        current, next_probs = next_probs, current
        
    expectation = 0.0
    for sid in range(state_count):
        base = sid * width
        for i in range(width):
            p = current[base + i]
            if p > 0.0:
                diff = i - offset
                expectation += p * abs(diff)
                
    return expectation

def solve():
    alphabet = 10
    capacity = 5
    turns = 50
    states, transitions = build_graph(alphabet, capacity)
    ans = solve_exact(states, transitions, alphabet, turns)
    return "{:.15f}".format(ans)

if __name__ == '__main__':
    print(solve())
