import random
import turtle
from random import randint


class Food:
    def __init__(self):
        """ initialize """
        self.food = turtle.Turtle()
        self.create_food()

    def create_food(self):
        """ draw foods of snake """
        color = random.choice(["#91DCB1", "#F3E285", "#968181",
                               "#ADCCFF", "#D2B2FF"])
        self.food.speed(0)
        self.food.shape("turtle")
        self.food.shapesize(1, 1)
        self.food.color(color)
        self.food.penup()
        self.food.goto(0, 0)

    def random_food(self):
        """ Determine the position of random foods """
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.food.goto(x, y)