
try:
    print eval('six times seven')
except SyntaxError, err:
    print ('Syntax error', err)

# method-2
try:
    eval('x === x')
except SyntaxError:
    print ("You cannot do that")
    
 # method-3
try:
    eval('a <> b')
except SyntaxError:
    print("Syntax Error")
