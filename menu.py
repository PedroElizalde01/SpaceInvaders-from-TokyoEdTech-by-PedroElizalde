import turtle
import os
import platform

# SCREEN
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders!")
screen.bgpic("bgr.png")
screen.tracer(0)

# SHAPE
screen.register_shape("title.gif")
screen.register_shape("arcade.gif")

# BORDER
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

# TITLE
title = turtle.Turtle()
title.penup()
title.setposition(0, 200)
title.shape("title.gif")

# MODES
modes = turtle.Turtle()
modes.penup()
modes.setposition(0, -50)
modes.shape("arcade.gif")

# SELECTION
selec = turtle.Turtle()
selec.penup()
selec.color("white")
selec.setposition(-120, 43)
selec.shape("triangle")

# FUNCTIONS
def exit_game():
	if platform.system() == "Linux":
		os.system("killall aplay")
	else:
		os.system("killall afplay")
	screen.bye()

def select_option():
	if selec.ycor() == 43:
		title.setposition(0, 100000)
		selec.setposition(0, 100000)
		modes.setposition(0, 100000)
		import controls
	#elif selec.ycor() == -50:
		
	elif selec.ycor() == -143:
		if platform.system() == "Linux":
			os.system("killall aplay")
		else:
			os.system("killall afplay")
		screen.bye()

def move_up():
	if selec.ycor() == -50:
		selec.setposition(-120, 43)
	elif selec.ycor() == -143:
		selec.setposition(-110, -50)
def move_down():
	if selec.ycor() == 43:
		selec.setposition(-110, -50)
	elif selec.ycor() == -50:
		selec.setposition(-80, -143)
# CONTROLS
screen.listen()
screen.onkeypress(exit_game, "q")
screen.onkeypress(select_option, "space")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

# MAIN LOOP
while True:
	screen.update()
