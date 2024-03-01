a = []
l, n = map(int, input().split())
for i in range(1, l+1):
    if i%2 != 0:
        a.append(i)
for i in range(1, l+1):
    if i%2 == 0:
        a.append(i)
print(a[n+1])