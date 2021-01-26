from turtle import Turtle


class Snake:
    starting_positions = [(0, 0), (-10.5, 0), (-20.5, 0)]

    def __init__(self, screen):
        self.segments = []
        self.screen = screen
        self.create_snake()

    def turn_left(self):
        self.segments[0].left(90)

    def turn_right(self):
        self.segments[0].right(90)

    def turn_down(self):
        if self.segments[0].heading() == 180 or self.segments[0].heading() == 0:
            self.segments[0].setheading(270)

    def up(self):
        if self.segments[0].heading() == 180 or self.segments[0].heading() == 0:
            self.segments[0].setheading(90)

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.color("white")
        new_segment.penup()
        new_segment.shape("square")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def increase_size(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(20)
        self.screen.onkey(key="d", fun=self.turn_right)
        self.screen.onkey(key="a", fun=self.turn_left)
        self.screen.onkey(key="s", fun=self.turn_down)
        self.screen.onkey(key="w", fun=self.up)
        self.screen.onkey(key="Up", fun=self.up)
        self.screen.onkey(key="Down", fun=self.turn_down)
        self.screen.onkey(key="Left", fun=self.turn_left)
        self.screen.onkey(key="Right", fun=self.turn_right)
        self.screen.listen()

    def get_turtle(self):
        return self.segments[0]
