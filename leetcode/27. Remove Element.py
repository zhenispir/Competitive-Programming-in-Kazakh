t = int(input())
nums = list(map(int, input().split()))
val = int(input())

n = nums.count(val)

while n > 0:
    nums.remove(val)
    n -= 1

print(*nums)