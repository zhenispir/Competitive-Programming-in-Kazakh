"""
Python series
Date : 19-01-2021
#11 - Кірістірілген if | Nested if


if condition:
    statements / codes
elif condition:
    statements / codes
else:
    statements / codes
"""

a = int(input())

if 0 <= a <= 100:
    if a > 85:
        print("Bagasy 5")
    elif a > 65:
        print("Bagasy 4")
    elif a > 40:
        print("Bagasy 3")
    else:
        print("Bagasy 2")
else:
    print("Berilgen upai 0 men 100 aralygynda boluy kerek!")
