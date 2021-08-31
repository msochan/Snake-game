import this
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.__segments = []
        self.create_snake()
        self.__head = self.__segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.__segments.append(new_segment)

    def reset(self):
        for seg in self.__segments:
            seg.goto(1000, 1000)
        
        self.__segments.clear()
        self.create_snake()
        self.__head = self.__segments[0]

    def extend(self):
        self.add_segment(self.__segments[-1].pos())

    def move(self):
        for i in range(len(self.__segments) - 1, 0, -1):
            new_x = self.__segments[i - 1].xcor()
            new_y = self.__segments[i - 1].ycor()
            self.__segments[i].goto(x=new_x, y=new_y)
        self.__head.forward(20)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)

    def get_head(self):
        return self.__head
    
    def get_segments(self):
        return self.__segments
