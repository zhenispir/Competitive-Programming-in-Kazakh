'''
Name: Lucky?
Link: https://codeforces.com/problemset/problem/1676/A
Categories: implementation, digits
'''
# number of test cases
t = int(input())
while t > 0:
    t -= 1
    d = int(input())
    dfirst = d // 1000  # first three numbers
    dlast = d % 1000    # last three numbers

    dfirsta = (dfirst//100) % 10
    dfirstb = (dfirst//10) % 10
    dfirstc = dfirst % 10

    dlasta = (dlast//100) % 10
    dlastb = (dlast//10) % 10
    dlastc = dlast % 10

    if dfirsta+dfirstb+dfirstc == dlasta+dlastb+dlastc:
        print("YES")
    else:
        print("NO")
