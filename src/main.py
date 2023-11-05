import numpy as np
from enum import Enum

class Affinity(Enum):
    H = 0 ## Is hydrophobic
    P = 1 ## Is polar

class Vertice:
    def __init__(self, grid_pos, affinity, previous_point=None, next_point=None):
        self.next_point = next_point
        self.previous_point = previous_point
        self.grid_pos = grid_pos
        self.affinity =  affinity

class HPModel:
    def __init__(self):
        print("Starting model...")
        self.points = []
        self.grid_map = {}
        self.actual_vertice = None
    def start_model(self):
        print("Started Model in (0,0)")
        first_vertice = Vertice((0,0), Affinity.H, None, None)
        self.actual_vertice = first_vertice
        self.points.append(first_vertice)
        self.grid_map[first_vertice.grid_pos] = first_vertice
    def print(self):
        ## TODO: Add grid vision
        print(self.actual_vertice)

if __name__ == "__main__":
    print("Executing as main...")
    model = HPModel()
    model.start_model()
