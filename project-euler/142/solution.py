import math
import sys

def is_square(x: int) -> bool:
    if x < 0:
        return False
    root = int(math.isqrt(x))
    return root * root == x or (root + 1) * (root + 1) == x

def solve(search_limit: int) -> int:
    for i in range(4, search_limit + 1):
        a = i * i
        for j in range(3, i):
            c = j * j
            f = a - c
            if f <= 0 or not is_square(f):
                continue
            
            kstart = 1 if (j & 1) else 2
            for k in range(kstart, j, 2):
                d = k * k
                e = a - d
                b = c - e
                
                if b <= 0 or e <= 0 or not is_square(b) or not is_square(e):
                    continue
                
                x = (d + c) // 2
                y = (e + f) // 2
                z = (c - d) // 2
                
                if not (x > y and y > z and z > 0):
                    continue
                
                if (is_square(x + y) and is_square(x - y) and
                    is_square(x + z) and is_square(x - z) and
                    is_square(y + z) and is_square(y - z)):
                    return x + y + z
    
    return 0

def main():
    args = sys.argv[1:]
    
    search_limit = 5000
    run_checkpoints = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--search-limit="):
            try:
                search_limit = int(arg[len("--search-limit="):])
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
    
    if search_limit < 4:
        sys.stderr.write("Search limit must be at least 4\n")
        sys.exit(1)
    
    if run_checkpoints:
        if solve(5000) != 1006193:
            sys.stderr.write("Checkpoint failed for search limit 5000\n")
            sys.exit(2)
    
    result = solve(search_limit)
    print(result)

if __name__ == "__main__":
    main()
