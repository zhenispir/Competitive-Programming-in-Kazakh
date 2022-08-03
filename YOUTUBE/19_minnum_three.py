"""
Problem solving series

Date: 21-01-2022
#7 - Minimum number | Кіші сан
Үш бүтін a, b және с сандарын оқып, олардың 
ең кішісін шығаратын программа жазыңыз. 
Сандар 1-ден 1000-ға дейінгі бүтін сандар.

* * * * * * * * * * * * * *
Test 1:
Входные данные (Input):     15
                            36
                            12
Выходные данные (Output):   12
* * * * * * * * * * * * * *
Test 2:
Входные данные (Input):     15
                            68
                            10
Выходные данные (Output):   10
"""

a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
else:
    print("Barlygy teng")
