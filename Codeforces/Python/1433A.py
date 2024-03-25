t = int(input())
for i in range(t):
    n = (input())
    if len(n) == 1:
        print(n)
    elif len(n) == 2:
        print(9+int(n[0])*2)
    elif len(n) == 3:
        print(+int(n[0])*3)
    else:  
        print(9+18+27+int(n[0])*4)