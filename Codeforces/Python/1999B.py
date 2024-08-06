def count_wins(a1, a2, b1, b2):
    suneet_cards = [a1, a2]
    slavic_cards = [b1, b2]
    
    suneet_wins = 0
    for i in range(2):
        for j in range(2):
            suneet_score = 0
            slavic_score = 0
            
            # First round
            if suneet_cards[i] > slavic_cards[j]:
                suneet_score += 1
            elif suneet_cards[i] < slavic_cards[j]:
                slavic_score += 1
            
            # Second round
            if suneet_cards[1-i] > slavic_cards[1-j]:
                suneet_score += 1
            elif suneet_cards[1-i] < slavic_cards[1-j]:
                slavic_score += 1
            
            # Check if Suneet wins more rounds
            if suneet_score > slavic_score:
                suneet_wins += 1
    
    return suneet_wins


t = int(input())

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    print(count_wins(a1, a2, b1, b2))