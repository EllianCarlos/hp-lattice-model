from random import uniform
import random

import numpy as np

from lib.hp2dmodel import MODEL_INF, Hp2dSquareModel
from lib.string_to_model import load_str_from_file


class SimulatedAnnealing:
    def __init__(self, obj_func, neighbor_func: (), t_initial=10000, t_min=0.5, actual_s: Hp2dSquareModel = None, star_s: Hp2dSquareModel = None, alpha=0.95, k_iter=10, max_iter=100000):
        self.alpha = alpha
        self.k_iter = k_iter
        self.f = obj_func
        self.find_neighbor = neighbor_func
        self.star_s = star_s
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
                self.actual_s = self.find_neighbor(self.actual_s)
                i = 0

        return self.star_s


def find_best_improviment(model):
    star_switch = None
    star_energy = MODEL_INF
    for point in model.points:
        result = model.get_transformations_of_point(point)
        i_of_min_energy = np.argmin(result['energies'])
        if result['energies'][i_of_min_energy] < star_energy and result['switches'][i_of_min_energy][0] != result['switches'][i_of_min_energy][1]:
            star_switch = result['switches'][i_of_min_energy]
            star_energy = result['energies'][i_of_min_energy]
    return (star_switch, star_energy)


def find_any_diagonal_move(model):
    star_switch = None
    star_energy = MODEL_INF
    for point in model.points:
        result = model.get_transformations_of_point(point)
        i_of_min_energy = np.argmin(result['energies'])
        if result['energies'][i_of_min_energy] < MODEL_INF and result['switches'][i_of_min_energy][0] != result['switches'][i_of_min_energy][1]:
            star_switch = result['switches'][i_of_min_energy]
            star_energy = result['energies'][i_of_min_energy]
        if random.uniform(0, 1) > 0.5 and star_switch is not None:
            return (star_switch, star_energy)


def find_neighboor(model: Hp2dSquareModel):
    star_switch, _ = find_best_improviment(model)
    # star_switch, _ = find_any_diagonal_move(model)
    return model.switch_point(star_switch[0], star_switch[1])


if __name__ == "__main__":
    import sys

    args = sys.argv

    if len(args) < 2 or args[1] is None:
        raise Exception("Path was not given")

    full_path = args[1]

    model = load_str_from_file(full_path)
    model.visualize_model()

    model = find_neighboor(model)

    calculated_energy = model.get_energy()
    print(calculated_energy)

    sa = SimulatedAnnealing(
        lambda model: model.get_energy(),
        find_neighboor,
        actual_s=model,
        star_s=model)

    new_model = sa.run()
    print(new_model.get_energy())
