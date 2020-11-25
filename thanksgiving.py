from turtle import *
tut = Turtle()
screen = Screen()
screen.setup(720, 720)
screen.bgcolor("orange")

tut.shape("turtle")
def moveTurtle(aTurtle,xcoord,ycoord):
    aTurtle.penup()
    aTurtle.goto(xcoord,ycoord)
    aTurtle.pendown()
def drawCircle(aTurtle,aColor,radius,degrees):
    if aColor != "none":
        aTurtle.fillcolor(aColor)
        aTurtle.begin_fill()
        aTurtle.circle(radius,degrees)
        aTurtle.end_fill()
    else:
        aTurtle.circle(radius,degrees)

#Pre: aTurtle, sideLen, and aColor are valid and exist.
#Post: A triangle (the turkey's beak) is drawn.
def drawBeak(aTurtle,sideLen,aColor):
    aTurtle.fillcolor(aColor)
    aTurtle.begin_fill()
    aTurtle.forward(sideLen)
    aTurtle.right(120)
    aTurtle.forward(sideLen)
    aTurtle.right(120)
    aTurtle.forward(sideLen)
    aTurtle.end_fill()

#Pre: aTurtle exists and is valid.
#Post: The turkey's feathers are drawn with different color filling.
def drawFeathers(aTurtle,InitialX,InitialY):
    aTurtle.left(35)
    for aColor in ["red","yellow","light blue","green","light pink"]:
        moveTurtle(aTurtle,InitialX,InitialY)
        drawOvalShape(25,160,aTurtle,190,aColor)
        aTurtle.right(165)

#Pre: circRadius, AmntFrwd, aTurtle, circDegrees, and aColor all exist and are valid.
#Post: An oval shape (straight line, part of a circle, straight line) is drawn.
def drawOvalShape(circRadius,AmntFrwd,aTurtle,circDegrees,aColor):
    aTurtle.fillcolor(aColor)
    aTurtle.begin_fill()
    aTurtle.forward(AmntFrwd)
    drawCircle(aTurtle,"none",circRadius,circDegrees)
    aTurtle.forward(AmntFrwd)
    aTurtle.end_fill()

#Pre: aTurtle exists and is valid.
#Post: One of the turkey's legs is drawn.
def drawLeg(aTurtle):
    aTurtle.left(50)
    drawOvalShape(8,40,aTurtle,180,"yellow")
    aTurtle.right(90)
    CurrentX,CurrentY = aTurtle.position()
    moveTurtle(aTurtle,CurrentX-8,CurrentY+8)
    drawOvalShape(8,40,aTurtle,180,"yellow")
    aTurtle.right(40)
    drawOvalShape(8,45,aTurtle,180,"yellow")
    drawOvalShape(8,45,aTurtle,180,"yellow")

#Pre: aTurtle,Xcoord, and Ycoord exist and are valid.
#Post: Two turkey legs are drawn.
def drawTurkeyLegs(aTurtle,Xcoord,Ycoord):
    moveTurtle(aTurtle,Xcoord,Ycoord)
    drawLeg(aTurtle)
    CurrentX,CurrentY = aTurtle.position()
    moveTurtle(aTurtle,CurrentX+130,CurrentY)
    aTurtle.left(105)
    drawLeg(aTurtle)

#Pre: aTurtle exists and is valid.
#Post: The problem statement is solved and a turkey is drawn.
def drawTurkey(aTurtle,initialX,initialY):
    drawFeathers(aTurtle,initialX,initialY)

    drawTurkeyLegs(aTurtle,initialX-70,initialY-120)

    aTurtle.right(105)
    aTurtle.color("black")
    moveTurtle(aTurtle,initialX,initialY-110)
    drawCircle(aTurtle,"brown",100,360) #body

    aTurtle.right(100)
    moveTurtle(aTurtle,initialX-10,initialY+80)        #neck
    drawOvalShape(25,100,aTurtle,200,"dark red")

    aTurtle.right(100)
    moveTurtle(aTurtle,initialX,initialY+40)
    drawCircle(aTurtle,"maroon",40,360) #head

    for i in [-15,15]:
        moveTurtle(aTurtle,initialX+i,initialY+88)
        drawCircle(aTurtle,"grey",8,360)    #eye

    moveTurtle(aTurtle,initialX-10,initialY+80)    #beak
    drawBeak(aTurtle,20,"yellow")

def make_triangle(x, y, color):
  tut.penup()
  tut.goto(x,y)
  tut.begin_fill()
  tut.color(color)
  tut.pendown()
  for count in range(3):
    tut.forward(50)
    tut.left(120)
  tut.end_fill()

def make_square(x, y, color):
  tut.penup()
  tut.goto(x,y)
  tut.begin_fill()
  tut.color(color)
  tut.pendown()
  for count2 in range(3):
    tut.forward(50)
    tut.left(90)
  tut.end_fill()

def petal(t, radius, angle):
    for i in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
        
def flower(t, n, radius, angle):
    for i in range(n):
        petal(t, radius, angle)
        t.left(360.0 / n)

def move(t, length):
    window = turtle.Screen()
    window.bgcolor("Yellow")
    t.pu()
    t.fd(length)
    t.pd()
tut.shape("blank")

drawTurkey(tut,-50,-30)

tut.penup()
tut.goto(320,-50)
tut.color('#ff6600')
tut.begin_fill()
tut.circle(100)
tut.end_fill()
tut.left(180)

# The Teeth:
make_triangle(180, -130, '#ffffff')
make_triangle(210, -130, '#ffffff')
make_triangle(240, -130, '#ffffff')
# tut.left(180)

# The Eyes:
make_triangle(180, -30, '#ffffff')
make_triangle(250, -30, '#ffffff')

make_square(200, 20, '#663300')

tut.penup()
tut.goto(-240,-300)
tut.color("black")

tut.write('Happy Thanksgiving!', font=("Comic Sans MS",35,"bold"))

