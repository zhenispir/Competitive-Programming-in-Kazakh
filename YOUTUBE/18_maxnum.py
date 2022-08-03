"""
Problem solving series

Date: 20-01-2022
#6 - Maximum number | Үлкен сан
Екі бүтін a және b сандарын оқып, олардың 
ең үлкенін шығаратын программа жазыңыз. 
Сандар 1-ден 1000-ға дейінгі бүтін сандар.

* * * * * * * * * * * * * *
Test 1:
Входные данные (Input):     8
                            5
Выходные данные (Output):   8
* * * * * * * * * * * * * *
Test 2:
Входные данные (Input):     15
                            33
Выходные данные (Output):   33
"""

a = int(input())
b = int(input())

if a > b:
    print(a)
elif a == b:
    print("Teng")
else:
    print(b)
