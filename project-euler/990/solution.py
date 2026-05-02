from __future__ import annotations

import sys
from array import array


MOD = 1_000_000_007
TARGET_N = 50
MAX_TERMS = (TARGET_N + 1) // 2
DELTA_LIMIT = 25
DELTA_SIZE = 2 * DELTA_LIMIT + 1


class Options:
    __slots__ = ("run_checkpoints", "allow_multithreading", "requested_threads", "target_n")

    def __init__(self) -> None:
        self.run_checkpoints = True
        self.allow_multithreading = True
        self.requested_threads = 0
        self.target_n = TARGET_N


class Transition:
    __slots__ = ("by_residue",)

    def __init__(self) -> None:
        self.by_residue = [[] for _ in range(10)]


def mod_add(a: int, b: int) -> int:
    s = a + b
    return s - MOD if s >= MOD else s


def mod_mul(a: int, b: int) -> int:
    return (a * b) % MOD


def convolve(lhs: list[int], rhs: list[int]) -> list[int]:
    result = [0] * (len(lhs) + len(rhs) - 1)
    for i, left in enumerate(lhs):
        if left == 0:
            continue
        for j, right in enumerate(rhs):
            if right == 0:
                continue
            result[i + j] = mod_add(result[i + j], mod_mul(left, right))
    return result


def append_digit_set(poly: list[int], low_digit: int, high_digit: int) -> list[int]:
    next_poly = [0] * (len(poly) + high_digit)
    for i, coeff in enumerate(poly):
        if coeff == 0:
            continue
        for digit in range(low_digit, high_digit + 1):
            next_poly[i + digit] = mod_add(next_poly[i + digit], coeff)
    return next_poly


