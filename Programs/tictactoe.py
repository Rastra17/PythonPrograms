#A program to play tictactoe using turtle library

import turtle

screen=turtle.Screen()
screen.bgcolor("black")
screen.title("Tic Tac Toe")

pen=turtle.Turtle()
pen.shape("turtle")
pen.color("white")
pen.width(2)
pen.speed(10)
pen.shapesize(1)
pen.up()
pen.goto(100, 270)
pen.down()
pen.right(90)
pen.forward(535)
pen.up()
pen.goto(-100, 270)
pen.down()
pen.forward(535)
pen.right(90)
pen.up()
pen.goto(330, 100)
pen.down()
pen.forward(650)
pen.up()
pen.goto(330, -100)
pen.down()
pen.forward(650)
pen.up()
pen.goto(0, 0)

def cross():
    pen.down()
    pen.right(45)
    pen.forward(50)
    pen.back(100)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.back(100)
    pen.forward(50)
    pen.left(45)

def circle():
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.down()
    pen.circle(50)

counter=1

def count():
    global counter
    if (counter == 1):
        cross()
        counter = counter - 1
    else:
        circle()
        counter = counter + 1
box1, box2, box3, box4, box5, box6, box7, box8, box9 = 0, 0, 0, 0, 0, 0, 0, 0, 0
def button(x,y):
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    if(x>100 and y>100):
        pen.up()
        pen.goto(200,200)
        if(box1==0):
            count()
            if (counter == 1):
                box1 =1
            else:
                box1 =2

    elif(x<100 and x>-100 and y>100):
        pen.up()
        pen.goto(0,200)
        if (box2 == 0):
            count()
            if (counter == 1):
                box2 =1
            else:
                box2 =2
    elif(x<-100 and y>100):
        pen.up()
        pen.goto(-200,200)
        if (box3 == 0):
            count()
            if (counter == 1):
                box3 =1
            else:
                box3 =2
    elif(x>100 and y<100 and y>-100):
        pen.up()
        pen.goto(200,0)
        if (box4 == 0):
            count()
            if (counter == 1):
                box4 =1
            else:
                box4 =2
    elif(x<100 and x>-100 and y<100 and y>-100):
        pen.up()
        pen.goto(0,0)
        if (box5 == 0):
            count()
            if (counter == 1):
                box5 =1
            else:
                box5 =2
    elif(x<-100 and y<100 and y>-100):
        pen.up()
        pen.goto(-200,0)
        if (box6 == 0):
            count()
            if (counter == 1):
                box6 =1
            else:
                box6 =2
    elif(x>100 and y<-100):
        pen.up()
        pen.goto(200,-200)
        if (box7 == 0):
            count()
            if (counter == 1):
                box7 =1
            else:
                box7 =2
    elif(x<100 and x>-100 and y<-100):
        pen.up()
        pen.goto(0,-200)
        if (box8 == 0):
            count()
            if (counter == 1):
                box8 =1
            else:
                box8 =2
    elif(x<-100 and y<-100):
        pen.up()
        pen.goto(-200,-200)
        if (box9 == 0):
            count()
            if (counter == 1):
                box9 =1
            else:
                box9 =2
    else:
        pen.goto(0,0)
if(box1>0 or box2>0 or box3>0 or box4>0 or box5>0 or box6>0 or box7>0 or box8>0 or box9>0):
    if (box1 == box2 and box2 == box3 and box3==box1):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box4 == box5 and box5 == box6 and box6==box4):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box7 == box8 and box8 == box9 and box9==box7):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box3 == box6 and box6 == box9 and box9==box3):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box2 == box5 and box5 == box8 and box8==box2):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box1 == box4 and box4 == box7 and box7==box1):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box3 == box5 and box5 == box7 and box7==box3):
        pen.goto(90, 260)
        pen.forward(200)
    elif (box1 == box5 and box5 == box9 and box9==box1):
        pen.goto(90, 260)
        pen.forward(200)
turtle.onscreenclick(button,1)
turtle.done()