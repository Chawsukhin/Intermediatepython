class over:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, x):
        return self.a + x.a
ob1 = over(5)
ob2 = over(6)
ob3 = over("Good")
ob4 = over("Morning")

print(ob1 + ob2)
print(ob3 + ob4)


# a comparison operators
class greater:
    def __init__(self, x):
        self.x = x
    def __gt__(self, other):
        if(self.x>other.x):
            return True
        else:
            return False
ob1 = greater(2)
ob2 = greater(3)
if(ob1>ob2):
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")
