import turtle
import random


class Snake:

    def __init__(self):
        """ initialize """
        self.head = turtle.Turtle()
        self.tail = []
        self.create_head()

    def create_head(self):
        """ draw head of snake by turtle """

        self.head.shape('circle')
        self.head.shapesize(1, 1)
        self.head.color('white')
        self.head.penup()
        self.head.goto(0, 100)
        self.head.way = 'stop'

    def increase_tail(self, food):
        """
        draw tails of snake and random foods on the screen
        :param food
        :type food:object

        """
        color = random.choice(["#CDF1AE", "#D2F8DD", "#F7E9D1",
                               "#F4D2B5", "#EAB7B7", '#B89ACF', '#A1E6FD',
                               '#FEF4BE', '#F7DA95'])
        if self.head.distance(food.food) < 20:
            food.random_food()
            tail = turtle.Turtle()
            tail.speed(2)
            tail.shape('turtle')
            tail.color(color)
            tail.penup()
            self.tail.append(tail)

    def up(self):
        if self.head.way != 'down':
            self.head.way = 'up'

    def down(self):
        if self.head.way != 'up':
            self.head.way = 'down'

    def right(self):
        if self.head.way != 'left':
            self.head.way = 'right'

    def left(self):
        if self.head.way != 'right':
            self.head.way = 'left'

    def move(self):
        """ Determine the distance to walk each step of snake."""

        if self.head.way == 'up':
            y = self.head.ycor()
            self.head.sety(y + 10)
        if self.head.way == 'down':
            y = self.head.ycor()
            self.head.sety(y - 10)
        if self.head.way == 'left':
            x = self.head.xcor()
            self.head.setx(x - 10)
        if self.head.way == 'right':
            x = self.head.xcor()
            self.head.setx(x + 10)

    def is_collide(self):
        """
        Determine If a snake hits border or hits its own tail, snake will die.
        :return is_collide_border or is_collide_tail

        """
        is_collide_border = self.head.xcor() > 250 or self.head.xcor() < -250 \
                            or self.head.ycor() > 250 or self.head.ycor() < -250

        is_collide_tail = any(
            [body.distance(self.head) < 5 for body in self.tail])

        return is_collide_border or is_collide_tail

    def update_tail(self):
        """ Update the position in list of tail."""
        for i in range(len(self.tail) - 1, 0, -1):
            x = self.tail[i - 1].xcor()
            y = self.tail[i - 1].ycor()
            self.tail[i].goto(x, y)
        if len(self.tail) > 0:
            x = self.head.xcor()
            y = self.head.ycor()
            self.tail[0].goto(x, y)
        self.move()

    @property
    def score(self):
        """ set score of the Snake """
        return len(self.tail) * 100

    def reset_snake(self):
        """ clear list of tail when a snake dies to restart a game """
        for tail in self.tail:
            tail.goto(1000, 1000)
        self.tail.clear()
