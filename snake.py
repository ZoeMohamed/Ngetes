from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
            self.segments = []
            self.make_square()
            # self.up = up(self)
            # self.down = down(self)
            # self.left = left(self)
            # self.right = right(self)


    def make_square(self):
        for pos in STARTING_POS:
            new_turt = Turtle("square")
            new_turt.color("white")
            new_turt.penup()
            new_turt.goto(pos)
            self.segments.append(new_turt)

    def move(self):
        for index in range(len(STARTING_POS) - 1, 0, -1):
            pos_baru = self.segments[index - 1].xcor()
            pos_baru_y = self.segments[index - 1].ycor()
            # print(pos_baru)
            self.segments[index].goto(pos_baru,pos_baru_y)
        self.segments[0].forward(MOVE)
        # self.segments[0].setheading(180)
        # self.segments[0].setheading(90)



    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)


    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)


    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)














































