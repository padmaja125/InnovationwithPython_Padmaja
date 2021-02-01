name = input("Enter the file name: ")
fobj = open(name)
print(fobj.read())
fobj.close()
# with try and except block
from sys import argv

nop, fn = argv
print('name of program: ', nop)
print('name of file: ',fn)
try:
    while True:
        fh = open(fn, 'r')
        c = fh.readline()
        print(c)
        fh.close()
        break
except:
    print('Please enter the name again.')
