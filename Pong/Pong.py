import turtle


wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


#Score

player_a_score= 0
player_b_score = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation, sets to max speed
paddle_a.shape("square")
paddle_a.penup()
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.penup()
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.color("white")
ball.goto(0, 0)
ball.dx = 0.3
ball.dy= 0.3

#Pen
pen =turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"PlayerA :{player_a_score}  PlayerB:{player_b_score}", align="center", font=("Courier", 24 , "normal"))

#Functions
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
	wn.update()

	#Move the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)

	if ball.ycor() >= 290:
		ball.sety(290)
		ball.dy *=-1

	if ball.ycor() <= -290:
		ball.sety(-290)
		ball.dy *=-1

	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx *=-1
		player_a_score+=1
		pen.clear()
		pen.write(f"PlayerA :{player_a_score}  PlayerB:{player_b_score}", align="center", font=("Courier", 24 , "normal"))

	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx *=-1
		player_b_score+=1
		pen.clear()
		pen.write(f"PlayerA :{player_a_score}  PlayerB:{player_b_score}", align="center", font=("Courier", 24 , "normal"))


	#Paddle and Ball collisions

	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx*=-1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx*=-1