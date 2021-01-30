use4_input = int(input('Enter the number:  '))
try :
    x =str(use4_input)
    if len(x) == 4:
        print('proceed')
    else:
        raise ValueError
except ValueError as ve :
    print(ve,'The length is too short/long !!! Please provide only four digits”') 

