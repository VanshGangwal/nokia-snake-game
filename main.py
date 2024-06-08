from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard



mera_screen = Screen()
mera_screen.setup(height=620, width=620)
mera_screen.bgcolor("black")
mera_screen.title("My Snake Game")
mera_screen.tracer(0)

score_display = Scoreboard()
mera_snake = Snake()
khana = Food()
mera_screen.update()
# time.sleep(2)
mera_screen.listen()
game_on = True
count = 4

score_display.ready()
time.sleep(1.5)
mera_screen.update()

for j in range(count)[::-1]:
    score_display.countdown(display_number=j)
    time.sleep(0.75)
    mera_screen.update()


while game_on:

    mera_screen.onkey(fun=mera_snake.pause_button, key="space")

    if (not mera_snake.snake_stop) and (not mera_snake.manual_self_stop):
        mera_snake.move_snake()
        if mera_snake.head.distance(khana) < 10:
            khana.reposition_food()
            mera_snake.create_new_turtle()
            score_display.update_scoreboard(snake_score=mera_snake.score)
        mera_snake.bite_checker()
    mera_snake.i = 0
    if mera_snake.buffer is None:
        mera_snake.i = 0
        mera_screen.onkey(fun=mera_snake.point_up, key="Up")
        mera_screen.onkey(fun=mera_snake.point_down, key="Down")
        mera_screen.onkey(fun=mera_snake.point_right, key="Right")
        mera_screen.onkey(fun=mera_snake.point_left, key="Left")
        mera_screen.onkey(fun=mera_snake.create_new_turtle, key="q")

    else:
        if mera_snake.buffer == "w":
            mera_snake.point_up()
        elif mera_snake.buffer == "s":
            mera_snake.point_down()
        elif mera_snake.buffer == "d":
            mera_snake.point_right()
        elif mera_snake.buffer == "a":
            mera_snake.point_left()
        mera_snake.buffer = None

    mera_screen.onkey(fun=mera_snake.manual_switch, key="m")
    mera_screen.onkey(fun=mera_screen.bye, key="e")

    if mera_snake.manual_speed:
        mera_screen.onkey(fun=mera_snake.increase_speed, key="]")
        mera_screen.onkey(fun=mera_snake.decrease_speed, key="[")
        mera_screen.onkey(fun=mera_snake.max_speed, key="9")
        mera_screen.onkey(fun=mera_snake.min_speed, key="0")
    else:
        mera_snake.speed_moderator()

    mera_snake.border_fluidity_maintainer()

    time.sleep(mera_snake.speed_list[mera_snake.speed])
    mera_screen.update()

    if mera_snake.snake_stop:
        game_on = False
        print("Game Over !!")
        score_display.game_over()

mera_screen.exitonclick()
