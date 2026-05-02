def count_subtree(counts_tuple, remaining, dp):
    if remaining == 0:
        return 1
        
    counts = sorted(list(counts_tuple), reverse=True)
    while counts and counts[-1] == 0:
        counts.pop()
        
    key = (tuple(counts), remaining)
    if key in dp:
        return dp[key]
        
    total = 1
    for i in range(len(counts)):
        if counts[i] == 0:
            continue
        nxt = list(counts)
        nxt[i] -= 1
        total += count_subtree(tuple(nxt), remaining - 1, dp)
        
    dp[key] = total
    return total

def build_word(counts, remaining, pos, dp):
    if pos == 1:
        return ""
        
    pos -= 1
    for c in range(26):
        if counts[c] == 0:
            continue
        counts[c] -= 1
        cnt = count_subtree(tuple(counts), remaining - 1, dp)
        if cnt < pos:
            counts[c] += 1
            pos -= cnt
            continue
        return chr(ord('a') + c) + build_word(counts, remaining - 1, pos, dp)
        
    return ""

def position_of(counts, remaining, target, dp):
    if not target:
        return 1
        
    first = ord(target[0]) - ord('a')
    pos = 1
    
    for c in range(first):
        if counts[c] == 0:
            continue
        nxt = list(counts)
        nxt[c] -= 1
        pos += count_subtree(tuple(nxt), remaining - 1, dp)
        
    nxt = list(counts)
    nxt[first] -= 1
    pos += position_of(nxt, remaining - 1, target[1:], dp)
    return pos

def solve():
    source = "thereisasyetinsufficientdataforameaningfulanswer"
    counts = [0] * 26
    for ch in source:
        counts[ord(ch) - ord('a')] += 1
        
    dp = {}
    
    def pos_word(word):
        return position_of(list(counts), 15, word, dp) - 1
        
    def word_at(rank):
        return build_word(list(counts), 15, rank + 1, dp)
        
    target_rank = pos_word("legionary") + pos_word("calorimeters") - pos_word("annihilate") + pos_word("orchestrated") - pos_word("fluttering")
    
    return word_at(target_rank)

if __name__ == '__main__':
    print(solve())
