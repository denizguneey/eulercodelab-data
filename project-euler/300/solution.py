def solve():
    n = 15

    grid_side = 2 * n + 1
    offset = n

    pair_list = []
    pair_index = {}
    idx = 0
    for i in range(n):
        for j in range(i + 2, n):
            pair_index[(i, j)] = idx
            pair_list.append((i, j))
            idx += 1

    num_pairs = len(pair_list)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    contact_maps = set()

    px = [0] * n
    py = [0] * n
    occupied = bytearray(grid_side * grid_side)

    def cell_id(x, y):
        return y * grid_side + x

    def add_contact_map():
        key = 0
        for p_idx in range(num_pairs):
            i, j = pair_list[p_idx]
            manhattan = abs(px[i] - px[j]) + abs(py[i] - py[j])
            if manhattan == 1:
                key |= (1 << p_idx)
        contact_maps.add(key)

    def dfs(idx_pos):
        if idx_pos == n - 1:
            add_contact_map()
            return
        cx = px[idx_pos]
        cy = py[idx_pos]
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            cid = cell_id(nx, ny)
            if occupied[cid]:
                continue
            occupied[cid] = 1
            px[idx_pos + 1] = nx
            py[idx_pos + 1] = ny
            dfs(idx_pos + 1)
            occupied[cid] = 0

    import sys
    sys.setrecursionlimit(500000)

    x0, y0 = offset, offset
    x1, y1 = offset + 1, offset
    occupied[cell_id(x0, y0)] = 1
    occupied[cell_id(x1, y1)] = 1
    px[0] = x0; py[0] = y0
    px[1] = x1; py[1] = y1
    dfs(1)

    maps_list = list(contact_maps)

    # Build adjacency masks
    adj_masks = []
    for key in maps_list:
        adj = [0] * n
        for p_idx in range(num_pairs):
            if (key >> p_idx) & 1:
                i, j = pair_list[p_idx]
                adj[i] |= (1 << j)
                adj[j] |= (1 << i)
        adj_masks.append(adj)

    mask_count = 1 << n
    best = bytearray(mask_count)

    popcount = [0] * mask_count
    for m in range(1, mask_count):
        popcount[m] = popcount[m >> 1] + (m & 1)

    for adj in adj_masks:
        score = bytearray(mask_count)
        for mask in range(1, mask_count):
            lb = mask & (-mask)
            i = lb.bit_length() - 1
            prev = mask ^ lb
            add = popcount[prev & adj[i]]
            score[mask] = score[prev] + add
            if score[mask] > best[mask]:
                best[mask] = score[mask]

    numerator = 0
    for mask in range(mask_count):
        consecutive_hh = popcount[mask & (mask >> 1)]
        numerator += best[mask] + consecutive_hh

    # exact_average_decimal
    denominator = 1 << n
    integer_part = numerator // denominator
    rem = numerator % denominator
    result = str(integer_part)
    if rem > 0:
        result += '.'
        while rem > 0:
            rem *= 10
            digit = rem // denominator
            result += str(digit)
            rem %= denominator
    return result

if __name__ == '__main__':
    print(solve())
