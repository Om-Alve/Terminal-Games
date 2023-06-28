import shutil
import random
from pytimedinput import timedInput
import sys
import os
import time

FIELD_HEIGHT = 4
FIELD_WIDTH = shutil.get_terminal_size().columns - 1
os.system('cls' if os.name == 'nt' else 'clear')

Cells = [(x, y) for x in range(FIELD_HEIGHT) for y in range(shutil.get_terminal_size().columns)]

score=0

def print_field():
    sys.stdout.write('\033[H\n\n')
    sys.stdout.flush()
    for cell in Cells:
        if cell == dino.position:
            print('$', end='')
        elif cell in cacti.positions:
            print('@', end='')
        elif cell[0] in [0, FIELD_HEIGHT-1] or cell[1] in [0, FIELD_WIDTH]:
            print('#', end='')
        else:
            print(" ", end="")
        if cell[1] == FIELD_WIDTH:
            print('')
    print(f"Score: {score}")


class Dino():
    def __init__(self):
        self.jump = False
        self.position = (FIELD_HEIGHT-2, 4)

    def state(self):
        if self.jump:
            self.position = (1, 4)
            self.jump = False
        else:
            self.position = (2, 4)


class Cacti():
    def __init__(self):
        self.positions = []
        self.spawn_interval = 2.0  # Adjust this value to control the interval between cactus spawns
        self.spawn_timer = 2.0

    def spawn(self):
        self.spawn_timer += 0.1
        if self.spawn_timer >= self.spawn_interval:
            if random.random() < 0.2:
                self.positions.append((FIELD_HEIGHT-2, FIELD_WIDTH-2))
                self.spawn_timer = 0.0

    def move(self):
        new_positions = []
        for position in self.positions:
            if position[1] > 0:
                new_positions.append((position[0], position[1] - 1))
        self.positions = new_positions


dino = Dino()
cacti = Cacti()

while True:
    print_field()
    i, _ = timedInput(timeout=0.3)
    if i == ' ':
        dino.jump = True
    dino.state()
    cacti.spawn()
    cacti.move()
    score+=1
    if dino.position in cacti.positions:
        print('GAME OVER!')
        break
