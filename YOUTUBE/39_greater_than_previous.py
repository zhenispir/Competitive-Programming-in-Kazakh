"""  
Problem solving series

Date: 17-02-2022
17. Бұрынғыдан үлкен | Greater than previous - Python Есептер

Бүтін сандар массиві берілген. Алдыңғыдан көп (алдыңғы нөмірі 
бар элемент) массив элементтерінің санын есептейтін программа 
жазыңыз.
* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
6
1 3 2 1 5 9
Шығарылган деректер (Output): 
3
* * * * * * * * * * * * * *
"""
n = int(input())
a = list(map(int, input().split()))[:n]

result = 0
for i in range(n - 1):
    if a[i] < a[i+1]:
        result += 1
    else:
        result = result
print(result)
