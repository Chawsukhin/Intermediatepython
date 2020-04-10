f=open("example.txt","r")
print(f.read())


f=open("example.txt","r")
print(f.read(5))


f = open("example.txt", "r")
print(f.readline())
print(f.readline())
f.close()


f=open("example.txt","w")
f.write("Good Morning Chaw Su Khin!")
f.close()

#open and read the file after the appending:
f=open("example.txt", "r")
print(f.read())
f.close()


import os
if os.path.exists("eg.txt"):
  os.remove("eg.txt")
else:
  print("The file does not exist")


class context():
    def __init__(self):
        print("init method is called")
    def __enter__(self):
        print("enter method is called")
        return self
    def __exit__(self,exc_type, exc_value, exc_traceback):
        print("exit method is called")

with context() as manager:
    print("with statement blocked")


# file management using
# context manager
class File():
    def __init__(self, filename, mode):
        self.filename=filename
        self.mode=mode
        self.file=None
    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

with File("test.txt","w") as fs:
    fs.write("Hi Hi Hi")
print(fs.closed)
