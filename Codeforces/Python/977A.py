'''
Name: Wrong Subtraction
Link: https://codeforces.com/problemset/problem/977/A
Categories: for, if, multiple inputs in one line
'''

# a = number, b = number of steps
a, b = map(int, input().split())

# checking given number
for i in range(b):
    if a % 10 == 0:  # if it is divided by 10
        a = a // 10
    else:            # or not
        a = a-1

print(a)
