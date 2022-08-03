"""
Python series
Date : 23-02-2021
25. Ерікті аргументтер | Arbitrary arguments - Python Қазақша

def function_name(parameter list):
    '''docstring'''
    statement
    statement(s)
"""

'''
def salemdesu(*args):
    Kazaksha salemdesu
    for esim in args:
        print('Salem,', esim, 'kalaisyng?')


salemdesu("Akmaral", "Dina", "Sultan")
'''


def kosu(*args):
    '''Berilgen sandardy kosu'''
    result = 0
    for san in args:
        result = result + san
    print("Berilgen sandardyng kosyndy:", result)


kosu(10, 20, 30, 40)
