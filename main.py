from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snaky")
screen.tracer(0)

snake = Snake()
# starts listening to the user, keystrokes are defined like Up, Down, Left, Right and are case_sensitive
food: object = Food()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food, distance method returns the distance from (x,y)
    if snake.head.distance(food) < 15:
        food.refresh()
        # checking if the food is not generated inside the snake body
        for segment in snake.segments:
            if segment.distance(food) < 20:
                food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 279 or snake.head.xcor() < -279 or snake.head.ycor() > 279 or snake.head.ycor() < -279:
        scoreboard.reset()
        snake.reset_snake()
        # game_is_on = False
        # scoreboard.game_over()

    # Detect collision with tail
    # if the head collides with any segment in the tail, trigger game_over sequence
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()
            # game_is_on = False
            # scoreboard.game_over()



screen.exitonclick()

# range function comes from c, so it doesn't take named arguments
# for seg_num in range(start = 2, stop = 0, step = -1)
# for looping like 1,2,3 we'll have start = 1, stop = 3 and step = 1 and for 3,2,1 it'll be start =3, stop = 1,
# step = -1. We move from last seg to second last seg and so on

# tracer function turn turtle animation on/off and set delay. Need to use update to tell the draw screen
# This is needed so we can hide the work happening in the bg and then when all work is done we refresh the
# graphics or draw the screen

# time.sleep() sleeps the screen
# for seg in segments:
#    seg.forward(20)
# change of logic, instead of moving each segment separately which would make it impossible to turn direction
# we'll use logic of moving the last segment to second last and continue till the length

# after creating the basic logic of moving the snake, we'll tidy up the code and use separate class for the snake's
# behaviour and appearance and then a class for food and a class for scoreboard. This way we implement the OOPs. All of
# these classes will be in separate files managing the specific things. The goal of the refactoring is so that we can
# create a separate file snake.py and import snake in the main and just create an object of the snake and while the game
# is running we will have the snake (object) to continuously move forward
