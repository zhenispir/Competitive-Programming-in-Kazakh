n = int(input())
a = input()
b = 0
for i in range(n-1):
    if a[i]==a[i+1]:
        b+=1

print(b)