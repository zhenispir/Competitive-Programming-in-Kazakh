'''
Name: Vasya the Hipster
Link: https://codeforces.com/problemset/problem/581/A
Categories: multiple inputs, math
'''
a, b = map(int, input().split())
if a < b:
    print(a, (b-a)//2)
elif a == b:
    print(a, 0)
else:
    print(b, (a-b)//2)
