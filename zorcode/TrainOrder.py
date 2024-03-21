n,k = map(int, input().split())
a = list(map(int, input().split()))[:n]

summa = 0
for i in range(k-1):
    summa = summa + a[i]

print(summa)