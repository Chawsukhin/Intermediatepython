#nested function accessing a nonlocal variable
def print_output(msg):
    def output():
        print(msg)
    output()

print_output("Hello world!")

#return output function instead of calling it
def print_output(msg):
    def output():
        print(msg)
    return output
another=print_output("Hello Hello")
another()


def make_mutiplier(n):
    def multiplier(x):
        return x*n
    return multiplier

#make_mutiplier of 3
time3=make_mutiplier(3)

#make_mutiplier of 5
time5=make_mutiplier(5)

print(time3(9))

print(time5(3))

print(time3(time5(2)))

#higher order function
def increment(x):
    return x+1
def decrement(x):
    return x-1

def operate(func, x):
    result=func(x)
    return result

print("The result of increment:",operate(increment, 5))
print("The result of decrement:",operate(decrement, 5))
