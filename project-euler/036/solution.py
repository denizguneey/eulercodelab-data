import sys

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def to_binary(value):
    if value == 0:
        return "0"
    out = []
    while value > 0:
        out.append('1' if (value & 1) else '0')
        value >>= 1
    out.reverse()
    return ''.join(out)

def solve(limit):
    total = 0
    for n in range(1, limit):
        if is_palindrome(str(n)) and is_palindrome(to_binary(n)):
            total += n
    return total

def main():
    limit = 1000000
    run_checkpoints = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints = False
        elif arg.startswith("--limit="):
            try:
                limit = int(arg[8:])
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            sys.exit(1)
    
    if limit < 1:
        sys.exit(1)
    
    if run_checkpoints:
        if solve(1000) != 1772:
            sys.stderr.write("Checkpoint failed for limit=1000\n")
            sys.exit(2)
        if not is_palindrome("12321"):
            sys.stderr.write("Checkpoint failed for palindrome helper\n")
            sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
