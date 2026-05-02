import sys
import os

def parse_triangle(text):
    triangle = []
    for line in text.strip().split('\n'):
        if not line.strip():
            continue
        row = list(map(int, line.split()))
        if row:
            triangle.append(row)
    return triangle

def max_path_sum(triangle):
    if not triangle:
        return 0
    
    # Work from bottom to top
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    
    return triangle[0][0]

def solve(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except IOError:
        raise RuntimeError(f"Could not open triangle file: {file_path}")
    
    return max_path_sum(parse_triangle(content))

def run_checkpoints():
    sample = "3\n7 4\n2 4 6\n8 5 9 3"
    if max_path_sum(parse_triangle(sample)) != 23:
        print("Checkpoint failed for sample triangle", file=sys.stderr)
        return False
    return True

def main():
    # Parse command line arguments
    file_path = "resources/documents/0067_triangle.txt"
    run_checkpoints_flag = True
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--file="):
            file_path = arg[7:]
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
        i += 1
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    try:
        result = solve(file_path)
        print(result)
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(3)

if __name__ == "__main__":
    main()
