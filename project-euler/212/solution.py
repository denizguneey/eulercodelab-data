from __future__ import annotations

import multiprocessing as mp
import os
from concurrent.futures import ProcessPoolExecutor


LFG_MOD = 1_000_000
POS_MOD = 10_000
LEN_MOD = 399

G_SLABS: list[list[tuple[int, int, int, int]]] = []
G_MAX_Z = 0


def build_lfg_sequence(needed: int) -> list[int]:
    s = [0] * (needed + 1)
    for k in range(1, min(56, needed + 1)):
        s[k] = (100003 - 200003 * k + 300007 * k * k * k) % LFG_MOD
    for k in range(56, needed + 1):
        s[k] = (s[k - 24] + s[k - 55]) % LFG_MOD
    return s


def generate_cuboids(n: int) -> list[tuple[int, int, int, int, int, int]]:
    needed = 6 * n
    s = build_lfg_sequence(needed)
    cuboids: list[tuple[int, int, int, int, int, int]] = []
    cuboids_append = cuboids.append
    for i in range(1, n + 1):
        base = 6 * i
        x0 = s[base - 5] % POS_MOD
        y0 = s[base - 4] % POS_MOD
        z0 = s[base - 3] % POS_MOD
        dx = 1 + (s[base - 2] % LEN_MOD)
        dy = 1 + (s[base - 1] % LEN_MOD)
        dz = 1 + (s[base] % LEN_MOD)
        cuboids_append((x0, x0 + dx, y0, y0 + dy, z0, z0 + dz))
    return cuboids


def init_area_worker(slabs: list[list[tuple[int, int, int, int]]], max_z: int) -> None:
    global G_SLABS, G_MAX_Z
    G_SLABS = slabs
    G_MAX_Z = max_z


def area_worker(bounds: tuple[int, int]) -> int:
    start_x, end_x = bounds
    slabs = G_SLABS
    max_z = G_MAX_Z
    tree_size = 4 * max_z + 8

    def update(node: int, l: int, r: int, ql: int, qr: int, delta: int, cover: list[int], length: list[int]) -> None:
        if qr <= l or r <= ql:
            return
        if ql <= l and r <= qr:
            cover[node] += delta
        else:
            mid = l + ((r - l) >> 1)
            update(node * 2, l, mid, ql, qr, delta, cover, length)
            update(node * 2 + 1, mid, r, ql, qr, delta, cover, length)

        if cover[node] > 0:
            length[node] = r - l
        elif r - l == 1:
            length[node] = 0
        else:
            length[node] = length[node * 2] + length[node * 2 + 1]

    total = 0
    for x in range(start_x, end_x):
        rects = slabs[x]
        if not rects:
            continue

        events: list[tuple[int, int, int, int]] = []
        events_extend = events.extend
        for y0, y1, z0, z1 in rects:
            events_extend(((y0, z0, z1, 1), (y1, z0, z1, -1)))
        events.sort(key=lambda e: e[0])

        cover = [0] * tree_size
        length = [0] * tree_size
        area = 0
        prev_y = events[0][0]
        i = 0
        m = len(events)
        while i < m:
            y = events[i][0]
            area += length[1] * (y - prev_y)
            while i < m and events[i][0] == y:
                _, z0, z1, d = events[i]
                update(1, 0, max_z, z0, z1, d, cover, length)
                i += 1
            prev_y = y
        total += area

    return total


def solve() -> int:
    n = 50_000
    cuboids = generate_cuboids(n)

    max_x = max(c[1] for c in cuboids)
    max_z = max(c[5] for c in cuboids)

    slabs: list[list[tuple[int, int, int, int]]] = [[] for _ in range(max_x)]
    for x0, x1, y0, y1, z0, z1 in cuboids:
        r = (y0, y1, z0, z1)
        for x in range(x0, x1):
            slabs[x].append(r)

    threads = max(1, min(8, os.cpu_count() or 1))
    if threads == 1:
        init_area_worker(slabs, max_z)
        return area_worker((0, max_x))

    block = (max_x + threads - 1) // threads
    jobs = []
    for t in range(threads):
        start_x = t * block
        end_x = min(max_x, (t + 1) * block)
        if start_x >= end_x:
            break
        jobs.append((start_x, end_x))

    ctx = mp.get_context("fork") if "fork" in mp.get_all_start_methods() else mp.get_context()
    total = 0
    with ProcessPoolExecutor(
        max_workers=len(jobs),
        mp_context=ctx,
        initializer=init_area_worker,
        initargs=(slabs, max_z),
    ) as pool:
        for part in pool.map(area_worker, jobs):
            total += part
    return total


if __name__ == "__main__":
    print(solve())
