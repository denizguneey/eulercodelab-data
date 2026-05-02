def solve():
    target_steps = 10**18
    detect_steps = 200_000

    # Simulate Langton's ant
    black = set()
    x, y = 0, 0
    direction = 0  # 0=up, 1=right, 2=down, 3=left
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    counts = [0] * (detect_steps + 1)
    black_count = 0

    for step in range(1, detect_steps + 1):
        key = (x, y)
        if key in black:
            black.remove(key)
            black_count -= 1
            direction = (direction + 3) & 3
        else:
            black.add(key)
            black_count += 1
            direction = (direction + 1) & 3
        x += dx[direction]
        y += dy[direction]
        counts[step] = black_count

    # Detect linear periodic pattern
    max_period = 500
    verify_window = 50_000
    total = detect_steps
    window_start = total - verify_window if total > verify_window else 0

    pattern = None
    for period in range(1, max_period + 1):
        if period > total:
            break
        delta = counts[total] - counts[total - period]
        tail_ok = True
        for t in range(window_start, total - period + 1):
            if counts[t + period] - counts[t] != delta:
                tail_ok = False
                break
        if not tail_ok:
            continue

        # Find earliest start
        upto = total - period
        for start in range(upto + 1):
            all_ok = True
            for s in range(start, upto + 1):
                if counts[s + period] - counts[s] != delta:
                    all_ok = False
                    break
            if all_ok:
                pattern = (start, period, delta)
                break
        if pattern:
            break

    if target_steps <= detect_steps:
        return str(counts[target_steps])

    start, period, delta = pattern
    offset = target_steps - start
    cycles = offset // period
    rem = offset % period
    base = counts[start + rem]
    return str(base + cycles * delta)

if __name__ == '__main__':
    print(solve())
