from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("black")
colors = ["red", "orange", "pink", "green", "blue", "purple"]
y_positions = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-225, y=y_positions[turtle])
    all_turtles.append(new_turtle)


user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            turtle.goto(0, 100)
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                turtle.write(f"Congratulations! The {winning_turtle} turtle is the winner!", align="center")
            else:
                turtle.write(f"Sorry. The {winning_turtle} turtle is the winner!", font="20",  align="center")
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()
