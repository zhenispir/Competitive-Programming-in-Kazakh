n, k = map(int, input().split())

if k <= (n + 1) // 2:
    result = 2 * k - 1
else:
    result = 2 * (k - (n + 1) // 2)

print(result)
