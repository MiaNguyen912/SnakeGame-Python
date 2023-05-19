from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turn off tracer so we can use screen.update()

# set up snake, food, scoreboard
snake = Snake()
food = Food()
score_board = ScoreBoard()


# set screen event listening
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()


game_is_on = True
while game_is_on:
    # make snake move forward constantly
    screen.update()  # refresh screen at the beginning and at each time all segments have moved
    time.sleep(0.1)  # delay 0.1s then refresh screen so the snake move slower
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:  # if collide
        score_board.addScore()
        food.refresh()
        snake.extend()

    # detect passing wall
    if snake.head.xcor() > 300:
        snake.head.setposition(-300, snake.head.ycor())
    elif snake.head.xcor() < -300:
        snake.head.setposition(300, snake.head.ycor())
    elif snake.head.ycor() > 300:
        snake.head.goto(snake.head.xcor(), -300)
    elif snake.head.ycor() < -300:
        snake.head.goto(snake.head.xcor(), 300)

    # detect collision with tail
    for segment in snake.segments[2:]:  # exlude 1st and 2nd segment
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
