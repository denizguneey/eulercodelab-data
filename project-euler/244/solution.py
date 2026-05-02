from collections import deque

MOD = 100000007
ASCII_L = 76
ASCII_R = 82
ASCII_U = 85
ASCII_D = 68

START_BOARD = "WRBBRRBBRRBBRRBB"
TARGET_BOARD = "WBRBBRBRRBRBBRBR"

def encode_board(board):
    if len(board) != 16:
        return 0
    s = 0
    for i, char in enumerate(board):
        val = 0
        if char == 'R': val = 1
        elif char == 'B': val = 2
        s |= (val << (2 * i))
    return s

def get_cell(s, idx):
    return (s >> (2 * idx)) & 3

def set_cell(s, idx, val):
    mask = 3 << (2 * idx)
    s &= ~mask
    s |= (val << (2 * idx))
    return s

def find_blank(s):
    for i in range(16):
        if get_cell(s, i) == 0:
            return i
    return -1

def generate_moves(s):
    blank = find_blank(s)
    r = blank // 4
    c = blank % 4
    moves = []
    
    # L: tile moves left => blank moves right
    if c < 3:
        n_blank = blank + 1
        tile = get_cell(s, n_blank)
        ns = set_cell(s, blank, tile)
        ns = set_cell(ns, n_blank, 0)
        moves.append((ns, ASCII_L))
        
    # R: tile moves right => blank moves left
    if c > 0:
        n_blank = blank - 1
        tile = get_cell(s, n_blank)
        ns = set_cell(s, blank, tile)
        ns = set_cell(ns, n_blank, 0)
        moves.append((ns, ASCII_R))
        
    # U: tile moves up => blank moves down
    if r < 3:
        n_blank = blank + 4
        tile = get_cell(s, n_blank)
        ns = set_cell(s, blank, tile)
        ns = set_cell(ns, n_blank, 0)
        moves.append((ns, ASCII_U))
        
    # D: tile moves down => blank moves up
    if r > 0:
        n_blank = blank - 4
        tile = get_cell(s, n_blank)
        ns = set_cell(s, blank, tile)
        ns = set_cell(ns, n_blank, 0)
        moves.append((ns, ASCII_D))
        
    return moves

def build_solver_data(start_state, target_state):
    states = [start_state]
    id_of = {start_state: 0}
    dist_from_start = [0]
    
    queue = [0]
    while queue:
        curr_queue = []
        for v in queue:
            s = states[v]
            for ns, ascii_code in generate_moves(s):
                if ns not in id_of:
                    nid = len(states)
                    id_of[ns] = nid
                    states.append(ns)
                    dist_from_start.append(dist_from_start[v] + 1)
                    curr_queue.append(nid)
        queue = curr_queue
                    
    target_id = id_of.get(target_state, -1)
    if target_id == -1:
        return None
        
    adjacency = [[] for _ in range(len(states))]
    for i, s in enumerate(states):
        for ns, ascii_code in generate_moves(s):
            adjacency[i].append((id_of[ns], ascii_code))
            
    dist_to_target = [-1] * len(states)
    dist_to_target[target_id] = 0
    
    queue = [target_id]
    while queue:
        curr_queue = []
        for v in queue:
            nd = dist_to_target[v] + 1
            # Inverse adjacency is same structure, but we can do a backwards BFS using standard transitions from all nodes?
            # Actually, standard transitions are reversible. Tile moves L means it can move R to go back.
            s = states[v]
            for ns, _ in generate_moves(s):
                to = id_of[ns]
                if dist_to_target[to] == -1:
                    dist_to_target[to] = nd
                    curr_queue.append(to)
        queue = curr_queue
                    
    return adjacency, dist_from_start, dist_to_target, target_id, dist_from_start[target_id]

def solve():
    start_state = encode_board(START_BOARD)
    target_state = encode_board(TARGET_BOARD)
    
    data = build_solver_data(start_state, target_state)
    if not data: return "0"
    
    adjacency, dist_from_start, dist_to_target, target_id, shortest_len = data
    
    checksum_sum = 0
    path_count = 0
    
    # Simple DFS iteration
    stack = [(0, 0, 0)] # node, depth, checksum
    
    while stack:
        node, depth, checksum = stack.pop()
        
        if depth == shortest_len:
            if node == target_id:
                path_count += 1
                checksum_sum += checksum
            continue
            
        for to, ascii_code in adjacency[node]:
            if dist_from_start[to] == depth + 1 and dist_to_target[to] == shortest_len - dist_from_start[to]:
                ncs = (checksum * 243 + ascii_code) % MOD
                stack.append((to, depth + 1, ncs))
                
    return str(checksum_sum)

if __name__ == '__main__':
    print(solve())
