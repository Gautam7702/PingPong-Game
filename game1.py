#pong game 

import turtle # used for graphics
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



# Paddle A
paddle_a = turtle.Turtle()  # builds a object of turtle
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len =1)
paddle_a.penup()  # turle by default use to leave a line as the object moves
paddle_a.goto(-350,0)  

# Paddle B
paddle_b = turtle.Turtle()  # builds a object of turtle
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len =1)
paddle_b.penup()  # turle by default use to leave a line as the object moves
paddle_b.goto(350,0)  

# Ball
ball = turtle.Turtle()  # builds a object of turtle
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()  # turle by default use to leave a line as the object moves
ball.goto(0,0)  
ball.dx = 0.2
ball.dy =0.2

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align= "center",font = ("Courier",24,"normal"))

scoreA =0
scoreB =0

#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    if y<250:
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    if y>-250:
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    if y<250:
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    if y>-250:
        paddle_b.sety(y)



# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") # That is onpressing w the paddle_a will move up
wn.onkeypress(paddle_a_down,"s") # That is onpressing s the paddle_a will move down
wn.onkeypress(paddle_b_up,"Up") # That is onpressing w the paddle_a will move up
wn.onkeypress(paddle_b_down,"Down") # That is onpressing s the paddle_a will move down


# Main game Loop
while True:
    wn.update()

    #move the ball
    dx =(random.randint(0,100)*ball.dx)/100
    dy = (random.randint(0,100)*ball.dy)/100
    ball.setx(ball.xcor()+ dx)
    ball.sety(ball.ycor()+ dy)


    # Border Checking and movement 

    if ball.ycor()>290:
            ball.sety(290)
            ball.dy = ball.dy*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy = ball.dy*-1
    
    if ball.xcor()>390:
        scoreA+=1
        ball.setx(390)
        ball.dx = ball.dx*-1
        pen.clear()
        pen.write(f"Player A:{scoreA} Player B:{scoreB}",align= "center",font = ("Courier",24,"normal")) 
    
    if ball.xcor()<-390:
        scoreB+=1
        ball.setx(-390)
        ball.dx = ball.dx*-1
        pen.clear()
        pen.write(f"Player A:{scoreA} Player B:{scoreB}",align= "center",font = ("Courier",24,"normal")) 

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor()<350) and ball.ycor()< paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor():
        ball.setx(340)
        ball.dx *=-1
    
    if (ball.xcor() < -340 and ball.xcor()<350) and ball.ycor()< paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor():
        ball.setx(-340)
        ball.dx *=-1






    
