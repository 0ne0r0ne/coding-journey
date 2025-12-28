from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def reset(self):
        for _ in self.turtle_list:
            _.goto(2345,234234)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for m in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[m - 1].xcor()
            new_y = self.turtle_list[m - 1].ycor()
            self.turtle_list[m].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
