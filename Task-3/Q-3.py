from functools import reduce
list = [18,20,30,70,90]
print(sum(list))
y = 1
for x in list:
    y = x * y
print (y)
result1 = reduce((lambda x, y: x * y), list)
print(result1)

# Method-2
list=[18,20,30,70,90]
a=0;
b=1;
for i in range(len(list)):
    a = a+ list[i] # addition of all numbers in list
    b = b*list[i] #multiplication of all numbers in list
print("Sum: ",a)
print("Multiplication: ",b)

# Method-3
from functools import reduce
List=[18, 20, 30, 70, 90]
addition = reduce((lambda a,b:a+b), List)
print(addition)
multiplication = reduce((lambda a,b:a*b), List)
print(multiplication)
