class Person():
    def __init__(self,startage):
        if startage < 0:
            print("Age is not valid,setting age to 0")
            self.age = 0
        else:
            self.age = startage

    def yearPasses(self,incr):
        self.age +=incr
        return self.age

    def amIOld(self):
        if self.age >0:
            if self.age <13:
                print('You are young')
            elif self.age >=13 and self.age <=19:
                print('You are a teenager')
            else:
                print('You are Old')
    


lst = [-1, 4, 10, 16, 18, 64, 38]
try:
    for i in lst:
        startage = i
        p = Person(startage)
        p.amIOld()
except  ValueError as ve:
    print(ve)   

p=Person(38)
x =p.yearPasses(4)
print('Expected year of pass is :', x)