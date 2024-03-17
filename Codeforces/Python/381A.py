n = int(input())
a = list(map(int, input().split()))
s, d = 0, 0
l, r = 0, n - 1
for i in range(n):
    if i % 2 == 0:
        if a[l] > a[r]:
            s += a[l]
            l += 1
        else:
            s += a[r]
            r -= 1
    else:
        if a[l] > a[r]:
            d += a[l]
            l += 1
        else:
            d += a[r]
            r -= 1
print(s,d)