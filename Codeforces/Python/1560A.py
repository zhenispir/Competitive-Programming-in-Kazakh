t = int(input())

while t > 0:
    k = int(input())
    num = 0
    while k > 0:
        num += 1
        if num % 3 != 0 and num % 10 != 3:
            k -= 1
    print(num)
    t -= 1
