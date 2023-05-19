from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 24, "normal")


class ScoreBoard(Turtle):  # ScoreBoard object is also a Turtle object
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")  # so that we wont see scoreboard object moving from (0,0) to the location set in the following line
        self.goto(0, 270)
        self.score = 0
        self.print_score_board()

    def print_score_board(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def addScore(self):
        self.score += 1
        self.clear()
        self.print_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
