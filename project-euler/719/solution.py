def solve():
    LIMIT = 10**12

    def is_s_number(root):
        sq = root * root
        s = str(sq)
        n = len(s)
        digits = [int(c) for c in s]

        suffix_val = [0] * (n + 1)
        suffix_dsum = [0] * (n + 1)
        place = 1
        for i in range(n - 1, -1, -1):
            suffix_val[i] = digits[i] * place + suffix_val[i + 1]
            place *= 10
            suffix_dsum[i] = suffix_dsum[i + 1] + digits[i]

        def dfs(pos, sm):
            if pos == n: return sm == root
            part = 0
            for end in range(pos, n):
                part = part * 10 + digits[end]
                ns = sm + part
                if ns > root: break
                if ns + suffix_dsum[end + 1] > root: continue
                if ns + suffix_val[end + 1] < root: continue
                if dfs(end + 1, ns): return True
            return False

        first_part = 0
        for end in range(n - 1):
            first_part = first_part * 10 + digits[end]
            if first_part > root: break
            if first_part + suffix_dsum[end + 1] > root: continue
            if first_part + suffix_val[end + 1] < root: continue
            if dfs(end + 1, first_part): return True
        return False

    total = 0
    for root in range(2, 1000001):
        if root * root > LIMIT: break
        mod9 = root % 9
        if mod9 != 0 and mod9 != 1: continue
        if is_s_number(root):
            total += root * root

    return str(total)

if __name__ == '__main__':
    print(solve())
