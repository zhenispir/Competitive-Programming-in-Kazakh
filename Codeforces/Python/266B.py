n, m = map(int, input().split())
a = input()
b = 0
for i in range(m):
    a = a.replace('BG', 'GB')
print(a)