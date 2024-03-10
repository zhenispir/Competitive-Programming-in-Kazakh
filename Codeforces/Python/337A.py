n, m = map(int, input().split())
a = list(map(int, input().split()))[:m]
a.sort()
x = False
for i in range(m):
    if any(a[i] == a[i+1] for i in range(m-1)):
        x = True
    
print(0) if x==True else print(a[n - 1] - a[0])