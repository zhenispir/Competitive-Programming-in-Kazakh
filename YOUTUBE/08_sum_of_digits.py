"""
Problem solving series

#3 - Sum of digits
Үш таңбалы сан берілген. Оның цифрларының қосындысын табыңыз.
* * * * * * * * * * * * * *
Test 1:
Входные данные (Input):     179
Выходные данные (Output):   17
* * * * * * * * * * * * * *
Test 2:
Входные данные (Input):     489
Выходные данные (Output):   21
"""

a = int(input())

sifr1 = (a // 100)
sifr2 = ((a // 10) % 10)
sifr3 = (a % 10)

print(sifr1 + sifr2 + sifr3)
