def longlen (get1, get2):
    x = len(get1)
    y = len(get2)
    if x > y:
        print (get1)
    elif x == y:
        print(get1 , get2)
    else :
        print (get2)

get1 = input('enter the 1st string :')
get2 = input('enter the 2nd string :')
longlen(get1,get2)