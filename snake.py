from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        """add new segment to the snake"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())  # add new segment to the position of the last segment

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            # segment2 go to position of segment1, 1 go to 0, 0 move forward
            preceeding_segment_position = self.segments[segment_num - 1].position()
            self.segments[segment_num].goto(preceeding_segment_position)
        # self.segments[0].forward(MOVE_DISTANCE)
        self.head.forward(MOVE_DISTANCE)

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

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # go off the screen
        self.segments.clear()
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def stop(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            preceeding_segment_position = self.segments[segment_num].position()
            self.segments[segment_num].goto(preceeding_segment_position)
