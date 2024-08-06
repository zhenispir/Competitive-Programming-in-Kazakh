def count_wins(a1, a2, b1, b2):
    # Possible flips for Suneet: (a1, a2), (a1, b2), (a2, b1), (a2, b2)
    # Possible flips for Slavic: (b1, b2), (b1, a2), (b2, a1), (b2, a2)
    suneet_wins = 0
    games = [
        ((a1, b1), (a2, b2)),
        ((a1, b2), (a2, b1)),
        ((a2, b1), (a1, b2)),
        ((a2, b2), (a1, b1)),
        ((a1, b1), (b2, a2)),
        ((a1, b2), (b1, a2)),
        ((a2, b1), (b2, a1)),
        ((a2, b2), (b1, a1))
    ]
    
    for game in games:
        (s1, s2), (s3, s4) = game
        suneet_score = 0
        slavic_score = 0
        
        # First round
        if s1 > s2:
            suneet_score += 1
        elif s1 < s2:
            slavic_score += 1
        
        # Second round
        if s3 > s4:
            suneet_score += 1
        elif s3 < s4:
            slavic_score += 1
        
        # Check if Suneet wins
        if suneet_score > slavic_score:
            suneet_wins += 1
    
    return suneet_wins

# Read number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    print(count_wins(a1, a2, b1, b2))