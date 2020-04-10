def func1(name):
   print ('Hello', name)

def func2(func1):
   name = 'John'
   return func1(name)

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b
print(divide(2,5))



def repeater(old_function):
    def new_function(*args, **kwds):
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value

@repeater
def multiply(num1, num2):
    print(num1 * num2)
