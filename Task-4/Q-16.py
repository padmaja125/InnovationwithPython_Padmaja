def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)

# output: 2

def a():
    try:
        f(x,4)
    finally:
        print('after f')
        print('after f?')

a()
"""
 output: after f
after f?
Traceback (most recent call last):
  File "c:/Data/Padhu/Training/Assignment/Functions_assignment/Q-16.py", line 18, in <module>
    a()
  File "c:/Data/Padhu/Training/Assignment/Functions_assignment/Q-16.py", line 13, in a
    f(x,4)
    """
    