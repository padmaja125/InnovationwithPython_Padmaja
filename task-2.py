# Write a program in Python to perform the following operation:
# If a number is divisible by 3 it should print “Consultadd” as a string
# If a number is divisible by 5 it should print “Python Training” as a string
# If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a
# string.
x = int(input("Enter the number : "))
if x % 3 == 0 and x % 5 == 0:
    print ("Consultadd - Python Training")
elif x % 3 == 0:
    print ("Consultadd")
elif x %5 ==0 :
    print("Python Training")
else:
    print ("enter the proper number")

# Write a program in Python to perform the following operator based task:
# Ask user to choose the following option first:
# If User Enter 1 - Addition
# If User Enter 2 - Subtraction
# If User Enter 3 - Division
# If User Enter 4 - Multiplication
# If User Enter 5 - Average
#Ask user to enter two numbers and keep those numbers in variables num1 and num2
#respectively for the first 4 options mentioned above.
#Ask the user to enter two more numbers as first and second for calculating the average as
#soon as the user chooses an option 5.
#At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
#NOTE: At a time a user can only perform one action.


select = int(input("Enter the number from (1-5): "))
if select in range(1,5):
    x = int(input(" Enter the 1st value : "))
    y = int(input("Enter the 2nd value : "))
    if select <=5 and select >= 0:
        if select == 1:
            print("Addition")
            z = x + y
        elif select == 2:
            print("Subtraction")
            z = x - y
        elif select == 3:
            print("Division")
            z = x / y           
        elif select == 4:
            print("Multiplication")
            z = x * y
        else :
            print("Average")
            a = int(input("Enter two more number for average separated by (,) :")
            list = a.split(,)
            list1 = list.append(x,y)
            sum = 0
            for i in list:
                sum += i
            z = sum / (len(list1) 
    else:
        print("you entered wrong option")
    if z < 0:
        print('Negative')
    else:
        print("Result :", z)
    
# Write a program in Python to implement the given flowchart
a, b, c = 10, 20, 30
avg = (a + b + c) / 3
if avg > a and avg > b and avg > c :
    print(avg, "is greater than a =", a, ", b = ", b, ' and c = ', c)
elif avg > a and avg > b :
    print(avg, "is greater than a = ", a, ' and b = ', b)
elif avg > a and avg > c :
    print(avg, 'is greater than a = ', a, ' and c = ', c)
elif avg > b and avg > c :
    print (avg, " is greater than b =", b, ' and c = ', c)
elif avg > a :
    print (avg, " is greater than a =", a)
elif avg > b :
    print(avg, "is greater than b = ", b)
else :
    print (avg, " is greater than c = ", c)

# 4. Write a program in Python to break and continue if the following cases occurs:
# If user enters a negative number just break the loop and print “It’s Over”
# If user enters a positive number just continue in the loop and print “Good Going”

print ("You entered the loop")
while True:
    x = int (input("Enter the number : "))
    if x > 0:
        print (" Good going")
        continue 
    else :
        print ("It's over")
        break

# Write a program in Python which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200.

for x in range (2000,3201) :
    if x % 7 == 0 and x % 5 != 0:
        print (x) 

# What is the output of the following code examples
"""
x=123
for i in x:
    print(i)

print ("TypeError: 'int' object is not iterable")
"""
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

# output: 0
#error
#1
#error
#2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break
# Output: "NameError: name 'Break' is not defined"
# Reason : B in the break is capital

# Write a program that prints all the numbers from 0 to 6 except 3 and 6.
# Expected output: 0 1 2 4 5
for x in range (0,7):
    if x == 3 or x == 6:
        continue
    print(x, end = " ")

# Write a program that accepts a string as an input from the user and calculate the number of digits
# and letters.

x = input("Enter the message : ")
numbers = sum(c.isdigit() for c in x)
letters = sum(c.isalpha() for c in x)
print ("Numbers = ",numbers, ", letters = ", letters)

# Write a program such that it asks users to “guess the lucky number”. If the correct number is
# guessed the program stops, otherwise it continues forever.
# Modify the program so that it asks users whether they want to guess again each time. Use two
# variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want
# to continue guessing. The program stops if the user guesses the correct number or answers “no”. (
# The program continues as long as a user has not answered “no” and has not guessed the correct
# number)
x = 1
while x:
    answer = input('Do you want to guess the no (Y/N) : ')
    if answer == 'Y' or answer == 'y':
        number = int(input('guess the lucky number : '))
        if number == 10 :
            print('correct ans')
            x = 0
        else:
            x = 1
    else:
        x = 0
# For 10 
counter = 5
lucky_number = 10

while counter > 0:
    a = int(input("Guess the lucky number: "))
    if a == lucky_number:
        print("Good guess!")
        break

    elif counter == 1:
        print("Game over!")
        break

    else:
        print("Try again!")
    counter -= 1                    
                       
                       
                       
 # For  11                      
                       
                       
x = 1
while x :
    guess = input('Do you want to enter the game(Y/N) : ')
    if guess == 'Y' or guess == 'y':
        counter =1
        while counter <= 5:
            print("Type in the", counter, "number")
            global number
            number = int(input('Enter the number : '))
            counter = counter +1
            if number == 10 :
                print("Good Guess")
                break
            else:
                print("Try again!")
        if number == 10:
            print ('Game Over')
        else :
            print("Sorry but that was not very successful")
    else:
        print('See you later')
        x = 0
