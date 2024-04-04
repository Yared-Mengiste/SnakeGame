from turtle import Turtle


class Snake:
    def __init__(self, color):
        self.snakes = []
        self.color = color
        temp_tim = Turtle(shape='circle')
        temp_tim.penup()
        temp_tim.color(self.color)
        self.snakes.append(temp_tim)
        self.increase()
        self.increase()

    def increase(self):
        snake_part = Turtle(shape='square')
        snake_part.color(self.color)
        snake_part.penup()
        x_cor = self.snakes[-1].xcor()
        y_cor = self.snakes[-1].ycor()
        if self.snakes[-1].heading() == 0:
            snake_part.goto(x_cor - 20, y_cor)
            self.snakes.append(snake_part)
        elif self.snakes[-1].heading() == 90:
            snake_part.goto(x_cor, y_cor - 20)
            self.snakes.append(snake_part)
        elif self.snakes[-1].heading() == 180:
            snake_part.goto(x_cor + 20, y_cor)
            self.snakes.append(snake_part)
        elif self.snakes[-1].heading() == 270:
            snake_part.goto(x_cor, y_cor + 20)
            self.snakes.append(snake_part)

    def face_up(self):
        if self.snakes[0].heading() == 180:
            self.snakes[0].right(90)
        elif self.snakes[0].heading() == 0:
            self.snakes[0].left(90)

    def face_down(self):
        if self.snakes[0].heading() == 180:
            self.snakes[0].left(90)
        elif self.snakes[0].heading() == 0:
            self.snakes[0].right(90)

    def face_right(self):
        if self.snakes[0].heading() == 90:
            self.snakes[0].right(90)
        elif self.snakes[0].heading() == 270:
            self.snakes[0].left(90)

    def face_left(self):
        if self.snakes[0].heading() == 90:
            self.snakes[0].left(90)
        elif self.snakes[0].heading() == 270:
            self.snakes[0].right(90)

    def distance(self, pos, size):
        return self.snakes[0].distance(pos) < size

    def move_forward(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            self.snakes[snake].goto(self.snakes[snake - 1].pos())
        self.snakes[0].forward(20)

    def collide(self):
        for snake in self.snakes[1:]:
            if self.distance(snake.pos(), 10):
                return True

    def get_x(self):
        return self.snakes[0].xcor()

    def get_y(self):
        return self.snakes[0].ycor()
