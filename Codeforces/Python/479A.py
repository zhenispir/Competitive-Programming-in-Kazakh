'''
Name: Expression
Link: https://codeforces.com/problemset/problem/479/A
Categories: math, max
'''

# inputs as integer
a = int(input())
b = int(input())
c = int(input())

# all possibilities
c1 = a + b * c
c2 = a * (b + c)
c3 = a * b * c
c4 = (a + b) * c
c5 = a + b + c

# max is used find maximum of given values
print(max(c1, c2, c3, c4, c5))
