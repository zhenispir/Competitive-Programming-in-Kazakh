'''
Name: Next Round
Link: https://codeforces.com/problemset/problem/158/A
Categories: for, if, multiple inputs in one line
'''

# n = number of scores, b = score to pass
n, b = map(int, input().split())

# a = all scores by participants, number of values
a = list(map(int, input().split()))[:n]
count = 0

# checking each value
for i in range(len(a)):
    if a[i] > 0 and a[i] >= a[b-1]:
        count += 1

print(count)
