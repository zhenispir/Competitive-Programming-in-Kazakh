n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

#for i in range(n):
#    print(*matrix[i])

rotated_matrix = list(zip(*reversed(matrix)))
for i in range(m):
    print(*rotated_matrix[i])