from turtle import Turtle
import random


class Food(Turtle):  # Food inherit Turtle class
    def __init__(self):
        super().__init__(shape="circle")
        # self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10x10 circle
        self.color("yellow")
        self.speed("fastest")  # so that we wont see food object moving from (0,0) to the random location set in the following line
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
