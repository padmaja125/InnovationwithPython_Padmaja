def showNumbers(n):
    for i in range (0,n):
        if i % 2 == 0:
            print(i, 'EVEN')
        else:
            print(i, 'ODD')

n = int(input("How many no's you want to find: "))
showNumbers(n)