"""  
Problem solving series

Date: 16-02-2022
16. Оң элементтердің саны | Number of positive elements - Python Есептер

Сандар бос орынмен көрсетілуі керек. Барлық сандар 
бүтін сандар, модулі 1-2^31-ден аспайды. Тізім элементтерінің 
саны 10000-нан аспайды.

Бүтін сандар массиві берілген. Массив элементтерінің 
арасындағы оң сандар санын есептейтін программа жазыңыз.
* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
5
1 2 3 -1 -4
Шығарылган деректер (Output): 
3
* * * * * * * * * * * * * *
"""

n = int(input())
a = list(map(int, input().split()))[:n]

'''
positive = 0
for i in range(len(a)):
    if a[i] > 0:
        positive += 1   # positive = positive + 1
    else:
        positive = positive

print(positive)
'''

b = []
for i in range(len(a)):
    if a[i] > 0:
        b.append(a[i])

print(len(b))
