'''
Name: Helpful Maths
Link: https://codeforces.com/problemset/problem/339/C
Categories: split string to list, then sort and merge list to string 
'''
s = input()

# splitting string by + and turn it into a list
alist = list(s.split("+"))

# sorting a list
alist.sort()

print(*alist, sep="+")
