def rank_sjt(p):
    n = len(p)
    if n <= 1:
        return 0

    mx = n - 1
    pos = 0
    while p[pos] != mx:
        pos += 1

    q = []
    for i in range(n):
        if i != pos:
            q.append(p[i])

    b = rank_sjt(q)
    off = pos if (b & 1) else (n - 1 - pos)
    return b * n + off

def swaps_to_reach(word):
    sorted_word = sorted(word)
    idx = {}
    for i, c in enumerate(sorted_word):
        idx[c] = i

    perm = []
    for c in word:
        perm.append(idx[c])

    return rank_sjt(perm)

def solve():
    return str(swaps_to_reach("NOWPICKBELFRYMATHS"))

if __name__ == "__main__":
    print(solve())
