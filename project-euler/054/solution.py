import sys
from collections import Counter

def rank_from_char(c):
    if '2' <= c <= '9':
        return ord(c) - ord('0')
    mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return mapping.get(c, -1)

def parse_card(s):
    if len(s) != 2:
        raise ValueError(f"Invalid card token: {s}")
    rank = rank_from_char(s[0])
    suit = s[1]
    if not (2 <= rank <= 14):
        raise ValueError(f"Invalid card rank: {s}")
    return (rank, suit)

def evaluate_hand(hand):
    ranks = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    
    freq = Counter(ranks)
    
    flush = len(set(suits)) == 1
    
    sorted_ranks = sorted(ranks)
    straight = True
    for i in range(1, 5):
        if sorted_ranks[i] != sorted_ranks[i-1] + 1:
            straight = False
            break
    
    # Handle special case: A-2-3-4-5 straight (Ace low)
    if not straight and sorted_ranks == [2, 3, 4, 5, 14]:
        straight = True
        sorted_ranks = [1, 2, 3, 4, 5]  # Treat Ace as 1 for tiebreaking
    
    groups = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
    
    if straight and flush:
        return (8, [sorted_ranks[-1]])
    
    if groups[0][1] == 4:
        return (7, [groups[0][0], groups[1][0]])
    
    if groups[0][1] == 3 and groups[1][1] == 2:
        return (6, [groups[0][0], groups[1][0]])
    
    if flush:
        return (5, sorted_ranks[::-1])
    
    if straight:
        return (4, [sorted_ranks[-1]])
    
    if groups[0][1] == 3:
        result = [groups[0][0]]
        for rank, count in groups[1:]:
            result.append(rank)
        return (3, result)
    
    if groups[0][1] == 2 and groups[1][1] == 2:
        result = [groups[0][0], groups[1][0], groups[2][0]]
        return (2, result)
    
    if groups[0][1] == 2:
        result = [groups[0][0]]
        for rank, count in groups[1:]:
            result.append(rank)
        return (1, result)
    
    return (0, sorted_ranks[::-1])

def player1_wins(p1, p2):
    h1 = evaluate_hand(p1)
    h2 = evaluate_hand(p2)
    
    if h1[0] != h2[0]:
        return h1[0] > h2[0]
    
    return h1[1] > h2[1]

def solve(file_path):
    wins = 0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            cards = line.split()
            p1 = [parse_card(card) for card in cards[:5]]
            p2 = [parse_card(card) for card in cards[5:10]]
            
            if player1_wins(p1, p2):
                wins += 1
    
    return wins

def run_checkpoints():
    # Checkpoint 1: Player 2 should win
    p1 = [parse_card("5H"), parse_card("5C"), parse_card("6S"), parse_card("7S"), parse_card("KD")]
    p2 = [parse_card("2C"), parse_card("3S"), parse_card("8S"), parse_card("8D"), parse_card("TD")]
    if player1_wins(p1, p2):
        return False
    
    # Checkpoint 4: Player 1 should win
    p1 = [parse_card("4D"), parse_card("6S"), parse_card("9H"), parse_card("QH"), parse_card("QC")]
    p2 = [parse_card("3D"), parse_card("6D"), parse_card("7H"), parse_card("QD"), parse_card("QS")]
    if not player1_wins(p1, p2):
        return False
    
    return True

if __name__ == "__main__":
    file_path = "resources/documents/0054_poker.txt"
    
    # Parse command line arguments
    args = sys.argv[1:]
    skip_checkpoints = False
    for arg in args:
        if arg == "--skip-checkpoints":
            skip_checkpoints = True
        elif arg.startswith("--file="):
            file_path = arg[7:]
    
    if not skip_checkpoints and not run_checkpoints():
        sys.exit(2)
    
    try:
        print(solve(file_path))
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(3)
