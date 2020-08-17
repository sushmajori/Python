"""
PROGRAM TO CALCULATE THE DISTANCE BETWEEN TWO POINTS USING STATIC METHOD
"""

import math
class point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x > 0:
            self.__x = x
        else:
            raise Exception ("Invalid")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if y > 0:
            self.__y = y
        else:
            raise Exception ("Invalid")
    
    @staticmethod
    def distance(p1,p2):
        dist=math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
        return dist

    def display(self):
        print "x: ", self.x
        print "y: ", self.y
    

print "Point 1:"
pt1x=input("Enter x co-ordinate of point 1: ")
pt1y=input("Enter y co-ordinate of point 1: ")
p1=point(pt1x,pt1y)
print "Point 2:"
pt2x=input("Enter x co-ordinate of point 2: ")
pt2y=input("Enter y co-ordinate of point 2: ")
p2=point(pt2x,pt2y)
distan=point.distance(p1,p2)
print "Point 1:"
p1.display()
print "Point 2:"
p2.display()
print "Distance: ", distan

"""
Requirements: Python 2.7 Interpreter
"""

