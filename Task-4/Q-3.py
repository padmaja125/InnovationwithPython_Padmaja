def uniquelist(n):
    lst = []
    for a in n :
        if a not in lst:
            lst.append(a)
    return lst

lst1 = [21,'a',73,'a',21,7,9,7,21]
print(uniquelist(lst1))
