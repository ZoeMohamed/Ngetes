from turtle import Screen
import time
from food import Food
from snake import Snake

snake = Snake()
Foody = Food()
my_screens = Screen()
my_screens.listen()
my_screens.onkey(key="Up", fun=snake.up)
my_screens.onkey(key="Down", fun=snake.down)
my_screens.onkey(key="Left", fun=snake.left)
my_screens.onkey(key="Right", fun=snake.right)

my_screens.setup(width=600,height=600)
my_screens.bgcolor("black")





starting_pos = [(0,0),(-20,0),(-40,0)]
segments = []


game_on = True
while game_on:
    my_screens.update()
    time.sleep(0.1)

    snake.move()

    #Kita deteksi apakah snake bertabrakan dengan makanan

    if snake.segments[0].distance(Foody) < 15:
        Foody.refresh()
        score.

my_screens.exitonclick()






























#----------------------------------------------------------------------------------------------------------------------#
#SEBELUM OOP MENYERANG
# from turtle import Turtle,Screen
# import time
# from snake import Snake
#
# my_screens = Screen()
# my_screens.setup(width=600,height=600)
# my_screens.bgcolor("black")
# my_screens.tracer(0)
#
#
#
# starting_pos = [(0,0),(-20,0),(-40,0)]
# segments = []
# for pos in starting_pos:
#     bob = Turtle("square")
#     bob.color("white")
#     bob.penup()
#     bob.goto(pos)
#     segments.append(bob)
#
#
# my_screens.update()
#
#
# game_on = True
# while game_on:
#     my_screens.update()
#     time.sleep(1)
#
#     for index in range(len(starting_pos) - 1,0,-1):
#         pos_baru = segments[index - 1].xcor()
#         pos_baru_y = segments[index - 1].ycor()
#         print(pos_baru)
#         segments[index].goto(pos_baru,pos_baru_y)
#     segments[0].forward(20)
#     segments[0].left(90)
#
#
#
# my_screens.exitonclick()