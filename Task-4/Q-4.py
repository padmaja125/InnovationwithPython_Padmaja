get = input("Enter the string with hyphen separated : ")
a = get.split('-')
def sorting(x):
    for i in range(len(x)+1):
        for j in range(len(x)-1):
            if x[j][0] > x[j+1][0]:
                x[j],x[j+1] = x[j+1],x[j]
    string = ('-').join(x)
    print('After sorting :',string)


print(sorting(a))
"""
def sorting(get):
    a = get.split('-')
    b = a.sort()
    return ('-').join(b)

print(sorting(get))
"""