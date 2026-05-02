import sys

def sorted_digits(value):
    return ''.join(sorted(str(value)))

def solve(max_multiplier):
    x = 1
    while True:
        signature = sorted_digits(x)
        ok = True
        for k in range(2, max_multiplier + 1):
            if sorted_digits(k * x) != signature:
                ok = False
                break
        if ok:
            return x
        x += 1

def run_checkpoints():
    if sorted_digits(125874) != sorted_digits(251748):
        sys.stderr.write("Checkpoint failed for 125874\n")
        return False
    return True

def parse_arguments(args):
    max_multiplier = 6
    run_checkpoints_flag = True
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
            i += 1
            continue
        
        if arg.startswith("--max-multiplier="):
            try:
                value_str = arg[len("--max-multiplier="):]
                if not value_str:
                    return None, False
                max_multiplier = int(value_str)
                i += 1
                continue
            except ValueError:
                return None, False
        
        sys.stderr.write(f"Unknown argument: {arg}\n")
        return None, False
    
    if max_multiplier < 2:
        return None, False
    
    return {"max_multiplier": max_multiplier, "run_checkpoints": run_checkpoints_flag}, True

def main():
    args = sys.argv[1:]
    
    options, success = parse_arguments(args)
    if not success:
        sys.exit(1)
    
    if options["run_checkpoints"] and not run_checkpoints():
        sys.exit(2)
    
    result = solve(options["max_multiplier"])
    print(result)

if __name__ == "__main__":
    main()
