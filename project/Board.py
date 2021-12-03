import turtle
from time import sleep


class Board:

    def __init__(self):
        """ initialize """
        self.board = turtle.Screen()
        self.set_screen()
        self.painter = turtle.Turtle()

    def set_screen(self):
        """ set a background of game """

        self.board.title('Hungry Snake Game')
        self.board.bgcolor('black')
        self.board.setup(width=550, height=550)
        self.board.tracer(0)

    def show_info_player(self, name, score, best_score):
        """
        show name of player , score and the best score
        :param name, score, best_score
        :type name:str, score:int, best_score:int

        """
        self.painter.clear()
        self.painter.speed(0)
        self.painter.color('white')
        self.painter.penup()
        self.painter.hideturtle()
        self.painter.goto(0, 250)
        self.painter.write(
            f'Player: {name} Score: {score} Best Score: {best_score}',
            align='center', font=('Courier', 16, 'normal'))


if __name__ == '__main__':
    screen = Board()
    screen.show_info_player('tha', 0, 1000)
    sleep(3)
