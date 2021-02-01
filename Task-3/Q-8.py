a = {1:10,2:20}
b = {3:30, 4:40}
c = {}
c.update(a)
c.update(b)
print(c)

# method-2
a = {1:10,2:20}
b = {3:30,4:40}
d = {}
for c in (a,b):
    d.update(c)
print(d)

# method-3
a = {1 : 10, 2 : 20}
b = {3 : 30, 4 : 40}
c = {**a,**b} # **kwargs allows you to pass keyworded variable length of arguments to a function
print(c)

