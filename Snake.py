from turtle import  Turtle
STARRTING_POSSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTACNE =20
UP =90
DOWN =270
LEFT =180
RIGHT =0
class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head =self.segments[0]

    def create_snake(self):
        for position in STARRTING_POSSITION:
            self.add_segments(position)

    def add_segments(self,position):
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def Extend(self):
        self.add_segments(self.segments[-1].position())
    def Move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTACNE)

    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def Down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def Left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def Right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def Reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head =self.segments[0]









