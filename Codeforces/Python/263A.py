'''
Name: Beautiful Matrix
Link: https://codeforces.com/problemset/problem/158/A
Categories: matrix(list of list), index, for break, if, abs
'''
matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split()))[:5])

row = 0
for i in range(5):
    if sum(matrix[i]) == 1:
        column = matrix[row].index(1)
        break
    row += 1
print(abs(row-2) + abs(column-2))
