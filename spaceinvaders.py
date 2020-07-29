# SPACE INVADERS
import turtle
import os
import math
import random
import platform
import time
from threading import Timer

if platform.system() == "Windows":
	try:
		import winsound
	except:
		print("Winsound module not available.")

# SCREEN
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders!")
wn.bgpic("bgr.png")
wn.tracer(0)

# SHAPES
wn.register_shape("invader.gif")
wn.register_shape("player.gif")
wn.register_shape("bullet.gif")
wn.register_shape("missile.gif")

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

# SCORE
score = 0
intScore = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-200, 275)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# LEVEL
level = 1
level_pen = turtle.Turtle()
level_pen.speed(0)
level_pen.color("white")
level_pen.penup()
level_pen.setposition(-290, 275)
levelString = "Level: {}".format(level)
level_pen.write(levelString, False, align="left", font=("Arial", 14, "normal"))
level_pen.hideturtle()

# INSTRUCTIONS
text_pen = turtle.Turtle()
text_pen.speed(0)
text_pen.color("white")
text_pen.penup()
text_pen.setposition(165, 275)
textstring = "Press Q to Quit"
text_pen.write(textstring, False, align="left", font=("Arial", 14, "normal"))
text_pen.hideturtle()

# PLAYER
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)
player.speed = 0

# BULLET
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.setposition(0, 1000)
bullet.shapesize(0.4, 0.4)
bulletspeed = 4

bulletstate = "ready"

# ENEMIES
enemiesNum = 30
enemies = []
for i in range(enemiesNum):
	enemies.append(turtle.Turtle())
enemyspeed = 0.2

# MISSILE
missile = turtle.Turtle()
missile.color("yellow")
missile.shape("missile.gif")
missile.penup()
missile.speed(0)
missile.setheading(90)
missile.setposition(0, 0)
missile.shapesize(0.4, 0.4)
missileSpeed = 2

# FUNCTIONS
def move_left():
	player.speed = -0.7

def move_right():
	player.speed = 0.7

def move_player():
	x = player.xcor()
	x += player.speed
	if x < -280:
		x = -280
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	global bulletstate
	if bulletstate == "ready":
		play_sound("laser.wav")
		bulletstate = "fire"
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()



def fire_missile():
	n = random.randint(0, enemiesNum - 1)
	x = enemies[n].xcor()
	y = enemies[n].ycor() - 10
	print(y)
	if y < 300:
		play_sound("laser.wav")
		missile.setposition(x, y)
		missile.showturtle()
	else:
		fire_missile()

def isCollision(a, b):
    return math.sqrt(math.pow(a.xcor()-b.xcor(),2)+math.pow(a.ycor()-b.ycor(),2)) < 15

def play_sound(soundFile, time = 0):
	if platform.system() == "Windows":
		winsound.PlaySound(soundFile, winsound.SND_ASYNC)
	elif platform.system() == "Linux":
		os.system("aplay -q {}&".format(soundFile))
	else:
		os.system("afplay {}&".format(soundFile))

	if time > 0:
		turtle.ontimer(lambda: play_sound(soundFile, time), t=int(time * 1000))

def exit_game():
	if platform.system() == "Linux":
		os.system("killall aplay")
	else:
		os.system("killall afplay")
	wn.bye()

def enemySpawn(): 
	enemy_start_x = -225
	enemy_start_y = 250
	enemy_number = 0
	for enemy in enemies:
		enemy.color("red")
		enemy.shape("invader.gif")
		enemy.penup()
		enemy.speed(0)
		x = enemy_start_x + (50 * enemy_number)
		y = enemy_start_y
		enemy.setposition(x, y)
		enemy_number += 1
		if enemy_number == 10:
			enemy_start_y -= 45
			enemy_number = 0

t=0
def timeCounter():
	global t
	t += 1
	print(t)
	if t == 5:
		Timer(1.0, timeCounter).start()
		t = 0
		fire_missile()
	else:
		Timer(1.0, timeCounter).start()



# CONTROLS
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(fire_bullet, "space")
wn.onkeypress(exit_game, "q")

wn.onkeypress(fire_missile, "m")



# MUSIC
play_sound("background_music.wav", 114)

# MAIN GAME LOOP
enemySpawn()

n = 0

timeCounter()


while True:	
	

	wn.update()
	move_player()
	
	

	for enemy in enemies:
		x = enemy.xcor()
		x+= enemyspeed
		enemy.setx(x)			
		
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)	
			enemyspeed *= -1

		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		if isCollision(bullet, enemy):
			bullet.hideturtle()
			bulletstate == "ready"
			bullet.setposition(400, -400)
			enemy.setposition(0, 5000)
			play_sound("explosion.wav")
			score += 10
			intScore += 10
			scorestring = "Score: {}".format(score)
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

		if enemy.ycor() < -275:
			play_sound("explosion.wav")
			player.hideturtle
			enemy.hideturtle
			print("GAME OVER")
			exit_game()
	
	# BULLET MOVEMENT
	if bulletstate == "fire":
		y = bullet.ycor()
		y+= bulletspeed
		bullet.sety(y)
	
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"
	
	# MISSILE MOVEMENT
	y = missile.ycor()
	y -= missileSpeed
	missile.sety(y)

	if missile.ycor() < -275:
		missile.hideturtle()

	# GAME RULES
	if intScore == 300:
		level += 1
		levelString = "Level: {}".format(level)
		level_pen.clear()
		level_pen.write(levelString, False, align="left", font=("Arial", 14, "normal"))
		n += 1
		if n == 2:
			enemyspeed *= 1.2
			n = 0
		intScore = 0
		enemySpawn()
	
	#Timer(5, fire_missile).start()
	

