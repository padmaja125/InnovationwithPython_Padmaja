l=[]
for i in range (1,31):
    square = i ** 2
    l.append(square)
x = l[:5]
y =l[-5:]
z = x + y 
print(z)

# Method-2

list2 = []
for i in range(1,31):
    if (i in range(1,6) or i in range(25,31)):
        list2.append(i**2)
print("List: ", list2)
