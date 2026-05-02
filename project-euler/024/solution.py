import sys
from typing import List, Tuple


def factorial(n: int) -> int:
    value = 1
    for k in range(2, n + 1):
        if value > sys.maxsize // k:
            raise OverflowError("factorial overflow")
        value *= k
    return value


def nth_lexicographic_permutation(digits: str, index_one_based: int) -> str:
    sorted_digits = sorted(digits)
    n = len(sorted_digits)

    total = factorial(n)
    if index_one_based < 1 or index_one_based > total:
        raise RuntimeError("Permutation index out of range")

    rank = index_one_based - 1
    answer = []
    pool = list(sorted_digits)

    for remaining in range(n, 0, -1):
        block = factorial(remaining - 1)
        pick = rank // block
        rank %= block

        answer.append(pool[pick])
        del pool[pick]

    return ''.join(answer)


def solve(index: int, digits: str) -> str:
    return nth_lexicographic_permutation(digits, index)


def run_checkpoints() -> bool:
    if nth_lexicographic_permutation("012", 1) != "012":
        return False
    if nth_lexicographic_permutation("012", 6) != "210":
        return False
    return True


def parse_arguments(args: List[str]) -> Tuple[int, str, bool]:
    index = 1000000
    digits = "0123456789"
    run_checkpoints_flag = True

    i = 1
    while i < len(args):
        arg = args[i]

        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
            i += 1
            continue

        if arg.startswith("--index="):
            try:
                index = int(arg[8:])
                if index < 1:
                    raise ValueError()
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
            i += 1
            continue

        if arg.startswith("--digits="):
            digits = arg[9:]
            if not digits:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
            i += 1
            continue

        print(f"Unknown argument: {arg}", file=sys.stderr)
        sys.exit(1)

    if index < 1 or not digits:
        print("Invalid arguments", file=sys.stderr)
        sys.exit(1)

    return index, digits, run_checkpoints_flag


def main():
    args = sys.argv[1:]
    
    index, digits, run_checkpoints_flag = parse_arguments(args)

    if run_checkpoints_flag and not run_checkpoints():
        print("Checkpoint failed", file=sys.stderr)
        sys.exit(2)

    try:
        result = solve(index, digits)
        print(result)
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
