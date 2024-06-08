from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard(snake_score=0)

    def update_scoreboard(self, snake_score):
        # self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 270)
        self.clear()
        self.write(f"Score: {snake_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 64, "bold"))

    def countdown(self, display_number):

        self.goto(0, 30)

        if display_number != 0:
            self.write(f"{display_number}", align=ALIGNMENT, font=("Courier", 84, "bold"))
        else:
            self.write(f"START", align=ALIGNMENT, font=("Courier", 64, "bold"))

        self.clear()

    def ready(self):

        self.goto(0, 30)

        self.write(f"Ready!", align=ALIGNMENT, font=("Courier", 84, "bold"))

        self.clear()
