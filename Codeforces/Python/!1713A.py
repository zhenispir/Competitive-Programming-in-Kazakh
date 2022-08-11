'''
Name: Traveling Salesman Problem
Link: https://codeforces.com/problemset/problem/1713/A
Categories: geometry, greedy, absolute value
'''
# number of test cases
t = int(input())
while t > 0:
    output = 0

    # nth test case x and y values
    n = int(input())
    while n > 0:
        x, y = map(int, input().split())
        output += (abs(x) + abs(y))
        n -= 1
    print(2 * output)
    t -= 1
