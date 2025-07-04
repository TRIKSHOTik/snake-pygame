import random

CELL_SIZE = 30
WIDTH, HEIGHT = 1600, 1600

class Field:
    def __init__(self, cell):
        self.cell = cell

    def generate_food(self):
        while True:
            x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
            if (x, y) not in self:
                return (x, y)