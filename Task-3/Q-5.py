lst = [12, 30, 7, 15, 22]
y = []
for x in lst:
    if (x % 2) !=0:
        y.append(x)
print (y)

# Method-2
list = [x for x in lst if x%2 != 0]
print(list)

