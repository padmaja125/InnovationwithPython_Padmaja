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

import sys
print("First value", sys.argv[0])
print("All values")
for i, x  in enumerate(sys.argv):
    print(i, x)
    
