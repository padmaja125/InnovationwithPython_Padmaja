"""
try:
    print eval('six times seven')
except SyntaxError, err:
    print ('Syntax error', err)
"""
try:
    eval('x === x')
except SyntaxError:
    print ("You cannot do that")