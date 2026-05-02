import sys

TARGET_N = 1_000_000_000_000_000_000
CYCLE_START = 512
CYCLE_BANANAS = 71
CYCLE_SHIFT = 118
CHECK_LIMIT = 10_000


class Simulator:
    def __init__(self, max_target):
        self.offset = 20 * max_target + 10_000
        self.occupied = [False] * (2 * self.offset + 10)
        self.x = 0
        self.line_count = 0

    def _index(self, position):
        idx = position + self.offset
        assert 0 <= idx < len(self.occupied)
        return idx

    def _has(self, position):
        return self.occupied[self._index(position)]

    def _set(self, position):
        idx = self._index(position)
        assert not self.occupied[idx]
        self.occupied[idx] = True
        self.line_count += 1

    def _clear(self, position):
        idx = self._index(position)
        assert self.occupied[idx]
        self.occupied[idx] = False
        self.line_count -= 1

    def first_positions(self, max_target):
        first = [0] * (max_target + 1)
        filled = -1

        while filled < max_target:
            here = self._has(self.x)
            nxt = self._has(self.x + 1)

            if here and nxt:
                self._clear(self.x + 1)
                self.x -= 1
            elif here:
                self._clear(self.x)
                self.x += 2
            elif nxt:
                self._clear(self.x + 1)
                self._set(self.x)
                self.x += 2
            else:
                stop = min(self.line_count, max_target)
                while filled < stop:
                    filled += 1
                    first[filled] = self.x

                assert not self._has(self.x - 1)
                assert not self._has(self.x)
                assert not self._has(self.x + 1)
                self._set(self.x - 1)
                self._set(self.x)
                self._set(self.x + 1)
                self.x -= 2

        return first


def bb(n, first):
    target = 0 if n <= 2 else n - 2
    if target < len(first):
        return first[target]

    cycles = (target - CYCLE_START) // CYCLE_BANANAS
    residue = CYCLE_START + (target - CYCLE_START) % CYCLE_BANANAS
    return first[residue] + cycles * CYCLE_SHIFT


def run_checkpoints(first):
    assert bb(0, first) == 0
    assert bb(1, first) == 0
    assert bb(2, first) == 0
    assert bb(3, first) == 1
    assert bb(5, first) == -1
    assert bb(1000, first) == 1499

    for m in range(CYCLE_START, CHECK_LIMIT - CYCLE_BANANAS + 1):
        assert first[m + CYCLE_BANANAS] == first[m] + CYCLE_SHIFT


def main(argv=None):
    argv = sys.argv if argv is None else argv
    should_run_checkpoints = True

    for arg in argv[1:]:
        if arg == "--skip-checkpoints":
            should_run_checkpoints = False
            continue
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return 1

    simulator = Simulator(CHECK_LIMIT)
    first = simulator.first_positions(CHECK_LIMIT)

    if should_run_checkpoints:
        run_checkpoints(first)

    print(bb(TARGET_N, first))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
