# we can pass funcs as argus to other funcs
def sum(n, func):
    total=0
    for num in range(n):
        total += func(num)
    return total

def square(x):
    return x*x
def cube(x):
    return x*x*x

print(sum(3, square))
print(sum(3, cube))

#nested function
from random import choice
def food(drink):
    def get_drink():
       msg=choice(('coffee', 'bubble', 'tea'))
       return msg
    result=get_drink() + drink
    return result
print(food("Milk"))
