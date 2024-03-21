a = int(input())
maxx = 0
while a:
    digit = a % 10
    if digit > maxx:
        maxx = digit
    a = a // 10
print(maxx)