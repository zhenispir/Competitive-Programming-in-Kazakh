"""
Python series
Date : 02-03-2021
28. Екі өлшемді массивті енгізу | Input two dimensional arrays - Python Қазақша
"""
# A = [[1, 2], [3, 4], [5, 6]]

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

# for i in range(n):
#    a.append(list(map(int, input().split())))

print(a)
