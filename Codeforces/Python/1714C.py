'''
Name: Minimum Varied Number
Link: https://codeforces.com/problemset/problem/1714/C
Categories:
'''
t = int(input())
slist = []
for i in range(t):
    slist.append(int(input()))

# esas cozum
final = []
for i in range(t):
    final.append([])
    for nz in range(9, 0, -1):  # senin metodu biraz degistirdim
        if slist[i] - nz >= 0:  # nz means 'nine to zero'
            final[i].append(nz)
            slist[i] -= nz


def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
# source for reversing list: https://www.geeksforgeeks.org/python-reversing-list/


for i in range(t):
    print(*Reverse(final[i]), sep="")
