
r = filter(lambda x : x % 7 == 0 and x %3 !=0, [21,37,46,78,20,14,28,35])
print(list(r))

# with higher order function method 
def mutipleof7(x):
    return x%7 ==0 and x %3 !=0

r = filter(mutipleof7,[21,37,46,78,20,14,28,35])
print(list(r))
