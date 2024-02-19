t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    maxx = max(a)
    minn = min(a)
    print(maxx-minn)