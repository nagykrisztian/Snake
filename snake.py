import turtle
import time


def jobbra():
  fej.right(90)


def balra():
  fej.left(90)


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

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.goto(-120,200)

while True:
  if 400< fej.xcor() or fej.xcor() < -400 or 300< fej.ycor()or fej.ycor() <-300:
    kijelzo.write("Game over",font=("Arial", 36, "bold"))
  fej.forward(20)
  palya.update()
  time.sleep(0.3)
  