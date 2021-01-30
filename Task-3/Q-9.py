a_dict = {}
def create_dict(n):
    for x in range (1,n+1):
        b_dict = {x : x* x} 
        a_dict.update(b_dict)
    return a_dict
create_dict(5)
print (a_dict)