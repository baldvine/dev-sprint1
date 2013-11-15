from TurtleWorld import *

world = TurtleWorld()			
bob = Turtle()				

bob.delay=0.0001
bob.set_color('green')

def drawSillyLines(t,length,n):
    if n==0:
    	return
    angle=50
    fd(t,length*n)
    lt(t,angle)
    draw(t,length,n-1)
    rt(t,2*angle)
    draw(t,length,n-1)
    lt(t,angle)
    bk(t,length*n)

#drawSillyLines(bob,10,6) Ok, draws a silly pattern using recursion

def drawKoch(someTurtle,length):
    if length<3:
        someTurtle.fd(length)
    else:
        drawKoch(someTurtle,length/3)
    
    someTurtle.lt(60)

    if length<3:
        someTurtle.fd(length)
    else:
        drawKoch(someTurtle,length/3)
    
    someTurtle.rt(120)
    
    if length<3:
        someTurtle.fd(length)
    else:
        drawKoch(someTurtle,length/3)
    
    someTurtle.lt(60)
    if length<3:
        someTurtle.fd(length)
    else:
        drawKoch(someTurtle,length/3)


#Move into a convenient location for the Koch curve:
bob.pu()
bob.bk(120)
bob.pd()
drawKoch(bob,100.0) #Works

wait_for_user()