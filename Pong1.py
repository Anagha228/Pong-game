# Part one: getting started 

import turtle 
import time
import winsound

window = turtle.Screen()
window.title("Ping Pong game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#score 
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)#max possible speed 
paddle_a.shape("square")#default 20 x 20 pixels
paddle_a.color("red")
paddle_a.shapesize(stretch_wid= 5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)#max possible speed 
paddle_b.shape("square")#default 20 x 20 pixels
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid= 5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)#max possible speed 
ball.shape("circle")#default 20 x 20 pixels
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = -2

#pen
pen = turtle.Turtle()
pen.speed()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20 
    paddle_b.sety(y)


#keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

#main game loop 
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    #paddle and ball interaction 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor()<paddle_b.ycor() +50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        # distance from paddle center
        offset = ball.ycor() - paddle_b.ycor()
        # change vertical direction based on hit location
        ball.dy = offset * 0.1
        # reverse horizontal direction
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()<paddle_a.ycor() +50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        # distance from paddle center
        offset = ball.ycor() - paddle_a.ycor()
        # change vertical direction based on hit location
        ball.dy = offset * 0.1
        # reverse horizontal direction
        ball.dx *= -1

    if(score_a-score_b > 5):
        window.clear()
        window.bgcolor("black")
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("white")
        pen.penup()
        pen.goto(0, 0)
        pen.write("Player A Wins!", align="center", font=("Courier", 24, "normal"))

        break
    if(score_a-score_b < -5):
        window.clear()
        window.bgcolor("black")
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("white")
        pen.penup()
        pen.goto(0, 0)
        pen.write("Player B Wins!", align="center", font=("Courier", 24, "normal"))

        break
    
    
    time.sleep(0.01)
window.mainloop()