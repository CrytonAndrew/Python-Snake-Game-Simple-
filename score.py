from turtle import Turtle


class Score(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.score_refresh()
        self.color("white")
        self.hideturtle()

    def score_refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, "normal"))
        self.setposition(x=0, y=280)

    def end_game(self):
        self.clear()
        self.color("red")
        self.write(f"Game Over (Hit Wall): {self.score} points", False, "Center", ("Arial", 20, "normal"))
        self.setposition(x=0, y=280)

    def hit_tail(self):
        self.clear()
        self.color("Red")
        self.write(f"Game Over (Hit Tail): {self.score} points", False, "Center", ("Arial", 20, "normal"))
        self.setposition(x=0, y=280)

