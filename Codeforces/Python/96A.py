'''
Name: Football
Link: https://codeforces.com/problemset/problem/69/A
Categories: matrix, sum
'''

n = (input())
count0 = n.count("0000000")
count1 = n.count("1111111")

# checking the condition
if (count0 > 0) or (count1 > 0):
    print("YES")
else:
    print("NO")
