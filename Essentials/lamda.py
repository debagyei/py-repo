# syntax = lambda arguments: expression
 
number = lambda x, y: x+y
print(number(3,6))


def number(n):
    return lambda a:a*n

check = number(4)
print(check(33))
    