n = int(input())
while n > 0:
    s = input()
    print('A' if s.count('A')>s.count('B') else 'B')
    n -= 1
