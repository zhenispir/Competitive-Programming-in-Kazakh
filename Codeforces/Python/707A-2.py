n, m = map(int, input().split())

color = '#Black&White'
for i in range(n):
    x = input()
    if ('Y' in x or 'C' in x or 'M' in x):
        color = '#Color'
print(color)