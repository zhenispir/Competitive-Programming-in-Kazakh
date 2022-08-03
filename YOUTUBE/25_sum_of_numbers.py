"""
Problem solving series

Date: 28-01-2022
#10 - Sum of the numbers | Сандардың қосындысы
Натурал n саны берілген, 1 + 2 +... + n 
қосындысын есептеңдер.

* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
3
Шығарылган деректер (Output): 
6
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
9
Шығарылган деректер (Output): 
45
"""

a = int(input())
natije = 0
for i in range(1, a + 1, 1):
    print(natije, '+', i, '=', natije + i)
    natije = natije + i

print(natije)
