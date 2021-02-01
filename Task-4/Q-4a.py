def my_min_function(somelist):
    min_value = None
    for value in somelist:
        if not min_value:
            min_value = value
        elif value > min_value:
            min_value = value
    return min_value

list=[50,6,25,70,2,7,93]
print(my_min_function(list))

list = [x for x in list if x%2!=0]
print(list)

l=[]
for i in range (1,31):
    square = i ** 2
    l.append(square)
x = l[:5]
y =l[-5:]
z = x + y 
print(z)