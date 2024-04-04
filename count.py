from turtle import Turtle
FONT = ('Courier', 24, 'normal')
ALIGNMENT = 'center'


class Counter(Turtle):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.hideturtle()
        self.penup()
        self.color('green')
        self.goto(0, 300)

    def print(self):
        self.clear()
        self.write(f'COUNTER = {self.counter} ', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f' GAME OVER  ', align=ALIGNMENT, font=FONT)

    def increase_counter(self):
        self.counter +=1