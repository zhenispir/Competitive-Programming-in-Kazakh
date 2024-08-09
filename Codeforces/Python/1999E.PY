def count_operations_to_zero(n):
    operations = 0
    while n != 0:
        if n % 3 == 0:
            n //= 3
        else:
            n *= 3
        operations += 1
    return operations

def minimum_operations(l, r):
    total_operations = 0
    for number in range(l, r + 1):
        total_operations += count_operations_to_zero(number)
    return total_operations

# Read number of test cases
t = int(input())
results = []

for _ in range(t):
    l, r = map(int, input().split())
    results.append(minimum_operations(l, r))

# Print all results
for result in results:
    print(result)