class Solver:
    def __init__(self, _options: Options) -> None:
        self.binom = self.build_binom()
        self.digit_sums = self.build_digit_sum_polynomials()
        self.transition_base, self.transition_count = self.build_transition_base()
        self.transitions = self.build_transitions()

    @staticmethod
    def build_binom() -> list[list[int]]:
        result = [[0] * (MAX_TERMS + 1) for _ in range(MAX_TERMS + 1)]
        result[0][0] = 1
        for n in range(1, MAX_TERMS + 1):
            result[n][0] = 1
            result[n][n] = 1
            for k in range(1, n):
                result[n][k] = result[n - 1][k - 1] + result[n - 1][k]
        return result

    @staticmethod
    def build_digit_sum_polynomials() -> list[list[list[int] | None]]:
        result: list[list[list[int] | None]] = [[None] * (MAX_TERMS + 1) for _ in range(MAX_TERMS + 1)]

        free_digits: list[list[int] | None] = [None] * (MAX_TERMS + 1)
        leading_digits: list[list[int] | None] = [None] * (MAX_TERMS + 1)
        free_digits[0] = [1]
        leading_digits[0] = [1]

        for terms in range(1, MAX_TERMS + 1):
            free_digits[terms] = append_digit_set(free_digits[terms - 1], 0, 9)
            leading_digits[terms] = append_digit_set(leading_digits[terms - 1], 1, 9)

        for active in range(MAX_TERMS + 1):
            for nxt in range(active + 1):
                result[active][nxt] = convolve(leading_digits[active - nxt], free_digits[nxt])

        return result

    @staticmethod
    def build_transition_base() -> tuple[list[list[list[int]]], int]:
        base = [[[0] * (MAX_TERMS + 1) for _ in range(MAX_TERMS + 1)] for _ in range(MAX_TERMS + 1)]
        next_index = 0
        for left_active in range(MAX_TERMS + 1):
            for left_next in range(left_active + 1):
                for right_active in range(MAX_TERMS - left_active + 1):
                    base[left_active][left_next][right_active] = next_index
                    next_index += right_active + 1
        return base, next_index

    def build_single_transition(
        self,
        left_active: int,
        left_next: int,
        right_active: int,
        right_next: int,
    ) -> Transition:
        transition = Transition()
        left_poly = self.digit_sums[left_active][left_next]
        right_poly = self.digit_sums[right_active][right_next]

        min_diff = -len(right_poly) + 1
        max_diff = len(left_poly) - 1
        diff_counts = [0] * (max_diff - min_diff + 1)

        for left_sum, left_ways in enumerate(left_poly):
            if left_ways == 0:
                continue
            for right_sum, right_ways in enumerate(right_poly):
                if right_ways == 0:
                    continue
                diff = left_sum - right_sum
                diff_counts[diff - min_diff] = mod_add(
                    diff_counts[diff - min_diff],
                    mod_mul(left_ways, right_ways),
                )

        for diff in range(min_diff, max_diff + 1):
            ways = diff_counts[diff - min_diff]
            if ways == 0:
                continue
            transition.by_residue[diff % 10].append((diff, ways))

        return transition

    def build_transitions(self) -> list[Transition]:
        transitions: list[Transition | None] = [None] * self.transition_count
        for left_active in range(MAX_TERMS + 1):
            for left_next in range(left_active + 1):
                for right_active in range(MAX_TERMS - left_active + 1):
                    base = self.transition_base[left_active][left_next][right_active]
                    for right_next in range(right_active + 1):
                        transitions[base + right_next] = self.build_single_transition(
                            left_active, left_next, right_active, right_next
                        )
        return transitions

    def solve(self, n: int) -> int:
        assert 0 <= n <= TARGET_N

        stride_len = (MAX_TERMS + 1) * (MAX_TERMS + 1) * DELTA_SIZE
        stride_a = (MAX_TERMS + 1) * DELTA_SIZE
        stride_b = DELTA_SIZE

        def index(used: int, left_active: int, right_active: int, delta: int) -> int:
            return (
                used * stride_len
                + left_active * stride_a
                + right_active * stride_b
                + delta
                + DELTA_LIMIT
            )

        dp = array("I", [0]) * ((n + 1) * stride_len)

        for left_terms in range(1, MAX_TERMS + 1):
            max_right_terms = MAX_TERMS - left_terms
            for right_terms in range(1, max_right_terms + 1):
                base_length = left_terms + right_terms - 1
                if base_length > n:
                    continue
                dp[index(base_length, left_terms, right_terms, 0)] = 1

        binom = self.binom
        transition_base = self.transition_base
        transitions = self.transitions

        for used in range(n + 1):
            for left_active in range(MAX_TERMS + 1):
                max_right_active = MAX_TERMS - left_active
                for right_active in range(max_right_active + 1):
                    if left_active == 0 and right_active == 0:
                        continue

                    next_length = used + left_active + right_active
                    if next_length > n:
                        continue

                    for delta in range(-DELTA_LIMIT, DELTA_LIMIT + 1):
                        current = dp[index(used, left_active, right_active, delta)]
                        if current == 0:
                            continue

                        residue = (-delta) % 10
                        for left_next in range(left_active + 1):
                            choose_left = binom[left_active][left_next]
                            for right_next in range(right_active + 1):
                                structure_weight = mod_mul(
                                    current,
                                    mod_mul(choose_left, binom[right_active][right_next]),
                                )
                                tindex = transition_base[left_active][left_next][right_active] + right_next
                                group = transitions[tindex].by_residue[residue]
                                for diff, ways in group:
                                    total = diff + delta
                                    next_delta = total // 10
                                    if -DELTA_LIMIT <= next_delta <= DELTA_LIMIT:
                                        target = index(next_length, left_next, right_next, next_delta)
                                        dp[target] = mod_add(dp[target], mod_mul(structure_weight, ways))

        answer = 0
        for used in range(n + 1):
            answer = mod_add(answer, dp[index(used, 0, 0, 0)])
        return answer


def usage() -> None:
    sys.stderr.write(
        "Usage:\n"
        "  python Euler990.py [n] [--skip-checkpoints] [--single-thread] [--threads=N]\n"
    )


def parse_options(argv: list[str]) -> Options:
    options = Options()
    for arg in argv[1:]:
        if arg == "--skip-checkpoints":
            options.run_checkpoints = False
            continue
        if arg == "--single-thread":
            options.allow_multithreading = False
            options.requested_threads = 1
            continue
        if arg.startswith("--threads="):
            options.requested_threads = int(arg[10:])
            continue
        if arg.startswith("-"):
            usage()
            raise SystemExit(1)
        options.target_n = int(arg)

    if options.target_n < 0 or options.target_n > TARGET_N:
        sys.stderr.write(f"n must satisfy 0 <= n <= {TARGET_N}.\n")
        raise SystemExit(1)

    return options


def run_checkpoints(solver: Solver) -> None:
    assert solver.solve(0) == 0
    assert solver.solve(1) == 0
    assert solver.solve(2) == 0
    assert solver.solve(3) == 9
    assert solver.solve(5) == 171
    assert solver.solve(7) == 4878


def main(argv: list[str]) -> int:
    options = parse_options(argv)
    solver = Solver(options)
    if options.run_checkpoints:
        run_checkpoints(solver)
    print(solver.solve(options.target_n))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
