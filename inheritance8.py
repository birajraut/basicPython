from __future__ import print_function
import math

class Shape():
    def __init__(self):
        self.color='red'
        self.sides=0
    def calArea(self):
        return 0
class Quadrilateral(Shape):
    def __init__(self,w,l,c):
        self.sides=4
        self.width=w
        self.length=l
        self.color=c
    def calArea(self):
        return self.width*self.length

class Square(Quadrilateral):
    def __init__(self,w,c):
        Quadrilateral.__init__(self,w,w,c)
class Circle(Shape):
    def __init__(self,r,c):
        Shape.__init__(self)
        self.radius=r
        self.color=c
    def calArea(self):
        return self.radius
class Triangle(Shape):
    def __init__(self,s1,s2,s3,c):
        Shape.__init__(self)
        self.side1=s1
        self.side2=s2
        self.side3=s3
        self.color=c
def printArea(s):
        print(s.calArea())

sq1=Square(5,'green')
sq2=Square(9,'black')
c1=Circle(10,'orange')
T1=Triangle(3,4,5,'purple')

print('Square Size',sq1.width,'X',sq1.sides,sq1.color,',',sq2.width,'X',sq2.sides,sq2.color)
print('Circle',c1.radius,c1.color)

print(sq1.calArea())
print(c1.calArea())
print('Triangle Area',printArea(T1))