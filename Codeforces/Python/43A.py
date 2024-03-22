n = int(input())
x=[]
for i in range(n):
    x.append(input())

x.sort()
print(x[0] if x.count(x[0])>x.count(x[-1]) else x[-1])