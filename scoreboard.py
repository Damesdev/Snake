from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.get_highscore()
        self.hideturtle()
        self.penup()
        self.goto(10, 370)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align="Center", font=("Ariel", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", align="Center", font=("Ariel", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore()
        self.score = 0
        self.update_scoreboard()


    def scored(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def get_highscore(self):
        with open("highscore.txt") as file:
            highest_score = file.read()
            self.highscore = int(highest_score)

    def update_highscore(self):
        with open("highscore.txt", mode= "w") as file:
            new_highscore = str(self.highscore)
            file.write(new_highscore)
