# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def GeneratorFun():
    yield 1
    yield 2
    yield 3

# Driver code to check above generator function
for value in GeneratorFun():
    print(value)
