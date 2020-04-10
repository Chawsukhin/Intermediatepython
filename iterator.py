mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "apple"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple=("apple", "banana","cherry")
for i in mytuple:
    print(i)

#create an object/class as an iterator
class mynum():
    def __iter__(self):
        self.x=1
        return self
    def __next__(self):
        y=self.x
        self.x +=1
        return y
myclass=mynum()
myiter=iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))      
