a,b = map(int, input().split())
count=0
for i in range(a,b+1):
    if str(i).count('4'):
        count+=1

print(count if count else -1)