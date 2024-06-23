from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anjali's Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# making the snake move
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

# collision of snake with food

    if snake.segment[0].distance(food) < 15:
         food.refresh()
         snake.extend()
         scoreboard.increase_score()


# DETECT COLLISION WITH THE WALL

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    # SLICING

    for segment in snake.segment[1:]:

        if snake.segment[0].distance(segment) < 10:
            scoreboard.reset()









screen.exitonclick()