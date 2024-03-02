t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_val = max(a)
    min_val = min(a)
    print(max(abs(max_val - a[0]) + abs(a[0] - a[-1]) + abs(a[-1] - min_val), abs(min_val - a[0]) + abs(a[0] - a[-1]) + abs(a[-1] - max_val)))