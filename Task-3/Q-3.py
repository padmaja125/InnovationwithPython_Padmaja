from functools import reduce
list = [18,20,30,70,90]
print(sum(list))
y = 1
for x in list:
    y = x * y
print (y)
result1 = reduce((lambda x, y: x * y), list)
print(result1)

