from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-200, 220)
        self.write("Level: " + str(self.level), False, align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        return self.write("Level: " + str(self.level), False, align="center", font=FONT)

    def reset_score(self):
        self.clear()
        self.level = 1
        return self.write("Level: " + str(self.level), False, align="center", font=FONT)
