n = int(input())

a = list(map(int, input().split()))

if len(a) == len(set(a)):
    print(False)
else:
    print(True)