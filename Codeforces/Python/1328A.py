n = int(input())
a = []
x = []
for i in range(n):
    a.append(list(map(int, input().split()))[:2])

for j in range(len(a)):
    if a[j][0] % a[j][1] == 0:
        print(0)
    else:
        print(a[j][1] * (a[j][0] // a[j][1] + 1) - a[j][0])
