"""
Problem solving series

Date: 29-01-2022
11. Factorial numbers | Факторлық сандар - Python Есептер
Натурал n саны берілген, 1 * 2 *... * n 
нәтіжесіні есептеңдер.

* * * * * * * * * * * * * *
Test 1:
Енгізілген деректер (Input): 
3
Шығарылган деректер (Output): 
6
* * * * * * * * * * * * * *
Test 2:
Енгізілген деректер (Input): 
6
Шығарылган деректер (Output): 
720
"""

a = int(input())
b = 1
for i in range(1, a+1, 1):
    #print(i, '*', b, '=', b * i)
    b = b * i
print(b)
