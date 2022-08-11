'''
Name: Lucky?
Link: https://codeforces.com/problemset/problem/1676/A
Categories: implementation, digits
'''
# number of test cases
t = int(input())
while t > 0:
    d = (input())
    t -= 1

    if (int(d[0]) + int(d[1]) + int(d[2])) == (int(d[3]) + int(d[4]) + int(d[5])):
        print("YES")
    else:
        print("NO")
