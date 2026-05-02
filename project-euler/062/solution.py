import sys
from collections import defaultdict


def solve(family_size):
    groups = defaultdict(list)
    current_digits = 1
    n = 1
    
    while True:
        cube = n * n * n
        digits = len(str(cube))
        
        if digits != current_digits:
            best = -1
            for vec in groups.values():
                if len(vec) == family_size:
                    candidate = min(vec)
                    if best == -1 or candidate < best:
                        best = candidate
            if best != -1:
                return best
            groups.clear()
            current_digits = digits
        
        key = ''.join(sorted(str(cube)))
        groups[key].append(cube)
        n += 1


def main():
    args = sys.argv[1:]
    
    family_size = 5
    run_checkpoints = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--family-size="):
            try:
                family_size = int(arg[len("--family-size="):])
            except ValueError:
                print("Invalid argument", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if family_size < 2:
        print("Family size must be at least 2", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints:
        if solve(3) != 41063625:
            print("Checkpoint failed for family size 3", file=sys.stderr)
            sys.exit(2)
    
    print(solve(family_size))


if __name__ == "__main__":
    main()
