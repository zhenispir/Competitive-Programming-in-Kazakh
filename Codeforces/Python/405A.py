'''
Gravity Flip
https://codeforces.com/problemset/problem/405/A
sorting, array
'''

# n = length of an array, a = values
n = int(input())
a = list(map(int, input().split()))[:n]

a.sort()

# *a is used to print array values in one line
print(*a)
