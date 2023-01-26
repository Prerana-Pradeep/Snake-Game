from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
WALL = 290

def snake_direction(x, y, a):
    s = 20
    if a == 0:
        x -= s
    elif a == 90:
        y -= s
    elif a == 180:
        x += s
    else:
        y += s
    return x, y


class Snake():
    def __init__(self, snake_body):
        self.segments = snake_body
        if len(snake_body) == 0:
            self.new_snake()
        else:
            self.new_body()
        self.head = self.segments[0]

    def new_snake(self):
        snake1 = Turtle("square")
        snake1.color("white")
        self.segments.append(snake1)
        print ("1")

    def new_body(self):
        i = len(self.segments) - 1
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.speed(1)
        new_snake.color("white")
        x = self.segments[i].xcor()
        y = self.segments[i].ycor()
        angle = self.segments[i].heading()
        new_cord = snake_direction(x, y, angle)
        new_snake.setpos(new_cord)
        self.segments.append(new_snake)
        print("2")

    def move(self):
        position_list = []
        j = 0
        for i in self.segments:
            i.penup()
            position_list.append(i.position())
            i.goto(position_list[j - 1])
            j += 1
        self.head.forward(DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def crash_wall(self):
        c = False
        x_cord = self.head.xcor()
        y_cord = self.head.ycor()
        if x_cord > WALL:
            c = True
        elif x_cord < -WALL:
            c = True
        elif y_cord > WALL:
            c = True
        elif y_cord < -WALL:
            c = True
        return c

    def crash_tail(self):
        c = False
        for i in self.segments[1:]:
            if self.head.distance(i) < 15:
                c = True
        return c

    def snake_reset(self):
        l = len(self.segments)
        n = 0
        while n < l:
            self.segments[n].hideturtle()
            n += 1
        self.segments = []
        self.new_snake()
        self.new_body()
        self.new_body()
        self.head = self.segments[0]




