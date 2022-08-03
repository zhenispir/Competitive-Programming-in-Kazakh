"""
Python series
Date : 01-03-2021
27. Екі өлшемді массивтерді шығару | Printing two dimensional arrays - Python Қазақша
"""

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

for row in a:
    for element in row:
        print(element, end=' ')  # !!!!!!!!!!!
    print()
