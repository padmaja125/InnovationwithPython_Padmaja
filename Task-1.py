# Create three variables in a single line and assign values to them in such a manner that each one of
# them belongs to a different data type.

a,b,c = 1, 2.01, 'string'
print('a =',a )
print('b =',b)
print('c =',c)

# Create a variable of type complex and swap it with another variable of type integer.

x = 7 + 9j
y = 10
print('x before swap is ',x)
print('y before swap is',y)
z = x
x = y
y = z
print('x after swap =',x)
print('y after swap=', y)

# Swap two numbers using a third variable and do the same task without using any third variable.

x, y = 21, 12
print('Before swap x  = {0} , y = {1}'.format(x, y) )
# with third variable
z = x
x = y
y = z
print ('After swap using third variable x = {0} , y = {1}'.format(x, y))

# without 3rd variable
x, y = 21, 12
print('Before swap x  = {0} , y = {1}'.format(x, y)
x = x + y
y = x - y
x = x - y
#x,y = y,x
print('After swap without third variable x = {0} , y = {1}'.format(x, y))

# Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x
# Version.
x = raw_input(' Enter the value : ')
y = input ('Enter the values ')
print (y)
# in version 2.x ==> print x

# Write a program to complete the task given below:
# Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
# another variable called z. Add 30 to z and store the output in variable result and print result as the
# final output.

x = int(input('Enter the values between 1-10 : '))
y = int(input('Enter the values between 1-10 : '))
z = x + y
result = z + 30
print(result)

# Write a program to check the data type of the entered values.
x = 10
y = 2.6
z = 'string'
a = 2 + 3j
print ('type for 10 :',eval(x))
print ('type for 2.6 :',eval(y))
print ('type for string :',type(z))
print ('type for 2 + 3j :',type(a))

# Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and
# UPPERCASE.
userName = 'lowerCamelCase'
UserName = 'UpperCamelCase'
user_name01 = 'SnakeCase'
USERNAME01 = 'UPPERCASE'

# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’
# again. Will it change the value? If Yes then Why?
an = 10
an = 'abc'
print(an)

# Yes, because python variable  is used for storing the value. We can retrieve same value many times. 
 # If we assigned new value to the same variable then it erases the old value form that variable.


