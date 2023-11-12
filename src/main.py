
from lib.affinity import Affinity
from lib.direction import Direction
from lib.hp2dmodel import Hp2dSquareModel


if __name__ == "__main__":
    print("Executing as main...")
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
    model.visualize_model()
    model.print_sequence()
    calculated_energy = model.energy()

