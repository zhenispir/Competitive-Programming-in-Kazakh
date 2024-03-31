def solve(a, b):
    side = min(max(a * 2, b), max(a, b * 2))
    return side * side

t = int(input())  # Read the number of test cases
for _ in range(t):
    a, b = map(int, input().split())  # Read the values of a and b for each test case
    print(solve(a, b))  # Print the result of the solve function
