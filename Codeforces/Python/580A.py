'''
Name: Kefa and First Steps
Link: https://codeforces.com/problemset/problem/580/A
Categories: brute force, geometry, max element
'''
# number of test cases
n = int(input())
a = list(map(int, input().split()))[:n]

length = 1
result = []
for i in range(n-1):
    if a[i] <= a[i+1]:
        length += 1
    else:
        result.append(length)
        length = 1

result.append(length)

print(max(result))
