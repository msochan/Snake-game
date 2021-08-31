from turtle import Screen
from score_board import ScoreBoard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake-game Remake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.get_head().distance(food) < 15:
        score_board.update_score(food)
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.get_head().xcor() > 280 or snake.get_head().xcor() < -280 or snake.get_head().ycor() > 280 or snake.get_head().ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.get_segments()[1:]:
        if snake.get_head().distance(segment) < 15:
            score_board.reset()
            snake.reset()

screen.exitonclick()