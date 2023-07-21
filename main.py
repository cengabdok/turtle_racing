from turtle import Turtle,Screen
import random

is_race_on= False
screen = Screen()
screen.setup(width=600,height=500)
user_bet= screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color :")
y_positions = [200,100,0,-100,-200]
colors = ['red','green','blue','yellow','black','purple']
all_turtles = []

for i in range(0,5):

    new_turtle = Turtle(shape="turtle")
    new_turtle.turtlesize(1.5)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet :
    is_race_on=Turtle

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor()>250:
            is_race_on=False
            winning_color= turtle.pencolor()
            if winning_color ==user_bet:
                print(f"You win! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
        random_distance =random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()