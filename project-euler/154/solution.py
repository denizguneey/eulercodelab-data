from __future__ import annotations

import argparse
import multiprocessing as mp
import os
from concurrent.futures import ProcessPoolExecutor


G_V2: list[int] = []
G_V5: list[int] = []
G_N = 0
G_NEED2 = 0
G_NEED5 = 0


def build_factorial_prime_exponents(n: int) -> tuple[list[int], list[int]]:
    v2 = [0] * (n + 1)
    v5 = [0] * (n + 1)
    for i in range(1, n + 1):
        x = i
        add2 = 0
        while (x & 1) == 0:
            x >>= 1
            add2 += 1

        x = i
        add5 = 0
        while x % 5 == 0:
            x //= 5
            add5 += 1

        v2[i] = v2[i - 1] + add2
        v5[i] = v5[i - 1] + add5
    return v2, v5


def init_worker(v2: list[int], v5: list[int], n: int, need2: int, need5: int) -> None:
    global G_V2, G_V5, G_N, G_NEED2, G_NEED5
    G_V2 = v2
    G_V5 = v5
    G_N = n
    G_NEED2 = need2
    G_NEED5 = need5


def count_chunk(a_start: int, a_end: int) -> int:
    v2 = G_V2
    v5 = G_V5
    n = G_N
    need2 = G_NEED2
    need5 = G_NEED5

    local = 0
    for a in range(a_start, a_end):
        a2 = v2[a]
        a5 = v5[a]
        b_max = (n - a) // 2
        for b in range(a, b_max + 1):
            c = n - a - b
            if a2 + v2[b] + v2[c] > need2:
                continue
            if a5 + v5[b] + v5[c] > need5:
                continue
            if a == b == c:
                local += 1
            elif a == b or b == c:
                local += 3
            else:
                local += 6
    return local


def solve(n: int = 200000, threads: int | None = None) -> int:
    v2, v5 = build_factorial_prime_exponents(n)
    need2 = v2[n] - 12
    need5 = v5[n] - 12
    a_max = n // 3

    if threads is None:
        threads = min(8, os.cpu_count() or 1)
    threads = max(1, threads)

    if threads == 1:
        init_worker(v2, v5, n, need2, need5)
        return count_chunk(0, a_max + 1)

    ctx = mp.get_context("fork") if "fork" in mp.get_all_start_methods() else mp.get_context()
    chunk_size = 256
    tasks = []
    for start in range(0, a_max + 1, chunk_size):
        end = min(a_max + 1, start + chunk_size)
        tasks.append((start, end))

    total = 0
    with ProcessPoolExecutor(
        max_workers=threads,
        mp_context=ctx,
        initializer=init_worker,
        initargs=(v2, v5, n, need2, need5),
    ) as pool:
        futures = [pool.submit(count_chunk, start, end) for start, end in tasks]
        for fut in futures:
            total += fut.result()
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=200000)
    parser.add_argument("--threads", type=int, default=min(8, os.cpu_count() or 1))
    args = parser.parse_args()
    print(solve(args.n, args.threads))


if __name__ == "__main__":
    main()
