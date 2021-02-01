"""
my_list = [int(x) for x in input('Enter the numbers :').split(',')]
C, H, x = 50, 30, []

for D in my_list:
    Q = ((2*C*D)/H)**(1/2)
    x.append(round(Q))

print(','.join(map(str, x)))


import math


class sqroot(object):
    def __init__(self, c, h):
        self.c = c
        self.h = h

    def q(self):
        numbers = input("Enter numbers separated by comma: ")
        numbers = numbers.split(',')
        result_list = []

        for d in numbers:
            result_list.append(round(math.sqrt(2 * self.c * int(d) / self.h)))
        return result_list

x = sqroot(50, 30)
print(x.q())
"""
# method -2
class sq2:
    def __init__(self):
        self.C = 50
        self.H = 30

    def q(self):
        my_list = [int(x) for x in input('Enter the numbers :').split(',')]
        x = []

        for D in my_list:
             Q = ((2*self.C*D)/self.H)**(1/2)
             x.append(round(Q))
        return x

ans = sq2()
print(ans.q())

