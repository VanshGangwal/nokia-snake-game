from turtle import Turtle
from speed_list import speed_list_generator

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SPEED_INCREASE_INTERVAL = 3

color_list = ["red", "yellow", "blue", "pink"]


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]
        self.snake_stop = False
        self.manual_self_stop = False
        self.i = 0
        self.buffer = None
        self.speed_list = speed_list_generator(
            starting_speed=0.2,
            number_of_iteration=50,
            percentage_increase=10,
        )
        self.speed = 0
        self.score = 0
        self.manual_speed = False

    def pause_button(self):
        changed_state = True if self.manual_self_stop == False else False
        self.manual_self_stop = changed_state

    def create_snake(self):
        for i in range(len(STARTING_POSITIONS)):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color(color_list[i])
            # new_turtle.color("white")
            new_turtle.goto(STARTING_POSITIONS[i])
            self.all_turtles.append(new_turtle)

    def move_snake(self):
        for index in range(len(self.all_turtles)):
            if (index + 1) != len(self.all_turtles):
                self.all_turtles[len(self.all_turtles) - index - 1].setpos(
                    self.all_turtles[len(self.all_turtles) - index - 2].pos())
        self.head.forward(MOVE_DISTANCE)

    def create_new_turtle(self):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("square")
        new_turtle.color(color_list[len(self.all_turtles) % len(color_list)])
        new_turtle.goto(self.all_turtles[len(self.all_turtles) - 1].pos())
        self.all_turtles.append(new_turtle)
        self.score += 1
        print(f"Score increased to {self.score}")

    def bite_checker(self):
        '''
        :return: True if bite has taken place, else returns false
        '''
        for t in self.all_turtles:
            if t != self.head:
                if t.distance(self.head) < 10:
                    self.snake_stop = True

    def point_up(self):
        if self.i == 0:
            if self.head.heading() != 270:
                self.head.setheading(90)
                self.i += 1
        elif self.i == 1:
            self.buffer = "w"

    def point_down(self):
        if self.i == 0:
            if self.head.heading() != 90:
                self.head.setheading(270)
                self.i += 1
        elif self.i == 1:
            self.buffer = "s"

    def point_right(self):
        if self.i == 0:
            if self.head.heading() != 180:
                self.head.setheading(0)
                self.i += 1
        elif self.i == 1:
            self.buffer = "d"

    def point_left(self):
        if self.i == 0:
            if self.head.heading() != 0:
                self.head.setheading(180)
                self.i += 1
        elif self.i == 1:
            self.buffer = "a"

    def position_head(self):
        return self.head.pos()

    def border_fluidity_maintainer(self):
        if self.head.pos()[0] >= 320:
            self.head.goto(-300, self.head.pos()[1])
        elif self.head.pos()[0] <= -320:
            self.head.goto(300, self.head.pos()[1])
        if self.head.pos()[1] >= 320:
            self.head.goto(self.head.pos()[0], -300)
        if self.head.pos()[1] <= -320:
            self.head.goto(self.head.pos()[0], 300)

    def increase_speed(self):
        self.speed += 1

    def decrease_speed(self):
        self.speed -= 1

    def max_speed(self):
        self.speed = len(self.speed_list) - 1

    def min_speed(self):
        self.speed = 0

    def speed_moderator(self):
        self.speed = self.score // SPEED_INCREASE_INTERVAL

    def manual_switch(self):
        changed_state = True if self.manual_speed == False else False
        self.manual_speed = changed_state
