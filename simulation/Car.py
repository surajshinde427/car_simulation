DIRECTIONS = ['N', 'E', 'S', 'W']

MOVE_MAP = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}


class Car:
    def __init__(self, name, x, y, direction, commands):

        if direction not in DIRECTIONS:
            raise ValueError(f"Invalid direction '{direction}' for car {name}. Must be one of {DIRECTIONS}")
        if not all(c in 'LRF' for c in commands):
            raise ValueError(f"Invalid commands for car {name}. Only L, R, F are allowed.")
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = list(commands)
        self.active = True
        self.step = 0

    def turn_left(self):
        match self.direction:
            case 'N':
                self.direction = 'W'
            case 'W':
                self.direction = 'S'
            case 'S':
                self.direction = 'E'
            case 'E':
                self.direction = 'N'

    def turn_right(self):
        match self.direction:
            case 'N':
                self.direction = 'E'
            case 'E':
                self.direction = 'S'
            case 'S':
                self.direction = 'W'
            case 'W':
                self.direction = 'N'

    def move_forward(self, width, height):
        dx, dy = MOVE_MAP[self.direction]
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < width and 0 <= new_y < height:
            self.x = new_x
            self.y = new_y
        else:
            print(f"[Warning] Car {self.name} attempted to move outside the field and stayed at ({self.x},{self.y}).")

    def current_position(self):
        return (self.x, self.y)

    def next_command(self):
        if self.step < len(self.commands):
            command = self.commands[self.step]
            self.step += 1
            return command
        return None
