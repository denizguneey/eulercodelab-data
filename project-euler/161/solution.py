from __future__ import annotations

from collections import defaultdict
from functools import lru_cache


W = 9
H = 12
FULL = (1 << (2 * W)) - 1


def bit(mask: int, pos: int) -> bool:
    return ((mask >> pos) & 1) != 0


@lru_cache(maxsize=None)
def transitions(state: int) -> tuple[tuple[int, int], ...]:
    out: dict[int, int] = defaultdict(int)

    def dfs(d: int, mask: int) -> None:
        if d < 0:
            if ((mask + 1) & ((1 << W) - 1)) == 0:
                out[mask >> W] += 1
            return

        dfs(d - 1, mask)

        if not bit(mask, d) and not bit(mask, d + W):
            dfs(d - 1, mask | (1 << d) | (1 << (d + W)) | (1 << (d + 2 * W)))

        if d >= 2:
            dfs(d - 3, mask | (1 << (d + 2 * W)) | (1 << (d - 1 + 2 * W)) | (1 << (d - 2 + 2 * W)))

        if d >= 1 and not bit(mask, d + W) and not bit(mask, d + 2 * W - 1):
            dfs(d - 2, mask | (1 << (d + W)) | (1 << (d + 2 * W - 1)) | (1 << (d + 2 * W)))

        if d >= 1 and not bit(mask, d + W - 1) and not bit(mask, d + 2 * W - 1):
            dfs(d - 2, mask | (1 << (d + W - 1)) | (1 << (d + 2 * W - 1)) | (1 << (d + 2 * W)))

        if d >= 1 and not bit(mask, d + W - 1) and not bit(mask, d + W):
            dfs(d - 1, mask | (1 << (d + W - 1)) | (1 << (d + W)) | (1 << (d + 2 * W)))

        if d < W - 1 and not bit(mask, d + W) and not bit(mask, d + W + 1):
            dfs(d - 1, mask | (1 << (d + W + 1)) | (1 << (d + W)) | (1 << (d + 2 * W)))

    dfs(W - 1, state)
    return tuple(out.items())


def solve() -> int:
    if (W * H) % 3 != 0:
        return 0

    cur: dict[int, int] = {FULL: 1}
    for _ in range(H):
        nxt: dict[int, int] = defaultdict(int)
        for state, ways in cur.items():
            for dst, multiplicity in transitions(state):
                nxt[dst] += ways * multiplicity
        cur = nxt
    return cur.get(FULL, 0)


if __name__ == "__main__":
    print(solve())
