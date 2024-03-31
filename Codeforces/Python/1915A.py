t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))[:3]
    if a.count(a[0]) == 1:
        print(a[0])
    elif a.count(a[1]) == 1:
        print(a[1])
    elif a.count(a[2]) == 1:
        print(a[2])