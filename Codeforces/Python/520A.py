'''
Name: Pangram
Link: https://codeforces.com/problemset/problem/520/A
Categories: string
'''

# n int, a string input
n = int(input())
a = input()

# lowercase given string and make it set
aset = set(a.lower())

if (len(aset)) == 26:
    print('YES')
else:
    print('NO')
