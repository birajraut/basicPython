from __future__ import print_function

class Shape():
    def __init__(self):
        self.color='red'
        self.sides=0
class Square(Shape):
    def __init__(self,w,c):
        Shape.__init__(self)
        self.width=w
        self.color=c

sq1=Square(5,'green')
sq2=Square(9,'black')

print('Square Size',sq1.width,'X',sq1.sides,sq2.sides,sq2.color)