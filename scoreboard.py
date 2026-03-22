from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    # Scoreboard inherits from Turtle so it can write text on screen

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()  # lift pen so moving to position doesn't draw a line
        self.goto(0, 270)  # place score text near the top of the screen
        self.hideturtle()  # hide the turtle arrow, we only want the text
        self.update_scoreboard()

    def update_scoreboard(self):
        # Write the current score on screen at the turtle's position
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # Add 1 to score, clear the old text, then redraw with new score
        self.score += 1
        self.clear()  # erase previous score text before writing new one
        self.update_scoreboard()

    def game_over(self):
        # Move to center of screen and display game over message
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
