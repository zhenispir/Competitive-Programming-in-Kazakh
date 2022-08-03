"""
Python series
Date : 10-03-2021
30. Жоғары Ретті Функциялар | Higher Order Functions - Python Қазақша

In fact, in Python, Higher-Order Functions are functions that do at least one of
the following (and may do both):
• Take one or more functions as a parameter,
• Return as a result a function.

Python тілінде Жоғары ретті функциялар деп төмендегілердің кем дегенде біреуін 
орындайтын функциялар болып табылады:
• Параметр ретінде бір немесе бірнеше функцияларды алыңыз,
• Нәтиже ретінде функцияны қайтару.
"""


def beskos(x):
    return x + 5


def kurdeli(a, func):
    return func(a)


print(kurdeli(50, beskos))
