n = int(input())
a = list(map(int, input().split()))
tot=0
ans=0
for i in range(n):
    if a[i]==-1:
        if tot>0:
            tot-=1
        else:
            ans+=1
    else:
        tot+=a[i]
print(ans)