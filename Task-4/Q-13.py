from functools import reduce
r = reduce(lambda x,y : str(x)+str(y),[1,2,3,4,5,6,7])
print(r)