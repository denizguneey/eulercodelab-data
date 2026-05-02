from __future__ import annotations

import bisect
import math
import multiprocessing as mp
import os
from concurrent.futures import ProcessPoolExecutor


G_LIMIT = 0
G_BASE_PRIMES: list[int] = []


def isqrt(n: int) -> int:
    return math.isqrt(n)


def sieve_primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    is_p = bytearray(b"\x01" * (n + 1))
    is_p[0] = 0
    is_p[1] = 0
    root = isqrt(n)
    for p in range(2, root + 1):
        if is_p[p]:
            start = p * p
            is_p[start::p] = bytearray(((n - start) // p) + 1)
    return [p for p in range(2, n + 1) if is_p[p]]


def is_good_prime(p: int) -> bool:
    if p <= 7:
        return False
    residue = p % 168
    return residue == 1 or residue == 25 or residue == 121


def singleton_sum_in_range(low: int, high: int, limit: int, base_primes: list[int]) -> int:
    if low > high or high < 2:
        return 0

    segment_size = 1 << 20
    total = 0
    seg_low = low

    while seg_low <= high:
        seg_high = min(seg_low + segment_size - 1, high)
        length = seg_high - seg_low + 1
        is_prime = bytearray(b"\x01" * length)

        for p in base_primes:
            p2 = p * p
            if p2 > seg_high:
                break
            start = ((seg_low + p - 1) // p) * p
            if start < p2:
                start = p2
            is_prime[start - seg_low : length : p] = bytearray(((seg_high - start) // p) + 1)

        if seg_low <= 1:
            bound = min(2, length)
            for i in range(bound):
                if seg_low + i <= 1:
                    is_prime[i] = 0

        for idx, flag in enumerate(is_prime):
            if not flag:
                continue
            value = seg_low + idx
            if is_good_prime(value):
                total += isqrt(limit // value)

        seg_low = seg_high + 1

    return total


def init_singleton_worker(limit: int, base_primes: list[int]) -> None:
    global G_LIMIT, G_BASE_PRIMES
    G_LIMIT = limit
    G_BASE_PRIMES = base_primes


def singleton_worker(bounds: tuple[int, int]) -> int:
    low, high = bounds
    return singleton_sum_in_range(low, high, G_LIMIT, G_BASE_PRIMES)


def sum_singleton_kernels(limit: int, base_primes: list[int], threads: int) -> int:
    first = 2
    last = limit
    count = last - first + 1
    workers = max(1, min(threads, count))
    if workers == 1:
        return singleton_sum_in_range(first, last, limit, base_primes)

    block = (count + workers - 1) // workers
    jobs = []
    for tid in range(workers):
        low = first + tid * block
        if low > last:
            break
        high = min(last, low + block - 1)
        jobs.append((low, high))

    ctx = mp.get_context("fork") if "fork" in mp.get_all_start_methods() else mp.get_context()
    total = 0
    with ProcessPoolExecutor(
        max_workers=workers,
        mp_context=ctx,
        initializer=init_singleton_worker,
        initargs=(limit, base_primes),
    ) as pool:
        for partial in pool.map(singleton_worker, jobs):
            total += partial
    return total


def build_spf_table(n: int) -> list[int]:
    spf = list(range(n + 1))
    root = isqrt(n)
    for i in range(2, root + 1):
        if spf[i] == i:
            for x in range(i * i, n + 1, i):
                if spf[x] == x:
                    spf[x] = i
    return spf


def factorize_dy2(y: int, d: int, spf: list[int]) -> list[tuple[int, int]]:
    factors: dict[int, int] = {}
    val = y
    while val > 1:
        p = spf[val]
        count = 0
        while val % p == 0:
            val //= p
            count += 1
        factors[p] = factors.get(p, 0) + 2 * count

    rem_d = d
    p = 2
    while p * p <= rem_d:
        if rem_d % p == 0:
            count = 0
            while rem_d % p == 0:
                rem_d //= p
                count += 1
            factors[p] = factors.get(p, 0) + count
        p += 1
    if rem_d > 1:
        factors[rem_d] = factors.get(rem_d, 0) + 1

    return sorted(factors.items())


def build_divisors(factors: list[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for p, e in factors:
        base = list(divisors)
        mul = 1
        for _ in range(e):
            mul *= p
            for d in base:
                divisors.append(d * mul)
    return divisors


def square_roots_with_positive_rep(limit: int, d: int, spf: list[int]) -> bytearray:
    max_root = isqrt(limit)
    max_y = isqrt(limit // d)
    mark = bytearray(max_root + 1)

    for y in range(1, max_y + 1):
        D = d * y * y
        factors = factorize_dy2(y, d, spf)
        divisors = build_divisors(factors)

        for u in divisors:
            v = D // u
            if u > v:
                continue
            if ((u + v) & 1) != 0:
                continue
            if v <= u:
                continue
            m = (u + v) // 2
            if m <= max_root:
                mark[m] = 1

    return mark


def solve() -> str:
    limit = 2_000_000_000
    threads = max(1, min(8, os.cpu_count() or 1))

    square_kernel = isqrt(limit)
    base_bound = isqrt(limit)
    base_primes = sieve_primes_up_to(base_bound)
    singleton = sum_singleton_kernels(limit, base_primes, threads)

    min_good = 193
    max_factor = limit // min_good if min_good <= limit else 0
    good_primes = [p for p in sieve_primes_up_to(max_factor) if is_good_prime(p)] if max_factor >= 11 else []

    def multi_dfs(start_index: int, current_product: int, picked: int) -> int:
        total = 0
        for i in range(start_index, len(good_primes)):
            p = good_primes[i]
            if current_product > limit // p:
                break
            next_product = current_product * p
            if picked + 1 >= 2:
                total += isqrt(limit // next_product)
            total += multi_dfs(i + 1, next_product, picked + 1)
        return total

    multi = multi_dfs(0, 1, 0)
    integer_representable = square_kernel + singleton + multi

    max_root = isqrt(limit)
    spf = build_spf_table(max_root)
    d1 = square_roots_with_positive_rep(limit, 1, spf)
    d2 = square_roots_with_positive_rep(limit, 2, spf)
    d3 = square_roots_with_positive_rep(limit, 3, spf)
    d7 = square_roots_with_positive_rep(limit, 7, spf)

    good_squares = sum(1 for m in range(1, max_root + 1) if d1[m] and d2[m] and d3[m] and d7[m])
    total_squares = isqrt(limit)
    answer = integer_representable - total_squares + good_squares
    return str(answer)


if __name__ == "__main__":
    print(solve())
