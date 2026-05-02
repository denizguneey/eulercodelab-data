# Problem 84: Monopoly odds
# Using two 4-sided dice, find the three most popular squares (modal string).

import random

def solve():
    random.seed(42)
    # Board positions
    GO,A1,CC1,A2,T1,R1,B1,CH1,B2,B3 = 0,1,2,3,4,5,6,7,8,9
    JAIL,C1,U1,C2,C3,R2,D1,CC2,D2,D3 = 10,11,12,13,14,15,16,17,18,19
    FP,E1,CH2,E2,E3,R3,F1,F2,U2,F3 = 20,21,22,23,24,25,26,27,28,29
    G2J,G1,G2,CC3,G3,R4,CH3,H1,T2,H2 = 30,31,32,33,34,35,36,37,38,39
    
    visits = [0] * 40
    pos = 0
    doubles = 0
    cc_cards = list(range(16))
    ch_cards = list(range(16))
    random.shuffle(cc_cards)
    random.shuffle(ch_cards)
    cc_idx = ch_idx = 0
    
    def next_r(p):
        if p < 5 or p >= 35: return R1
        if p < 15: return R2
        if p < 25: return R3
        return R4
    
    def next_u(p):
        return U1 if p < 12 or p >= 28 else U2
    
    for _ in range(1000000):
        d1 = random.randint(1, 4)
        d2 = random.randint(1, 4)
        if d1 == d2:
            doubles += 1
        else:
            doubles = 0
        
        if doubles >= 3:
            pos = JAIL
            doubles = 0
        else:
            pos = (pos + d1 + d2) % 40
            
            if pos == G2J:
                pos = JAIL
            
            if pos in (CC1, CC2, CC3):
                card = cc_cards[cc_idx]; cc_idx = (cc_idx + 1) % 16
                if card == 0: pos = GO
                elif card == 1: pos = JAIL
            
            if pos in (CH1, CH2, CH3):
                card = ch_cards[ch_idx]; ch_idx = (ch_idx + 1) % 16
                if card == 0: pos = GO
                elif card == 1: pos = JAIL
                elif card == 2: pos = C1
                elif card == 3: pos = E3
                elif card == 4: pos = H2
                elif card == 5: pos = R1
                elif card == 6 or card == 7: pos = next_r(pos)
                elif card == 8: pos = next_u(pos)
                elif card == 9: pos = (pos - 3) % 40
        
        visits[pos] += 1
    
    indexed = sorted(range(40), key=lambda i: -visits[i])
    print(f"{indexed[0]:02d}{indexed[1]:02d}{indexed[2]:02d}")

solve()
