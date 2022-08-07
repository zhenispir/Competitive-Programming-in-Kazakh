'''
Anton and Polyhedrons
https://codeforces.com/problemset/problem/785/A
array, dictionary, loop
'''

# polygons = polygon names and number of faces dictionary
polygons = {"Tetrahedron": 4,
            "Cube": 6,
            "Octahedron": 8,
            "Dodecahedron": 12,
            "Icosahedron": 20, }

# n = length of an array, a = empty list, sum = total number of faces
a = []
n = int(input())
for i in range(n):
    a.append(input())  # adding each element to empty list
sum = 0

# checking every item in the list and add number of faces
for i in range(n):
    sum = sum + polygons[a[i]]
    # polygons - dictionary [a = filled list[values of a]]

print(sum)
