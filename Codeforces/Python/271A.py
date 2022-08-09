'''
Name: Beautiful Year
Link: https://codeforces.com/problemset/problem/271/A
Categories: matrix, sum
'''

n = int(input())

# bir jyl kosu
n = n+1

# ar bir sandy tekseru
a = n // 1000
b = (n//100) % 10
c = (n//10) % 10
d = n % 10

# ar bir sifrdi tengestiru
while a == b or a == c or a == d or b == c or b == d or c == d:
    n = n+1
    a = n // 1000
    b = (n//100) % 10
    c = (n//10) % 10
    d = n % 10

print(n)
