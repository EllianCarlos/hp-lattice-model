import numpy as np
from enum import Enum


class Affinity(Enum):
    H = 0  # Is hydrophobic
    P = 1  # Is polar


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class Color:
    GREY = '\033[90m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'


class Vertice:
    def __init__(self, grid_pos, affinity, previous_point=None, next_point=None):
        self.next_point = next_point
        self.previous_point = previous_point
        self.grid_pos = grid_pos
        self.affinity = affinity


class HPModel:
    def __init__(self):
        print("Starting model...")
        self.points = []
        self.grid_map = {}
        self.actual_vertice = None

    def start_model(self, affinity):
        print("Started Model in (0,0)")
        first_vertice = Vertice((0, 0), affinity, None, None)
        self.actual_vertice = first_vertice
        self.points.append(first_vertice)
        self.grid_map[first_vertice.grid_pos] = first_vertice
        self.left_most_point = 0
        self.right_most_point = 0
        self.bottom_most_point = 0
        self.top_most_point = 0

    def append_vertice(self, direction, affinity):
        next_vertice_grid_pos = None
        actual_pos = self.actual_vertice.grid_pos
        match direction:
            case Direction.UP:
                next_vertice_grid_pos = (actual_pos[0], actual_pos[1]+1)
            case Direction.DOWN:
                next_vertice_grid_pos = (actual_pos[0], actual_pos[1]-1)
            case Direction.LEFT:
                next_vertice_grid_pos = (actual_pos[0]-1, actual_pos[1])
            case Direction.RIGHT:
                next_vertice_grid_pos = (actual_pos[0]+1, actual_pos[1])
        if next_vertice_grid_pos in self.grid_map.keys():
            return None

        # Adding new vertice
        new_vertice = Vertice(next_vertice_grid_pos,
                              affinity, self.actual_vertice, None)
        self.actual_vertice.next_point = new_vertice
        self.actual_vertice = new_vertice
        self.grid_map[next_vertice_grid_pos] = new_vertice
        self.points.append(new_vertice)

        # Check to add new printing variables
        if next_vertice_grid_pos[0] > self.right_most_point:
            self.right_most_point = next_vertice_grid_pos[0]
        if next_vertice_grid_pos[0] < self.left_most_point:
            self.left_most_point = next_vertice_grid_pos[0]

        if next_vertice_grid_pos[1] > self.top_most_point:
            self.top_most_point = next_vertice_grid_pos[1]
        if next_vertice_grid_pos[1] < self.bottom_most_point:
            self.bottom_most_point = next_vertice_grid_pos[1]


    def print(self):
        # TODO: improve top, left, bottom and right most points
        # TODO: add warning for exceding terminal size
        top_most = max(self.top_most_point, 1)
        bottom_most = min(self.bottom_most_point, -1)
        right_most = max(self.right_most_point, 1)
        left_most = min(self.left_most_point, -1)
        for j in range(top_most, bottom_most-2, -1):
            print_str = ""
            for i in range(left_most, right_most+1, 1):
                print_pos = (i, j)
                if print_pos in self.grid_map.keys():
                    if self.grid_map[print_pos].affinity == Affinity.H:
                        print_str += Color.BLUE + "H"
                    else:
                        print_str += Color.GREEN + "P"
                else:
                    print_str += Color.GREY + "*"
            print(print_str)


if __name__ == "__main__":
    print("Executing as main...")
    model = HPModel()
    model.start_model(Affinity.P)
    model.append_vertice(Direction.DOWN, Affinity.H)
    model.print()
