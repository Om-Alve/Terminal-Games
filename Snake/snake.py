import random
from pytimedinput import timedInput
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

FIELD_HEIGHT = 16
FIELD_WIDTH = 32

Cells = [(x, y) for x in range(FIELD_HEIGHT) for y in range(FIELD_WIDTH)]
Direction = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}


def print_field():
    sys.stdout.write('\033[H\n\n')
    sys.stdout.flush()
    for cell in Cells:
        if cell in snake.body:
            print('X', end='')
        elif cell[0] in [0, FIELD_HEIGHT-1] or cell[1] in [0, FIELD_WIDTH-1]:
            print('#', end='')
        elif cell == apple.position:
            print('A', end='')
        else:
            print(" ", end="")
        if cell[1] == FIELD_WIDTH-1:
            print('')


class Apple():
    def __init__(self, snake):
        self.position = (random.randint(1, FIELD_HEIGHT-2), random.randint(1, FIELD_WIDTH-2))
        self.snake = snake

    def update(self):
        if self.snake.body[0] == self.position:
            self.position = (random.randint(1, FIELD_HEIGHT-2), random.randint(1, FIELD_WIDTH-2))
            while self.position in self.snake.body:
                self.position = (random.randint(1, FIELD_HEIGHT-2), random.randint(1, FIELD_WIDTH-2))
            self.snake.eat = True


class Snake():
    def __init__(self):
        self.body = [(8, 16), (8, 17), (8, 18)]
        self.eat = False

    def move(self, direction):
        self.body.insert(0, (self.body[0][0] + direction[0], self.body[0][1] + direction[1]))
        if not self.eat:
            self.body.pop(-1)
        else:
            self.eat = False


snake = Snake()
apple = Apple(snake)
direction = Direction['left']

while True:
    print_field()
    d, _ = timedInput(timeout=0.3)
    match d:
        case 'w':
            direction = Direction['up']
        case 'a':
            direction = Direction['left']
        case 's':
            direction = Direction['down']
        case 'd':
            direction = Direction['right']
        case 'q':
            break
    if snake.body[0] in snake.body[1:] or snake.body[0][0] in [0,FIELD_HEIGHT-1] or snake.body[0][1] in [0,FIELD_WIDTH-1]:
        print('Game Over!')
        break
    
    snake.move(direction)
    apple.update()
