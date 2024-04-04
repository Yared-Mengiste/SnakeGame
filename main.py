import time
from turtle import Screen
from snake import Snake
import count
from food import Food

screen = Screen()
screen.setup(1200, 700)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)
snake = Snake('white')
counter = count.Counter()
dot = Food()

screen.onkey(key='Right', fun=snake.face_right)
screen.onkey(key='Left', fun=snake.face_left)
screen.onkey(key='Up', fun=snake.face_up)
screen.onkey(key='Down', fun=snake.face_down)
game_is_on = True
screen.title('Snake Game')
while game_is_on:
    counter.print()
    if snake.distance(dot.dot_pos(), 20):
        dot.change_place(580, 320)
        snake.increase()
        counter.increase_counter()
    if snake.get_y() >= 350 or snake.get_y() <= -350 \
            or snake.get_x() >= 600 or snake.get_x() <= -600 or snake.collide():
        counter.game_over()
        game_is_on = False
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

screen.exitonclick()
