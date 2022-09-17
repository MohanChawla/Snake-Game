from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# declaring as constant
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turning = None
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("seashell")
        # I was able to declare segments outside the init wo self but inside init we need to declare it with self only
        # using it elsewhere required using the self along with it
        # we could have included the create_snake functionality inside the init itself but looks better this way

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # sub_prob1: creating the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # position is a function of turtle class gives position
    # In the lists in python, -1 gives reference to the last element

    # sub_prob2: moving the snake
    def move(self):
        """Moves the last segment to second last segment and then moves the head forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)
        self.turning = False

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("seashell")

    # sub_prob3: controlling the snake, self turning to avoid situation where multiple
    # keys are pressed like snake in east, we press north + west which makes the snake
    # direction to opposite even before it moves causing game to end
    def up(self):
        if self.head.heading() != DOWN and not self.turning:
            self.head.setheading(UP)
            self.turning = True

    def down(self):
        if self.head.heading() != UP and not self.turning:
            self.head.setheading(DOWN)
            self.turning = True

    def left(self):
        if self.head.heading() != RIGHT and not self.turning:
            self.head.setheading(LEFT)
            self.turning = True

    def right(self):
        if self.head.heading() != LEFT and not self.turning:
            self.head.setheading(RIGHT)
            self.turning = True
