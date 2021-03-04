import turtle
import time
from random import *


def jobbra():
    fej.right(90)


def balra():
    fej.left(90)


def gyumolcs_kirak():
    x=randint(-380,300)
    y=randint(-280,280)
    gyumolcs.goto(x,y)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(jobbra, "Right")
palya.onkey(balra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

gyumolcs=turtle.Turtle()
gyumolcs.penup()
gyumolcs.shape("circle")
gyumolcs.color("red")
gyumolcs_kirak()

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.sety(240)

kijelzo2 = turtle.Turtle()
kijelzo2.color("white")
kijelzo2.hideturtle()
kijelzo2.penup()
kijelzo2.sety(240)

megevett_db=0

while True:
    fej.forward(20)
    
    if  fej.distance(gyumolcs.xcor(),gyumolcs.ycor())<15:
        gyumolcs_kirak()
        megevett_db+=1
        
    kijelzo2.clear()
    kijelzo2.write(megevett_db,font=("Arial", 36, "bold"))
    
    if 400< fej.xcor() or fej.xcor() < -400 or 300< fej.ycor()or fej.ycor() <-300:
        kijelzo.clear()
        kijelzo.write("Game over",align="center",font=("Arial", 36, "bold"))
    
    palya.update()
    time.sleep(0.3)
    