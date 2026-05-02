import sys


def solve(digits):
    if digits == 1:
        return 1

    previous = 1.0
    current = 1.0
    decade = 1
    index = 1

    while decade < digits:
        previous, current = current, previous + current
        if previous >= 10.0:
            previous /= 10.0
            current /= 10.0
            decade += 1
        index += 1

    return index


def main():
    digits = 1000
    run_checkpoints_flag = True

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
            i += 1
        elif arg.startswith("--digits="):
            try:
                digits = int(arg[9:])
                if digits < 1:
                    sys.stderr.write("Invalid digits value\n")
                    return 1
                i += 1
            except ValueError:
                sys.stderr.write(f"Unknown argument: {arg}\n")
                return 1
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return 1

    if run_checkpoints_flag:
        if solve(2) != 7:
            sys.stderr.write("Checkpoint failed for digits=2\n")
            return 2
        if solve(3) != 12:
            sys.stderr.write("Checkpoint failed for digits=3\n")
            return 2
        if solve(1000) != 4782:
            sys.stderr.write("Checkpoint failed for digits=1000\n")
            return 2

    print(solve(digits))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
