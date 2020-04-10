# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print (arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myfunc(*argv):
    for i in argv:
        print(i)
myfunc('kiki', 'hehe', 'haha')


# *kargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))

myFun(first ='Geeks', mid ='for', last='Geeks')

#Using *args and **kwargs to call a function

def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("coffee", "milk", "juice")
myFun(*args)

kwargs = {"arg1" : "coffee", "arg2" : "milk", "arg3" : "juice"}
myFun(**kwargs)
