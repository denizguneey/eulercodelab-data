import sys
from typing import List, Tuple


def name_value(name: str) -> int:
    value = 0
    for c in name:
        if 'A' <= c <= 'Z':
            value += ord(c) - ord('A') + 1
    return value


def score_sum(names: List[str]) -> int:
    names = sorted(names)
    
    total = 0
    for i, name in enumerate(names):
        position = i + 1
        total += position * name_value(name)
    return total


def parse_csv_names(payload: str) -> List[str]:
    names = []
    current = []
    inside_quotes = False

    for ch in payload:
        if ch == '"':
            inside_quotes = not inside_quotes
            if not inside_quotes:
                names.append(''.join(current))
                current = []
            continue
        if inside_quotes:
            current.append(ch)

    return names


def solve(names_file: str) -> int:
    try:
        with open(names_file, 'r') as input_file:
            payload = input_file.read()
    except IOError:
        raise RuntimeError(f"Could not open names file: {names_file}")
    
    return score_sum(parse_csv_names(payload))


def run_checkpoints() -> bool:
    if name_value("COLIN") != 53:
        print("Checkpoint failed for COLIN value", file=sys.stderr)
        return False

    sample = ["B", "A"]
    if score_sum(sample) != 5:
        print("Checkpoint failed for small score set", file=sys.stderr)
        return False

    return True


def main() -> None:
    args = sys.argv[1:]
    
    names_file = "resources/documents/0022_names.txt"
    run_checkpoints_flag = True
    
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
            i += 1
        elif arg.startswith("--names-file="):
            names_file = arg[len("--names-file="):]
            i += 1
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    try:
        result = solve(names_file)
        print(result)
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
