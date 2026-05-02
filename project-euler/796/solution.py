def binom(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
    return res

def expected_formula(decks, suits, ranks, jokers_per_deck, need_suits, need_ranks, need_decks):
    total_cards = decks * (suits * ranks + jokers_per_deck)
    
    max_s = suits if need_suits else 0
    max_r = ranks if need_ranks else 0
    max_d = decks if need_decks else 0
    
    ans = 0.0
    
    for s in range(max_s + 1):
        cs = binom(suits, s) if need_suits else 1
        for r in range(max_r + 1):
            cr = binom(ranks, r) if need_ranks else 1
            for d in range(max_d + 1):
                cd = binom(decks, d) if need_decks else 1
                
                missed = s + r + d
                if missed == 0:
                    continue
                    
                safe_per_deck = (suits - s) * (ranks - r) + jokers_per_deck
                safe_cards = (decks - d) * safe_per_deck
                bad_cards = total_cards - safe_cards
                
                weight = (total_cards + 1.0) / (bad_cards + 1.0)
                mult = float(cs * cr * cd)
                
                if missed % 2 == 1:
                    ans += mult * weight
                else:
                    ans -= mult * weight
                    
    return ans

def solve():
    ans = expected_formula(10, 4, 13, 2, True, True, True)
    # The problem asks for 8 decimal places
    return "{:.8f}".format(ans)

if __name__ == "__main__":
    print(solve())
