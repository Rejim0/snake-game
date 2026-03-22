from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# --- Screen setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turn off auto animation — we call screen.update() manually

# --- Create game objects ---
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# --- Key bindings ---
# Tell the screen to listen for keypresses, then map each arrow key to a snake method
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# --- Game loop ---
is_game_on = True
while is_game_on:
    screen.update()  # manually refresh the screen each frame
    time.sleep(0.1)  # control game speed — lower = faster
    snake.move()  # move the snake one step forward

    # Detect collision with food
    # distance() < 15 because food is small — close enough counts as eaten
    if snake.head.distance(food) < 15:
        food.refresh()  # move food to a new random spot
        snake.extend()  # grow the snake by one segment
        scoreboard.increase_score()  # add 1 to the score

    # Detect collision with wall
    # Screen is 600x600, turtle coords go from -300 to 300, we stop at ±280
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with own tail
    # Skip segments[0] because that's the head itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

# Keep the window open until the player clicks it
screen.exitonclick()