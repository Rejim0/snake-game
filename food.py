from turtle import Turtle
import random


class Food(Turtle):
    # Food inherits from Turtle so it can appear on screen as a shape

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()  # lift pen so it doesn't draw lines when moving
        self.speed("fastest")  # teleport instantly, no animation delay
        # Make the food smaller than a full turtle square (0.5 = half size = ~10px)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # Place food at a random position to start
        self.refresh()

    def refresh(self):
        # Move food to a new random position snapped to the 20px grid
        # Multiplying by 20 ensures food always lands on the same grid as the snake
        # So the snake can actually perfectly collide with it
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)
