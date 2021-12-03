from database import Database
from Board import Board
from Snake import Snake
from Game import Food
from random import randint
import turtle
import time

data = Database()
board = Board()
screen = board.board
snake = Snake()
food = Food()
up, down, right, left = snake.up, snake.down, snake.right, snake.left

name_input = turtle.textinput('Welcome, Snake will eat turtles!!',
                              'Enter your name:')
# keyboard control
screen.listen()
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(right, "d")
screen.onkey(left, "a")
delay = 0.1

# main
while True:
    screen.update()
    best_score = data.get_score(name_input)

    if snake.is_collide():
        time.sleep(1)
        snake.head.goto(0, 0)
        snake.head.way = 'stop'
        data.update_best_score(name_input, snake.score)
        snake.reset_snake()

    snake.increase_tail(food)
    snake.update_tail()
    board.show_info_player(name_input, snake.score, best_score)

if __name__ == '__main__':
    turtle.mainloop()
