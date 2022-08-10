'''
Name: 2-3 Moves
Link: https://codeforces.com/problemset/problem/1716/A
Categories: for, list, printing list
'''

t = int(input())
n = []
result = []
for i in range(t):
    n.append(int(input()))

for i in range(t):
    # condition for solution
    if abs(n[i]) == 1:
        r = 2
    elif abs(n[i]) == 2:
        r = 1
    elif abs(n[i]) % 3 == 0:
        r = abs(n[i]) // 3
    else:
        r = abs(n[i])//3 + 1

    # adding result to the list
    result.append(r)

# printing list in seperate lines
print(*result, sep="\n")
