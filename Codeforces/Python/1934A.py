t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    ssum=0
    for i in range(n):
        
        ssum += abs(a[i]-a[i+1])
    print(ssum)
