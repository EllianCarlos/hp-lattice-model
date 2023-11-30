from random import uniform

import numpy as np

from lib.hp2dmodel import MODEL_INF, Hp2dSquareModel
from lib.string_to_model import get_filename_from_args, load_str_from_file


"""The Simulated Annealing Algorithm
        - Based around the termodynamics
        - Does local search
        - Has a random probabilistic factor to run of local optimal
"""


class SimulatedAnnealing:
    """ Initializes the SA class
        obj_func -> The objective function, the function to be minimized
        neighbor_func -> The function to find a neighbor of the current moedl
        t_initial -> Initial Temperature of the Algorithm
        t_min -> Minimal temperature of the algorithm, below this the algorithm will no improve
        actual_s ->
        star_s ->
        alpha ->
        k_iter ->
        max_iter ->

    """

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

    """Runs the algorithm with the given parameters
    """

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

            if self.f(self.actual_s) <= self.f(self.star_s):
                self.star_s = self.actual_s
            else:
                i += 1

            if i == self.k_iter:
                self.actual_s = self.find_neighbor(self.actual_s)
                i = 0

        return self.star_s


"""Function to find the best switch of a H point that minimizes the energy function
"""


def find_best_improviment(model: Hp2dSquareModel):
    star_switch = None
    star_energy = MODEL_INF
    for point in model.points:
        result = model.get_transformations_of_point(point)
        i_of_min_energy = np.argmin(result['energies'])
        if result['energies'][i_of_min_energy] < star_energy and result['switches'][i_of_min_energy][0] != result['switches'][i_of_min_energy][1]:
            star_switch = result['switches'][i_of_min_energy]
            star_energy = result['energies'][i_of_min_energy]
    return (star_switch, star_energy)


"""Function to find the any switch of a H point that minimizes the energy function
"""


def find_any_diagonal_move(model: Hp2dSquareModel):
    star_switch = None
    star_energy = MODEL_INF

    # Analyses the possible transformation of every point the model
    for point in model.points:
        result = model.get_transformations_of_point(point)

        # Finds the one that minimizes the energy
        i_of_min_energy = np.argmin(result['energies'])

        # If its better than the actual best, keeps it
        if result['energies'][i_of_min_energy] < MODEL_INF and result['switches'][i_of_min_energy][0] != result['switches'][i_of_min_energy][1]:
            star_switch = result['switches'][i_of_min_energy]
            star_energy = result['energies'][i_of_min_energy]

        # If there was any switch in the run, returns its
        if star_switch is not None and star_energy < MODEL_INF:
            return (star_switch, star_energy)


def find_neighboor(model: Hp2dSquareModel):
    # The find_best_improviment function is way slower than the find_any_diagonal_move in the average case, and the find_any_diagonal_move should be better to run from local optima.

    star_switch, _ = find_best_improviment(model)
    # star_switch, _ = find_any_diagonal_move(model)
    return model.switch_point(star_switch[0], star_switch[1])


if __name__ == "__main__":
    full_path = get_filename_from_args()

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
