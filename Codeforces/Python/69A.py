'''
Name: Young Physicist
Link: https://codeforces.com/problemset/problem/69/A
Categories: matrix, sum
'''

# creating an empty matrix and
matrix = []
n = int(input())

# adding elements to the matrix which is 3x3
for i in range(n):
    matrix.append(list(map(int, input().split()))[:3])

totalx = totaly = totalz = 0
# sum of all rows
for i in range(n):
    totalx += matrix[i][0]
    totaly += matrix[i][1]
    totalz += matrix[i][2]

if totalx == totaly == totalz == 0:
    print("YES")
else:
    print("NO")
