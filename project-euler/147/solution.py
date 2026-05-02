import sys

def solve(width, height):
    n = min(width, height)
    m = max(width, height)

    answer = (n * (n + 1) * (n + 2) // 6) * (m * (m + 1) * (m + 2) // 6)

    shift = m + 3
    dim = 2 * shift + 2
    grid = [[0] * dim for _ in range(dim)]

    for i in range(2 * n + 1):
        for j in range(2 * m + 1):
            if ((i + j) & 1) != 0:
                continue
            x = (i + j) // 2
            y = (i + 2 * shift - j) // 2
            grid[x + 1][y + 1] = 1

    for i in range(1, dim):
        for j in range(1, dim):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

    for lx in range(1, dim):
        for rx in range(lx + 1, dim):
            for ly in range(1, dim):
                for ry in range(ly + 1, dim):
                    area = (rx - lx + 1) * (ry - ly + 1)
                    full = grid[rx][ry] - grid[rx][ly - 1] - grid[lx - 1][ry] + grid[lx - 1][ly - 1]
                    if full != area:
                        continue

                    mi = (rx + ry - shift - 1) // 2
                    mj = (rx - ly + shift + 1) // 2
                    if mi < 1 or mj < 1 or mi > n or mj > m:
                        continue
                    answer += (n - mi + 1) * (m - mj + 1)

    return answer

def run_checkpoints():
    if solve(3, 2) != 72:
        return False
    return True

def parse_arguments(args):
    options = {
        'width': 47,
        'height': 43,
        'run_checkpoints': True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == '--skip-checkpoints':
            options['run_checkpoints'] = False
            i += 1
            continue
        
        if arg.startswith('--width='):
            try:
                value = int(arg[8:])
                options['width'] = value
                i += 1
                continue
            except ValueError:
                return None, "Invalid width value"
        
        if arg.startswith('--height='):
            try:
                value = int(arg[9:])
                options['height'] = value
                i += 1
                continue
            except ValueError:
                return None, "Invalid height value"
        
        return None, f"Unknown argument: {arg}"
    
    if options['width'] < 1 or options['height'] < 1:
        return None, "Width and height must be at least 1"
    
    return options, None

def main():
    args = sys.argv[1:]
    options, error = parse_arguments(args)
    
    if error:
        print(error, file=sys.stderr)
        sys.exit(1)
    
    if options['run_checkpoints'] and not run_checkpoints():
        print("Checkpoint failed for 3x2", file=sys.stderr)
        sys.exit(2)
    
    print(solve(options['width'], options['height']))

if __name__ == '__main__':
    main()
