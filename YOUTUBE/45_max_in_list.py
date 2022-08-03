"""  
Problem solving series

Date: 24-02-2022
20. Массивтегі максимум | Maximum in array - Python Есептер

Бүтін сандар массиві енгізіледі. Олардың ішіндегі ең үлкенін табыңыз.
* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
3
1 2 3
Шығарылган деректер (Output): 
3
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
6
5 3 8 6 9 7
Шығарылган деректер (Output): 
9 
* * * * * * * * * * * * * *
"""
n = int(input())
a = list(map(int, input().split()))
# a = [a[0], a[1], a[2]...]
max = 0
for i in range(n):
    if max < a[i]:
        max = a[i]
    else:
        max = max
print(max)
