"""
Python series
Date : 15-02-2021
21. Тізіmге деректерді еңғізү | List input - Python Қазақша

map() 
split()

3
0 1 2

5
66 
78 
95 
24 
31 
"""

n = int(input())
#a = list(map(str, input().split()))[:n]
b = []
for i in range(n):
    b.append(int(input()))
print(b)
