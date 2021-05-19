import math
import turtle

#draw a circle using turtle
def drawCircleTurtle(x, y, r):
    #move to the start of circle
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

#draw the circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))

drawCircleTurtle(100, 100, 50)
turtle.mainloop()

# a class that draws a spirograph
class Spiro:
    #constructor
    def __init__(self, xc, yc, col, R, r, l):
        
        #create the turtle object
        self.t = turtle.Turtle()
        # set the cursor shap
        self.t.shape('turtle')
        #set the step in degrees
        self.step = 5
        #set the drawing complete flag
        self.drawingComplete = False
        
        # set the parameters
        self.setparams(xc, yc, col, R, r, l)
        
        # initialize the drawing
        self.restart()

# set the parameters
def setparams(self, xc, yc, col, R, r, l):
    # the Spirograph parameters
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l
    self.col = col
    #reduce r/R to its smallest form by dividing with the GCD
    gcdVal = gcd(self.r, self.R)
    self.nRot = self.r//gcdVal
    #get ratio of radii
    self.k = r/float(R)
    #set the color
    self.t.color(*col)
    #store the current angle
    self.a = 0

#restart the drawing
def restart(self):
# set the flag
    self.drawingComplete = False
        #show the turtle
    self.t.showtutrle()
        #go to the first point
    self.t.up()
    R, k, l, = self.R, self.k, self.l
    a = 0.0
    x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    self.t.down()
    
# draw the whole thing
def draw(self):
    #draw the rest of the points
    R, k, l, = self.R, self.k, self.l
    for i in range(0, 360*self.nRot + 1, self.step):
        a = math.radians(i)
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = y = R*((1-k)*math.sin(a) + l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
    #drawing is now done so hide the turtle cursor
    self.t.hideturtle()
# update one step
def update(self):
    # skip the rest of the steps if done
    if self.drawingComplete:
        return
    #incre