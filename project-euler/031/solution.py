import sys

def solve(target):
    kCoins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1
    
    for coin in kCoins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[target]

def main():
    target = 200
    run_checkpoints = True
    
    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        
        if arg == "--skip-checkpoints":
            run_checkpoints = False
            i += 1
            continue
            
        if arg.startswith("--target="):
            try:
                value_str = arg[9:]
                if not value_str:
                    print("Unknown argument: " + arg, file=sys.stderr)
                    sys.exit(1)
                value = int(value_str)
                if value < 0:
                    print("Unknown argument: " + arg, file=sys.stderr)
                    sys.exit(1)
                target = value
                i += 1
                continue
            except ValueError:
                print("Unknown argument: " + arg, file=sys.stderr)
                sys.exit(1)
        
        print("Unknown argument: " + arg, file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints:
        if solve(5) != 4:
            print("Checkpoint failed for target=5", file=sys.stderr)
            sys.exit(2)
        if solve(10) != 11:
            print("Checkpoint failed for target=10", file=sys.stderr)
            sys.exit(2)
    
    print(solve(target))

if __name__ == "__main__":
    main()
