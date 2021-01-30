
"""
Decorators:

1. Nested functions
2. Function returning function
3.reference function(object of the function)
4.function taking function as a parameter
"""
# Decorator without passing parameter
def deco_upper(function):
    def uppercase():
        str1 = function()
        return str1.upper()
    return uppercase()
@deco_upper # used to call decorator without calling the function/method
def string():
    return 'Welcome Decorator'
"""
obj = deco_upper(string)
print(obj)
"""
print(string)

# decorator with parameter
def deco_division(function):
    def change(no1,no2):
        if no2 < no1:
            no1,no2 = no2,no1
        return function(no1,no2)
    return change

@deco_division
def division(no1,no2):
    return no1/no2

print(division(7,1))
print(division(1,7))