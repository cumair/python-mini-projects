'''

In this problem you will use a pseudo random numbers to estimate the area of two overlapping ellipses.
An ellipse is a curve in a plane surrounding two focal points such that the sum of the distances to the two
focal points is constant for every point on the curve. – Wikipedia.

Create a Point class that takes the x and y coordinates of the point:

    p1 = Point(2,3)
    p2 = Point(4,3)

Create an Ellipse class that takes two points and the width of the long axis:

    e1 = Ellipse(p1,p2,4)

Write a function that takes two ellipses and returns the area of the overlap:

    overlap = computeOverlapOfEllipses(e1,e2)

This function should leverage the pseudo random number generator you built in the previous assignment.

'''


import math
import random

#****************************************************************************
class Point:
    'class that defines a Point'

    #****************************
    def __init__(self, xc=0,yc=0):
        'Initialize x and y variables'

        self.x = xc
        self.y = yc
        self.p = (xc,yc)
        
    #****************************
    def get_x(self):
        'gets x'

        return self.x

    #****************************
    def get_y(self):
        'gets y'

        return self.y

    #****************************
    def get_p(self):
        'gets a point'

        return (self.x, self.y)

    #****************************
    def distance(self, p2):
        'gets distance b/w 2 points'

        dif_x = p2.get_x() - self.get_x()
        dif_y = p2.get_y() - self.get_y()

        return math.sqrt(dif_x**2 + dif_y**2)

    #****************************
    def __repr__(self):
        'canonical representation of Point'

        return 'Point({}, {})'.format(self.x, self.y)

#****************************************************************************
class Ellipse():
    'class that takes two points and the width of the long axis'

    #****************************
    def __init__(self, x1=0,y1=0,x2=0,y2=0,w=0):
        'initialize f1 and f2'

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = w

        self.f1 = Point(self.x1, self.y1)
        self.f2 = Point(self.x2, self. y2)

    #****************************
    def get_f1(self):
        'gets f1'

        return self.f1

    #****************************
    def get_f2(self):
        'gets f2'

        return self.f2

    #****************************
    def get_w(self):
        'gets w'

        return self.w

    #****************************
    def get_pair(self):
        'gets a pair of f1 and f2'

        return (self.f1, self.f2)

    #****************************
    def circumference(self):
        'returns circumference'

        #a = semi-major
        #b = semi-minor

        self.a = self.f1.distance(self.f2)*.5 + (self.w - self.f1.distance(self.f2))*.5
        self.b = math.sqrt((0.5*self.w)**2 - ((0.5*self.f1.distance(self.f2))**2))
        
        return math.pi*(3*(a+b) - math.sqrt((3 * a+b) * (a+3 * b)))

    #****************************
    def inside(self, p):
        'returns True if point is inside boundary'
        
        if self.f1.distance(p) + self.f2.distance(p) < self.w:

            return True

    #****************************
    def __repr__(self):
        'canonical representation of ellipse'

        return '({}, {}), {}'.format(self.f1, self.f2, self.w)


#****************************************************************************
def computeOverlapOfEllipses(e1,e2):
    'computes and return the area of two overlapping ellipses'
    
    bf = buffer()
    lowRightX,lowRightY,upRightX,upRightY,lowLeftX,lowLeftY,upLeftX,upLeftY = box(bf)
    begin_X,end_X,begin_Y,end_Y = begin_end(lowRightX,lowRightY,upRightX,upRightY,lowLeftX,lowLeftY,upLeftX,upLeftY)
    ratio = overlap_ratio(begin_X,end_X,begin_Y,end_Y)

    lowRight = Point(lowRightX, lowRightY)          #lower Right point of the box
    upRight  = Point(upRightX, upRightY)            #upper Right point of the box
    lowLeft  = Point(lowLeftX, lowLeftY)            #lower left point of the box
    upLeft   = Point(upLeftX, upLeftY)              #upper left point of the box

    length1 = lowRight.distance(upRight)            #length of one side
    length2 = lowRight.distance(lowLeft)            #length of another side

    square_area = length1 * length2                 #area surrounding two ellipses

    return ratio * square_area                      #area of two overlapping ellipses 


#****************************************************************************
def ellipse_1(p1x,p1y,p2x,p2y,w):
    'returns an ellipse using Ellipse class'

    e1 = Ellipse(p1x,p1y,p2x,p2y,w)

    return e1


#****************************************************************************
def ellipse_2(p1x,p1y,p2x,p2y,w):
    'returns an ellipse using Ellipse class'

    e2 = Ellipse(p1x,p1y,p2x,p2y,w)

    return e2


#****************************************************************************
def buffer():
    'determines and returns buffer'

    widthOfe1 = e1.get_w()
    widthOfe2 = e2.get_w()

    if widthOfe1 > widthOfe2:
        bf = widthOfe1
    else:
        bf = widthOfe2

    return bf


#****************************************************************************
def single_test(p):
    'returns True if the Point is inside the boundary'

    if e1.inside(p) == True and e2.inside(p) == True:
        return True


#****************************************************************************
def box(bf):
    'determines and returns the coordinates of a box'

    lowRightX = max(e1.x1, e1.x2, e2.x1, e2.x2) + 0.5*bf    #lower right corner x
    lowRightY = min(e1.y1, e1.y2, e2.y1, e2.y2) - 0.5*bf    #lower right corner y   
    upRightX  = max(e1.x1, e1.x2, e2.x1, e2.x2) + 0.5*bf    #upper right corner x
    upRightY  = max(e1.y1, e1.y2, e2.y1, e2.y2) + 0.5*bf    #upper right corner y
    lowLeftX  = min(e1.x1, e1.x2, e2.x1, e2.x2) - 0.5*bf    #lower left corner x
    lowLeftY  = min(e1.y1, e1.y2, e2.y1, e2.y2) - 0.5*bf    #lower left corner y   
    upLeftX   = min(e1.x1, e1.x2, e2.x1, e2.x2) - 0.5*bf    #upper left corner x
    upLeftY   = max(e1.y1, e1.y2, e2.y1, e2.y2) + 0.5*bf    #upper left corner y

    return lowRightX,lowRightY,upRightX,upRightY,lowLeftX,lowLeftY,upLeftX,upLeftY


#****************************************************************************
def begin_end(lowRightX,lowRightY,upRightX,upRightY,lowLeftX,lowLeftY,upLeftX,upLeftY):
    'returns begin and end numbers'

    x_axis = [lowRightX, upRightX, lowLeftX, upLeftX]
    y_axis = [lowRightY, upRightY, lowLeftY, upLeftY]

    begin_X = int(min(x_axis))
    end_X = int(max(x_axis))
    begin_Y = int(min(y_axis))
    end_Y = int(max(y_axis))

    return begin_X,end_X,begin_Y,end_Y


#****************************************************************************
def overlap_ratio(begin_X,end_X,begin_Y,end_Y):
    'returns ratio of successful results from 10000 random points'

    counter = 0
    n = 10000
    
    for i in range(n):
        x = random.randint(begin_X, end_X)
        y = random.randint(begin_Y, end_Y)

        p = Point(x,y)

        if single_test(p) == True:
            counter += 1

    return counter/n

    
#****************************************************************************
e1 = ellipse_1(2,1,1,2,4)                       #get first Ellipse
e2 = ellipse_2(1,1,2,3,6)                       #get second Ellipse

overlap = computeOverlapOfEllipses(e1,e2)
print('The area of two overlapping ellipses is:', overlap)

