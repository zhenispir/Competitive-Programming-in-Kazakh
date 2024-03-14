n = int(input())
h = []
for i in range(n):
    h.append(tuple(map(int, input().split())))
count = 0
for i in range(n):
    for j in range(n):
        if h[i][0] == h[j][1]:
            count += 1
print(count)