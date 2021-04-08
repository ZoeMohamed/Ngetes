from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.scoring = 0
        self.write_score()





    def write_score(self):
        # self.scoring = 0
        self.goto(0, 250)
        self.penup()
        self.color("white")
        self.write(f"SCORE BOARD {self.scoring}", False,"center",("Arial", 20, "normal"))
        self.hideturtle()
        self.refresh()
    def refresh(self):

        self.scoring +=1


