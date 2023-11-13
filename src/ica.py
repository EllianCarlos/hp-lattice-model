from random import uniform

import numpy as np
from lib.affinity import Affinity
from lib.direction import Direction

from lib.hp2dmodel import Hp2dSquareModel


class SimulatedAnnealing:
    def __init__(self, obj_func, neighbor_func, t_initial=10000, t_min=0.5, actual_s=None, start_s=None, alpha=0.95, k_iter=10, max_iter=100000):
        self.alpha = alpha
        self.k_iter = k_iter
        self.f = obj_func
        self.find_neighbor = neighbor_func
        self.star_s = start_s
        self.t_initial = t_initial
        self.t_min = t_min
        self.actual_s = actual_s
        self.max_iter = max_iter

    def run(self):
        i = 0
        j = 0
        self.__t = self.t_initial

        while self.__t > self.t_min and j < self.max_iter:
            j += 1
            neighbor = self.find_neighbor(self.actual_s)
            delta = self.f(neighbor) - self.f(self.actual_s)
            entropy = np.exp(-delta/self.__t)
            if delta < 0 or uniform(0, 1) < entropy:
                self.actual_s = neighbor
                self.__t = self.__t * self.alpha

            if self.f(self.actual_s) < self.f(self.star_s):
                self.star_s = self.actual_s
            else:
                i += 1

            if i == self.k_iter:
                self.actual_s = self.f(self.actual_s)
                i = 0

        return self.star_s


if __name__ == "__main__":
    print()
    model = Hp2dSquareModel()
    model.start_model(Affinity.H)
    model.append_vertice(Direction.DOWN, Affinity.P)
    model.append_vertice(Direction.DOWN, Affinity.P)
    model.append_vertice(Direction.DOWN, Affinity.P)
    model.append_vertice(Direction.RIGHT, Affinity.H)
    model.append_vertice(Direction.UP, Affinity.H)
    model.append_vertice(Direction.UP, Affinity.H)
    model.append_vertice(Direction.RIGHT, Affinity.H)
    model.append_vertice(Direction.DOWN, Affinity.H)
    model.append_vertice(Direction.DOWN, Affinity.H)
    model.append_vertice(Direction.RIGHT, Affinity.P)
    model.append_vertice(Direction.UP, Affinity.H)
    model.append_vertice(Direction.RIGHT, Affinity.P)
    model.append_vertice(Direction.UP, Affinity.P)
    model.append_vertice(Direction.LEFT, Affinity.H)
    model.append_vertice(Direction.UP, Affinity.P)
    model.append_vertice(Direction.LEFT, Affinity.P)
    model.append_vertice(Direction.LEFT, Affinity.H)
    model.print_sequence()
    calculated_energy = model.energy()

    for point in model.points:
        result = model.find_transformations_of_point(point)
        print(result['energies'])
