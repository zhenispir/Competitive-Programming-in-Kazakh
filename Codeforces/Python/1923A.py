def count_zeros_between_ones(chips):
    chips_str = ''.join(map(str, chips)).strip('0')
    
    return chips_str.count('0')


t = int(input())
for i in range(t):
    n = int(input())
    chips = list(map(int, input().split()))
    print(count_zeros_between_ones(chips))
