from turtle import Turtle


def create_border(position, heading, forward):
    border = Turtle()
    border.color("orange")
    border.hideturtle()
    border.penup()
    border.pensize(width=3)
    border.goto(position)
    border.pendown()
    border.setheading(heading)
    border.forward(forward)


class Border:

    def __init__(self):
        self.create_borders()

    def create_borders(self):
        # Up Border
        create_border((-280, 280), 0, 560)
        # Left Border
        create_border((-280, 280), 270, 560)
        # Right Border
        create_border((280, 280), 270, 560)
        # Down Border
        create_border((-280, -280), 0, 560)