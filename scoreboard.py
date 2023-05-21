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
        with open("data.txt") as score_file:
            self.high_score = int(score_file.read())
        self.is_lost = False
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def addScore(self):
        self.score += 1
        self.update_score_board()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as score_file:
                score_file.write(f"{self.high_score}")

        self.is_lost = True
        self.update_score_board()
        self.goto(0, 0)
        self.write("GAME OVER. Tab [space] to restart", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        self.score = 0
        self.is_lost = True
        self.goto(0, 270)
        self.update_score_board()
