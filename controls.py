import turtle
import os

# SCREEN
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders!")
screen.bgpic("bgr.png")
screen.tracer(0)

# SHAPE
screen.register_shape("title.gif")
screen.register_shape("controls.gif")

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

# INSTRUCTIONS
text_pen = turtle.Turtle()
text_pen.speed(0)
text_pen.color("white")
text_pen.penup()
text_pen.setposition(165, 275)
textstring = "Press Q to Quit"
text_pen.write(textstring, False, align="left", font=("Arial", 14, "normal"))
text_pen.hideturtle()

# CONTROL'S TEXT
controls = turtle.Turtle()
controls.penup()
controls.setposition(0, -50)
controls.shape("controls.gif")


# FUNCTIONS
def exit_game():
	if platform.system() == "Linux":
		os.system("killall aplay")
	else:
		os.system("killall afplay")
	screen.bye()

def startGame():
	title.setposition(0, 100000)
	text_pen.setposition(0, 100000)
	controls.setposition(0, 100000)
	import spaceinvaders

###
screen.listen()
screen.onkeypress(startGame, "space")
###

# MAIN LOOP
while True:
	screen.update()