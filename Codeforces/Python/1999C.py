def can_shower(n, s, m, intervals):
    if intervals[0][0] >= s:
        return "YES"

    for i in range(1, n):
        if intervals[i][0] - intervals[i-1][1] >= s:
            return "YES"

    if m - intervals[-1][1] >= s:
        return "YES"
    
    return "NO"

t = int(input())
results = []

for _ in range(t):
    n, s, m = map(int, input().split())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((l, r))
    
    intervals.sort()

    result = can_shower(n, s, m, intervals)
    results.append(result)

for result in results:
    print(result)
