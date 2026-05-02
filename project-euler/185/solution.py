def solve():
    guesses = [
        ("5616185650518293", 2), ("3847439647293047", 1),
        ("5855462940810587", 3), ("9742855507068353", 3),
        ("4296849643607543", 3), ("3174248439465858", 1),
        ("4513559094146117", 2), ("7890971548908067", 3),
        ("8157356344118483", 1), ("2615250744386899", 2),
        ("8690095851526254", 3), ("6375711915077050", 1),
        ("6913859173121360", 1), ("6442889055042768", 2),
        ("2321386104303845", 0), ("2326509471271448", 2),
        ("5251583379644322", 2), ("1748270476758276", 3),
        ("4895722652190306", 1), ("3041631117224635", 3),
        ("1841236454324589", 3), ("2659862637316867", 2),
    ]
    guesses.sort(key=lambda x: x[1])
    length = len(guesses[0][0])

    def propagate(assign, banned):
        changed = True
        while changed:
            changed = False
            for pos in range(length):
                if assign[pos] != -1:
                    continue
                allowed = [d for d in range(10) if not banned[pos][d]]
                if len(allowed) == 0:
                    return False
                if len(allowed) == 1:
                    assign[pos] = allowed[0]
                    for d in range(10):
                        banned[pos][d] = (d != allowed[0])
                    changed = True
        return True

    def feasible(assign, banned):
        for digits, matches in guesses:
            min_m = 0
            max_m = 0
            for i in range(length):
                d = int(digits[i])
                if assign[i] == d:
                    min_m += 1
                    max_m += 1
                elif assign[i] == -1 and not banned[i][d]:
                    max_m += 1
            if min_m > matches or max_m < matches:
                return False
        return True

    def satisfies_all(assign):
        for digits, matches in guesses:
            m = sum(1 for i in range(length) if assign[i] == int(digits[i]))
            if m != matches:
                return False
        return True

    from math import comb

    result = [None]

    def dfs(assign, banned):
        if result[0] is not None:
            return
        a = list(assign)
        b = [list(row) for row in banned]
        if not propagate(a, b):
            return
        if not feasible(a, b):
            return
        if all(d >= 0 for d in a):
            if satisfies_all(a):
                result[0] = ''.join(str(d) for d in a)
            return

        best_gi = -1
        best_branching = float('inf')
        best_cands = []
        best_need = 0
        for gi, (digits, matches) in enumerate(guesses):
            fixed = 0
            cands = []
            for pos in range(length):
                d = int(digits[pos])
                if a[pos] == d:
                    fixed += 1
                elif a[pos] == -1 and not b[pos][d]:
                    cands.append(pos)
            need = matches - fixed
            if need < 0 or need > len(cands):
                return
            if need == 0 and not cands:
                continue
            branching = comb(len(cands), need)
            if branching < best_branching:
                best_branching = branching
                best_gi = gi
                best_cands = cands
                best_need = need

        if best_gi < 0:
            return

        digits_str = guesses[best_gi][0]

        def branch(idx, chosen):
            if result[0] is not None:
                return
            remaining = len(best_cands) - idx
            if len(chosen) > best_need or len(chosen) + remaining < best_need:
                return
            if idx == len(best_cands):
                na = list(a)
                nb = [list(row) for row in b]
                chosen_set = set(chosen)
                for i, pos in enumerate(best_cands):
                    d = int(digits_str[pos])
                    if pos in chosen_set:
                        if na[pos] != -1 and na[pos] != d:
                            return
                        if na[pos] == -1 and nb[pos][d]:
                            return
                        na[pos] = d
                        for dd in range(10):
                            nb[pos][dd] = (dd != d)
                    else:
                        if na[pos] == d:
                            return
                        nb[pos][d] = True
                dfs(na, nb)
                return
            branch(idx + 1, chosen + [best_cands[idx]])
            branch(idx + 1, chosen)

        branch(0, [])

    assign = [-1] * length
    banned = [[False] * 10 for _ in range(length)]
    for digits, matches in guesses:
        if matches == 0:
            for i in range(length):
                banned[i][int(digits[i])] = True
    dfs(assign, banned)
    return result[0]

if __name__ == '__main__':
    print(solve())
