import numpy as np
from affinity import Affinity
from direction import Direction
from vertice import Vertice
from print_utils import ShellColors


class Hp2dModel:
    # TODO: Add possiblity of 3 dimensions
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
                        print_str += ShellColors.BLUE + "H"
                    else:
                        print_str += ShellColors.GREEN + "P"
                else:
                    print_str += ShellColors.GREY + "*"
            print(print_str)

    def energy(self):
        # TODO: add doc for energy calculation
        energy = 0
        for i in range(len(self.points)-1):
            for j in range(i+2, len(self.points)):
                point1 = self.points[i]
                point2 = self.points[j]
                distance = np.linalg.norm(
                    np.array(list(point1.grid_pos)) - np.array(list(point2.grid_pos)))
                if point1.affinity == point2.affinity and point1.affinity == Affinity.H and distance == 1:
                    energy += 1
        return -energy
