'''
Name: Brain's Photos
Link: https://codeforces.com/problemset/problem/707/A
Categories: matrix, string, for in for
'''

# n and m - matrix length
n, m = map(int, input().split())

array = []
# creating matrix using n and m
for i in range(n):
    array.append(list(map(str, input().split()))[:m])

color = "#Black&White"
# checking every element of matrix
for i in range(n):
    for j in range(m):
        if array[i][j] == "C" or array[i][j] == "M" or array[i][j] == "Y":
            color = "#Color"

print(color)
