class Shape:
    def area(self):
        x = 0
        print("area of the shape : ", x)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        x = self.length * self.length
        print("area of the shape : ",x)

a = Shape()
a.area()
b = Square(21)
b.area()
