from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
STARTING_POSITIONS: [(0,0),(-20,0),(-40,0),(-60,0)]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#Screen Customizations
screen = Screen()
screen.setup(width= SCREEN_WIDTH, height= SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


#Object creation
snake =Snake()
food = Food()
scoreboard = Scoreboard()

# Response to user keyboard input
screen.listen()
screen.onkey(snake.up, "w" or "W")
screen.onkey(snake.down, "s" or "S")
screen.onkey(snake.left, "a" or "A")
screen.onkey(snake.right, "d" or "D")




is_game_on = True

while is_game_on:


    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(x=food) < 20:
        food.refresh()
        scoreboard.scored()
        snake.extend()

    if snake.head.xcor() > (SCREEN_WIDTH/2) or snake.head.xcor() < -(SCREEN_WIDTH/2) or snake.head.ycor() > (SCREEN_WIDTH/2) or snake.head.ycor() < -(SCREEN_WIDTH/2):
        # is_game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
        time.sleep(0.5)

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 5:
            # is_game_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()