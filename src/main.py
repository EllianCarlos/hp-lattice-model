from affinity import Affinity
from direction import Direction
from hp2dmodel import Hp2dModel


if __name__ == "__main__":
    print("Executing as main...")
    model = Hp2dModel()
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
    model.print()
    print(model.energy())
